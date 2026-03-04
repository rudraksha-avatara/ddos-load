#!/usr/bin/env python3
"""
DDoS Load Tool
High-performance DDoS load  for powerful servers
"""

import asyncio
import aiohttp
import time
import argparse
from datetime import datetime
from collections import defaultdict
import statistics
import json
import random
import string
import sys
from urllib.parse import urlparse, urlencode

class AdvancedLoadTester:
    def __init__(self, url, num_requests, concurrency, duration=None, 
                 method='GET', headers=None, body=None, timeout=30,
                 no_cache=False, random_user_agent=False, keep_alive=True,
                 verify_ssl=True, rate_limit=None):
        self.url = url
        self.num_requests = num_requests
        self.concurrency = concurrency
        self.duration = duration
        self.method = method.upper()
        self.headers = headers or {}
        self.body = body
        self.timeout = timeout
        self.no_cache = no_cache
        self.random_user_agent = random_user_agent
        self.keep_alive = keep_alive
        self.verify_ssl = verify_ssl
        self.rate_limit = rate_limit
        
        self.results = defaultdict(int)
        self.response_times = []
        self.errors = []
        self.start_time = None
        self.end_time = None
        self.completed_requests = 0
        self.bytes_received = 0
        self.request_counter = 0
        
        # User agents for rotation
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        ]
    
    def get_cache_busting_url(self):
        """Add cache-busting parameter to URL"""
        if not self.no_cache:
            return self.url
        
        # Generate random string for cache busting
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        separator = '&' if '?' in self.url else '?'
        return f"{self.url}{separator}_nocache={random_str}&_t={int(time.time() * 1000)}"
    
    def get_request_headers(self):
        """Get headers for request with optional cache control and user agent"""
        headers = self.headers.copy()
        
        if self.no_cache:
            headers.update({
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache',
                'Expires': '0'
            })
        
        if self.random_user_agent:
            headers['User-Agent'] = random.choice(self.user_agents)
        
        return headers
        
    async def send_request(self, session):
        """Send a single async HTTP request"""
        try:
            # Rate limiting
            if self.rate_limit:
                await asyncio.sleep(1.0 / self.rate_limit)
            
            url = self.get_cache_busting_url()
            headers = self.get_request_headers()
            
            start = time.time()
            
            async with session.request(
                self.method,
                url,
                headers=headers,
                data=self.body,
                timeout=aiohttp.ClientTimeout(total=self.timeout),
                ssl=self.verify_ssl
            ) as response:
                content = await response.read()
                elapsed = time.time() - start
                
                self.results[response.status] += 1
                self.response_times.append(elapsed)
                self.completed_requests += 1
                self.bytes_received += len(content)
                
        except asyncio.TimeoutError:
            self.results['timeout'] += 1
            self.errors.append('Timeout')
        except aiohttp.ClientError as e:
            self.results['connection_error'] += 1
            self.errors.append(f'Connection: {str(e)[:50]}')
        except Exception as e:
            self.results['error'] += 1
            self.errors.append(f'Error: {str(e)[:50]}')
    
    async def worker(self, session, request_queue):
        """Worker coroutine that processes requests from queue"""
        while True:
            try:
                await request_queue.get()
                await self.send_request(session)
                request_queue.task_done()
            except asyncio.CancelledError:
                break
    
    async def run_duration_test(self):
        """Run test for a specific duration"""
        print(f"Running duration-based test for {self.duration} seconds...")
        
        connector = aiohttp.TCPConnector(
            limit=self.concurrency,
            limit_per_host=self.concurrency,
            ttl_dns_cache=300,
            force_close=not self.keep_alive
        )
        
        async with aiohttp.ClientSession(connector=connector) as session:
            self.start_time = time.time()
            end_time = self.start_time + self.duration
            
            tasks = []
            while time.time() < end_time:
                if len(tasks) < self.concurrency:
                    task = asyncio.create_task(self.send_request(session))
                    tasks.append(task)
                else:
                    done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            
            if tasks:
                await asyncio.wait(tasks)
            
            self.end_time = time.time()
    
    async def run_count_test(self):
        """Run test for a specific number of requests"""
        print(f"Running request-based test with {self.num_requests} requests...")
        
        request_queue = asyncio.Queue()
        for _ in range(self.num_requests):
            request_queue.put_nowait(None)
        
        connector = aiohttp.TCPConnector(
            limit=self.concurrency,
            limit_per_host=self.concurrency,
            ttl_dns_cache=300,
            force_close=not self.keep_alive
        )
        
        async with aiohttp.ClientSession(connector=connector) as session:
            self.start_time = time.time()
            
            workers = [
                asyncio.create_task(self.worker(session, request_queue))
                for _ in range(self.concurrency)
            ]
            
            await request_queue.join()
            
            for worker in workers:
                worker.cancel()
            
            await asyncio.gather(*workers, return_exceptions=True)
            
            self.end_time = time.time()
    
    async def run(self):
        """Execute the load test"""
        print(f"\n{'='*70}")
        print(f"Advanced Load Testing Tool - Production Ready")
        print(f"{'='*70}")
        print(f"Target URL: {self.url}")
        print(f"Method: {self.method}")
        print(f"Concurrency: {self.concurrency}")
        if self.duration:
            print(f"Duration: {self.duration} seconds")
        else:
            print(f"Total Requests: {self.num_requests}")
        print(f"Timeout: {self.timeout}s")
        print(f"Cache Busting: {'Enabled' if self.no_cache else 'Disabled'}")
        print(f"Random User-Agent: {'Enabled' if self.random_user_agent else 'Disabled'}")
        print(f"Keep-Alive: {'Enabled' if self.keep_alive else 'Disabled'}")
        print(f"SSL Verification: {'Enabled' if self.verify_ssl else 'Disabled'}")
        if self.rate_limit:
            print(f"Rate Limit: {self.rate_limit} req/s")
        print(f"{'='*70}\n")
        print(f"Starting test at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...\n")
        
        if self.duration:
            await self.run_duration_test()
        else:
            await self.run_count_test()
        
        self.print_results()
    
    def print_results(self):
        """Print detailed test results"""
        duration = self.end_time - self.start_time
        total_requests = sum(self.results.values())
        
        print(f"\n{'='*70}")
        print(f"Test Results")
        print(f"{'='*70}")
        print(f"Completed in: {duration:.2f} seconds")
        print(f"Total requests: {total_requests}")
        print(f"Successful requests: {self.completed_requests}")
        print(f"Failed requests: {total_requests - self.completed_requests}")
        print(f"Requests per second: {total_requests/duration:.2f}")
        print(f"Average concurrency: {self.concurrency}")
        
        if self.bytes_received > 0:
            mb_received = self.bytes_received / (1024 * 1024)
            throughput = mb_received / duration
            print(f"Data received: {mb_received:.2f} MB")
            print(f"Throughput: {throughput:.2f} MB/s")
        
        print(f"\n{'='*70}")
        print(f"Status Code Distribution:")
        print(f"{'='*70}")
        for status, count in sorted(self.results.items()):
            percentage = (count/total_requests*100) if total_requests > 0 else 0
            bar_length = int(percentage / 2)
            bar = '█' * bar_length
            print(f"  {str(status):>20}: {count:>6} ({percentage:>5.1f}%) {bar}")
        
        if self.response_times:
            self.response_times.sort()
            avg_time = statistics.mean(self.response_times)
            median_time = statistics.median(self.response_times)
            min_time = min(self.response_times)
            max_time = max(self.response_times)
            
            try:
                stdev_time = statistics.stdev(self.response_times)
            except:
                stdev_time = 0
            
            percentiles = {
                50: self.response_times[int(len(self.response_times)*0.50)],
                75: self.response_times[int(len(self.response_times)*0.75)],
                90: self.response_times[int(len(self.response_times)*0.90)],
                95: self.response_times[int(len(self.response_times)*0.95)],
                99: self.response_times[int(len(self.response_times)*0.99)],
            }
            
            print(f"\n{'='*70}")
            print(f"Response Time Statistics (milliseconds):")
            print(f"{'='*70}")
            print(f"  Average:  {avg_time*1000:>8.2f}ms")
            print(f"  Median:   {median_time*1000:>8.2f}ms")
            print(f"  Std Dev:  {stdev_time*1000:>8.2f}ms")
            print(f"  Min:      {min_time*1000:>8.2f}ms")
            print(f"  Max:      {max_time*1000:>8.2f}ms")
            print(f"\n  Percentiles:")
            for p, value in percentiles.items():
                print(f"    {p}th:    {value*1000:>8.2f}ms")
        
        if self.errors:
            error_counts = defaultdict(int)
            for error in self.errors:
                error_counts[error] += 1
            
            print(f"\n{'='*70}")
            print(f"Error Summary:")
            print(f"{'='*70}")
            for error, count in sorted(error_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"  {error}: {count}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors)-10} more errors")
        
        success_rate = (self.results.get(200, 0) / total_requests * 100) if total_requests > 0 else 0
        print(f"\n{'='*70}")
        print(f"Summary:")
        print(f"{'='*70}")
        print(f"  Success Rate (200 OK): {success_rate:.2f}%")
        print(f"  Failed Requests: {total_requests - self.results.get(200, 0)}")
        print(f"  Throughput: {total_requests/duration:.2f} req/s")
        if self.response_times:
            print(f"  Avg Response Time: {avg_time*1000:.2f}ms")
        print(f"{'='*70}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Advanced Load Testing Tool - Production Ready High-Performance Testing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic test with 10,000 requests and 100 concurrent connections
  python main.py http://localhost:8000 -n 10000 -c 100
  
  # Test with cache busting enabled (bypass all caches)
  python main.py http://localhost:8000 -n 5000 -c 100 --no-cache
  
  # Run for 60 seconds with 200 concurrent connections
  python main.py http://localhost:8000 -d 60 -c 200
  
  # Maximum stress test with all features
  python main.py http://localhost:8000 -n 50000 -c 500 --no-cache --random-ua
  
  # POST request with custom headers and body
  python main.py http://localhost:8000/api -n 5000 -c 50 -m POST \\
    -H "Content-Type: application/json" --body '{"test": "data"}'
  
  # Rate-limited test (100 requests per second)
  python main.py http://localhost:8000 -n 1000 -c 10 --rate-limit 100
        """
    )
    
    parser.add_argument('url', help='Target URL to test')
    parser.add_argument('-n', '--requests', type=int, default=1000,
                       help='Total number of requests (default: 1000)')
    parser.add_argument('-c', '--concurrency', type=int, default=50,
                       help='Number of concurrent connections (default: 50)')
    parser.add_argument('-d', '--duration', type=int,
                       help='Test duration in seconds (overrides -n)')
    parser.add_argument('-m', '--method', default='GET',
                       help='HTTP method: GET, POST, PUT, DELETE, etc. (default: GET)')
    parser.add_argument('-H', '--header', action='append',
                       help='Custom header (format: "Key: Value"), can be used multiple times')
    parser.add_argument('--body', help='Request body for POST/PUT requests')
    parser.add_argument('--timeout', type=int, default=30,
                       help='Request timeout in seconds (default: 30)')
    parser.add_argument('--no-cache', action='store_true',
                       help='Enable cache busting (adds random parameters and cache headers)')
    parser.add_argument('--random-ua', action='store_true',
                       help='Use random User-Agent headers for each request')
    parser.add_argument('--no-keep-alive', action='store_true',
                       help='Disable HTTP keep-alive (creates new connection each time)')
    parser.add_argument('--no-verify-ssl', action='store_true',
                       help='Disable SSL certificate verification (use for self-signed certs)')
    parser.add_argument('--rate-limit', type=int,
                       help='Limit requests per second (e.g., 100 for 100 req/s)')
    
    args = parser.parse_args()
    
    if not args.url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)
    
    headers = {}
    if args.header:
        for header in args.header:
            if ':' in header:
                key, value = header.split(':', 1)
                headers[key.strip()] = value.strip()
    
    print("\n" + "="*70)
    print("LOAD TESTING TOOL - PRODUCTION READY")
    print("="*70)
    print("\nWARNING: Only test systems you own or have permission to test!")
    print("Unauthorized load testing may be illegal.\n")
    
    tester = AdvancedLoadTester(
        url=args.url,
        num_requests=args.requests,
        concurrency=args.concurrency,
        duration=args.duration,
        method=args.method,
        headers=headers,
        body=args.body,
        timeout=args.timeout,
        no_cache=args.no_cache,
        random_user_agent=args.random_ua,
        keep_alive=not args.no_keep_alive,
        verify_ssl=not args.no_verify_ssl,
        rate_limit=args.rate_limit
    )
    
    try:
        asyncio.run(tester.run())
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user!")
        if tester.start_time:
            tester.end_time = time.time()
            tester.print_results()
        sys.exit(0)

if __name__ == '__main__':
    main()
