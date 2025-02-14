### 🧑‍💻 문제 No. 43165

> n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
> 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
>
>> - -1+1+1+1+1 = 3
>> - +1-1+1+1+1 = 3
>> - +1+1-1+1+1 = 3
>> - +1+1+1-1+1 = 3
>> - +1+1+1+1-1 = 3
>
> 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

> 제한사항
>> - 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
>> - 각 숫자는 1 이상 50 이하인 자연수입니다.
>> - 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

> 입출력 예
>> |numbers|target|return|
>> |:---|:---|:---|
>> |[1, 1, 1, 1, 1]|3|5|

### 🧑‍💻 Solution

> 1. stack과 queue 두가지로 풀 수 있다.
> 2. numbers를 전부 탐색했는지 확인하기 위해서 인덱스 값을 부여해서 비교해준다.
> 3. 이 때 stack이나 queue를 딕셔너리처럼 key와 value를 사용한다.
> 4. 입력받은 첫번째 값을 pop 해주어서 queue나 stack에 넣어준다.
> 여기서 -1을 곱해준 두 값을 지정해준다.
> 5. 더하거나 빼준 total 값을 다음 value 값(-1을 곱해준 것 혹은 그렇지 않은 것)과 더해준다.
> 6. numbers를 모두 탐색했다면, total값과 target이 같은지 비교 후에, 같으면 answer에 +1
