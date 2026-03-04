#!/usr/bin/env python3
"""
DDoS Attack Tool
A legitimate tool for testing website performance under heavy traffic
"""

import requests
import threading
import time
from datetime import datetime
from collections import defaultdict
import argparse

class LoadTester:
    def __init__(self, url, num_requests, num_threads, timeout=10):
        self.url = url
        self.num_requests = num_requests
        self.num_threads = num_threads
        self.timeout = timeout
        self.results = defaultdict(int)
        self.response_times = []
        self.lock = threading.Lock()
        self.start_time = None
        self.end_time = None
        
    def send_request(self):
        """Send a single HTTP request and record the result"""
        try:
            start = time.time()
            response = requests.get(self.url, timeout=self.timeout)
            elapsed = time.time() - start
            
            with self.lock:
                self.results[response.status_code] += 1
                self.response_times.append(elapsed)
                
        except requests.exceptions.Timeout:
            with self.lock:
                self.results['timeout'] += 1
        except requests.exceptions.ConnectionError:
            with self.lock:
                self.results['connection_error'] += 1
        except Exception as e:
            with self.lock:
                self.results['error'] += 1
    
    def worker(self, requests_per_thread):
        """Worker thread that sends multiple requests"""
        for _ in range(requests_per_thread):
            self.send_request()
    
    def run(self):
        """Execute the load test"""
        print(f"\n{'='*60}")
        print(f"Load Testing Tool")
        print(f"{'='*60}")
        print(f"Target URL: {self.url}")
        print(f"Total Requests: {self.num_requests}")
        print(f"Concurrent Threads: {self.num_threads}")
        print(f"Timeout: {self.timeout}s")
        print(f"{'='*60}\n")
        
        requests_per_thread = self.num_requests // self.num_threads
        remainder = self.num_requests % self.num_threads
        
        threads = []
        self.start_time = time.time()
        
        print(f"Starting test at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
        
        for i in range(self.num_threads):
            extra = 1 if i < remainder else 0
            thread = threading.Thread(target=self.worker, args=(requests_per_thread + extra,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        self.end_time = time.time()
        self.print_results()
    
    def print_results(self):
        """Print test results"""
        duration = self.end_time - self.start_time
        total_requests = sum(self.results.values())
        
        print(f"\n{'='*60}")
        print(f"Test Results")
        print(f"{'='*60}")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Requests per second: {total_requests/duration:.2f}")
        print(f"\nStatus Codes:")
        for status, count in sorted(self.results.items()):
            print(f"  {status}: {count} ({count/total_requests*100:.1f}%)")
        
        if self.response_times:
            self.response_times.sort()
            avg_time = sum(self.response_times) / len(self.response_times)
            min_time = min(self.response_times)
            max_time = max(self.response_times)
            p50 = self.response_times[len(self.response_times)//2]
            p95 = self.response_times[int(len(self.response_times)*0.95)]
            p99 = self.response_times[int(len(self.response_times)*0.99)]
            
            print(f"\nResponse Times:")
            print(f"  Average: {avg_time*1000:.2f}ms")
            print(f"  Min: {min_time*1000:.2f}ms")
            print(f"  Max: {max_time*1000:.2f}ms")
            print(f"  50th percentile: {p50*1000:.2f}ms")
            print(f"  95th percentile: {p95*1000:.2f}ms")
            print(f"  99th percentile: {p99*1000:.2f}ms")
        
        print(f"{'='*60}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Load Testing Tool - Test website performance under heavy traffic'
    )
    parser.add_argument('url', help='Target URL to test (e.g., http://localhost:8000)')
    parser.add_argument('-n', '--requests', type=int, default=100,
                       help='Total number of requests (default: 100)')
    parser.add_argument('-t', '--threads', type=int, default=10,
                       help='Number of concurrent threads (default: 10)')
    parser.add_argument('--timeout', type=int, default=10,
                       help='Request timeout in seconds (default: 10)')
    
    args = parser.parse_args()
    
    # Validate URL
    if not args.url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        return
    
    tester = LoadTester(args.url, args.requests, args.threads, args.timeout)
    tester.run()

if __name__ == '__main__':
    main()
