# 6. 문자열

## [1. 11654 - 아스키 코드](https://github.com/laphayen/coding_test_python/blob/main/BAEKJOON/6.%20%EB%AC%B8%EC%9E%90%EC%97%B4/11654.py)
* 문제
	* 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

* 입력
	* 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

* 출력
	* 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

* 예제 입력1
<pre><code>A</code></pre>

* 예제 출력1
<pre><code>65</code></pre>

* 예제 입력2
<pre><code>C</code></pre>

* 예제 출력2
<pre><code>67</code></pre>

* 예제 입력3
<pre><code>0</code></pre>

* 예제 출력3
<pre><code>48</code></pre>

* 예제 입력4
<pre><code>9</code></pre>

* 예제 출력4
<pre><code>57</code></pre>

* 예제 입력5
<pre><code>a</code></pre>

* 예제 출력5
<pre><code>97</code></pre>

* 예제 입력6
<pre><code>z</code></pre>

* 예제 출력6
<pre><code>122</code></pre>

* 출처
	* 문제를 만든 사람: baekjoon
	* 문제의 오타를 찾은 사람: eric00513

* 알고리즘 분류
	* 구현

* * *

## [2. 11720 - 숫자의 합](https://github.com/laphayen/coding_test_python/blob/main/BAEKJOON/6.%20%EB%AC%B8%EC%9E%90%EC%97%B4/11720.py)
* 문제
	* N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

* 입력
	* 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

* 출력
	* 입력으로 주어진 숫자 N개의 합을 출력한다.

* 예제 입력1
<pre><code>1
1</code></pre>

* 예제 출력1
<pre><code>1</code></pre>

* 예제 입력2
<pre><code>5
54321</code></pre>

* 예제 출력2
<pre><code>15</code></pre>

* 예제 입력3
<pre><code>25
7000000000000000000000000</code></pre>

* 예제 출력3
<pre><code>7</code></pre>

* 예제 입력4
<pre><code>11
10987654321</code></pre>

* 예제 출력4
<pre><code>46</code></pre>

* 출처
	* 문제를 만든 사람: baekjoon
	* 데이터를 추가한 사람: jh05013

* 알고리즘 분류
	* 수학
	* 구현
	* 문자열

* * *

## [3. 10809 - 알파벳 찾기](https://github.com/laphayen/coding_test_python/blob/main/BAEKJOON/6.%20%EB%AC%B8%EC%9E%90%EC%97%B4/10809.py)
* 문제
	* 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

* 입력
	* 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

* 출력
	* 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

	* 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

* 예제 입력1
<pre><code>baekjoon</code></pre>

* 예제 출력1
<pre><code>1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1</code></pre>

* 출처
	* 문제를 만든 사람: baekjoon
	* 잘못된 데이터를 찾은 사람: djm03178
	* 데이터를 추가한 사람: djm03178

* 알고리즘 분류
	* 구현
	* 문자열

* * *

## [4. 2675 - 문자열 반복](https://github.com/laphayen/coding_test_python/blob/main/BAEKJOON/6.%20%EB%AC%B8%EC%9E%90%EC%97%B4/2675.py)
* 문제
	* 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

	* QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%x+-./: 이다.

* 입력
	* 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

* 출력
	* 각각 테스트 케이스에 대해 P를 출력한다.

* 예제 입력1
<pre><code>2
3 ABC
5 /HTP</code></pre>

* 예제 출력1
<pre><code>AAABBBCCC
/////HHHHHTTTTTPPPPP</code></pre>

* 출처
	* ICPC > Regionals > North America > Greater New York Region > 2011 Greater New York Programming Contest A번
	* 문제를 번역한 사람: baekjoon
	* 문제의 오타를 찾은 사람: jh05013
	* 잘못된 데이터를 찾은 사람: pichulia

* 알고리즘 분류
	* 구현
	* 문자열

* * *

## [5. 1157 - 단어 공부](https://github.com/laphayen/coding_test_python/blob/main/BAEKJOON/6.%20%EB%AC%B8%EC%9E%90%EC%97%B4/1157.py)
* 문제
	* 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

* 입력
	* 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

* 출력
	* 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

* 예제 입력1
<pre><code>Mississipi</code></pre>

* 예제 출력1
<pre><code>?</code></pre>

* 예제 입력2
<pre><code>zZa</code></pre>

* 예제 출력2
<pre><code>Z</code></pre>

* 예제 입력3
<pre><code>z</code></pre>

* 예제 출력3
<pre><code>Z</code></pre>

* 예제 입력4
<pre><code>baaa</code></pre>

* 예제 출력5
<pre><code>A</code></pre>

* 출처
	* 문제를 만든 사람: author5
	* 데이터를 추가한 사람: jh05013, rnjs4197

* 알고리즘 분류
	* 구현
	* 문자열

* * *
