# 5. 함수

## [1. 15596 - 정수 N개의 합](https://github.com/laphayen/coding_test_python/tree/main/BAEKJOON/5.%20%ED%95%A8%EC%88%98/15596.py)
* 문제
	* 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

	* 작성해야 하는 함수는 다음과 같다.

	* Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
		* a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
		* 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

* 출처
	* 문제를 만든 사람: baekjoon

* 알고리즘 분류
	* 수학
	* 구현
	* 사칙연산

* 제출할 수 있는 언어
	* C++17, Java 8, Python 3, C11, PyPy3, C99, C++98, C++11, C++14, Go, C99 (Clang), C++98 (Clang), C++11 (Clang), C++14 (Clang), C11 (Clang), C++17 (Clang)

* 채점 및 기타 정보
	* 예제는 채점하지 않는다.

* * *

## [2. 1065 - 구간 합 구하기 4](https://github.com/laphayen/coding_test_python/blob/main/BAEKJOON/5.%20%ED%95%A8%EC%88%98/1065.py)
* 문제
	* 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

* 입력
	* 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

* 출력
	* 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

* 제한
	* 1 ≤ N ≤ 100,000
	* 1 ≤ M ≤ 100,000
	* 1 ≤ i ≤ j ≤ N

* 예제 입력1
<pre><code>5 3
5 4 3 2 1
1 3
2 4
5 5</code></pre>

* 예제 출력1
<pre><code>12
9
1</code></pre>

* 출처
	* 문제를 만든 사람: baekjoon
	* 데이터를 추가한 사람: djm03178

* 알고리즘 분류
	* 누적합

* * *
