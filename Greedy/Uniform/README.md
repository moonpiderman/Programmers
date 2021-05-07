# No.42862

## Quiz

![initial](https://user-images.githubusercontent.com/70942197/116208970-65c31880-a77c-11eb-8f0a-d0ec1b6f0833.png)

## fail

1. fail을 보면 중첩반복문으로 인해 시간복잡도가 O(n^2)로 되었다.
2. 그리고 들어오는 리스트에 직접적으로 쿼리를 가해줬기 때문에 문제가 생긴 것이 아닌가 하는 생각도 들었다.

## Solution

1. lost, reverse 각각 서로가 가진 원소가 없는 리스트를 생성해준다.
2. 그 다음은 간단하다. los에 r-1이나 r+1에 해당하는 값이 존재한다면 삭제한다.
3. answer는 n 값에 los의 길이 만큼 빼준다. 즉 삭제되고 없는 녀석들만큼 빼준다.
