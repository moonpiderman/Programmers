# No.42840

## Quiz

![initial](https://user-images.githubusercontent.com/70942197/116193061-b8dfa000-a769-11eb-8d92-ffa53e8edd50.png)

## Solution

1. 각 학생마다의 규칙적인 범위 내의 작성할 정답을 리스트로 만들어준다.
2. answers의 위치에 따라 각 배열을 나눠서 정답체크를 check_n 변수에 count해준다
3. resource 리스트에 각 학생마다의 맞춘 문제의 수를 저장한다.
4. enumerate 함수를 사용해서 max 함수로 가장 많이 문제를 맞춘 학생을 answer 리스트에 저장해준다.
5. 이 때 맞춘 문제의 수가 같은 학생의 문제도 append를 이용하면 처리해줄 수 있다.
