### 🧑‍💻 [방문 길이](https://programmers.co.kr/learn/courses/30/lessons/49994)

> - 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
> > - U: 위쪽으로 한 칸 가기
> > - D: 아래쪽으로 한 칸 가기
> > - R: 오른쪽으로 한 칸 가기
> > - L: 왼쪽으로 한 칸 가기
> - 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
![initial](https://user-images.githubusercontent.com/70942197/124545623-5939fb00-de64-11eb-9b0d-94c0eb38ee80.png)
> - 예를 들어, "ULURRDLLU"로 명령했다면
![initial](https://user-images.githubusercontent.com/70942197/124545660-6951da80-de64-11eb-9c6b-de5d198fe2d5.png)
> > - 1번 명령어부터 7번 명령어까지 다음과 같이 움직입니다.
![initial](https://user-images.githubusercontent.com/70942197/124545693-78388d00-de64-11eb-8f1b-f7eb2bdedbd8.png)
> > - 8번 명령어부터 9번 명령어까지 다음과 같이 움직입니다.
![initial](https://user-images.githubusercontent.com/70942197/124545744-88506c80-de64-11eb-8385-2eee725253eb.png)
> - 이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. (8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)
> - 단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.
> - 예를 들어, "LULLLLLLU"로 명령했다면
![initial](https://user-images.githubusercontent.com/70942197/124545799-9d2d0000-de64-11eb-8d70-dada3af03763.png)
> > - 1번 명령어부터 6번 명령어대로 움직인 후, 7, 8번 명령어는 무시합니다. 다시 9번 명령어대로 움직입니다.
![initial](https://user-images.githubusercontent.com/70942197/124545837-ab7b1c00-de64-11eb-99d6-8759683daabc.png)
> - 이때 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.
> - 명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

> 제한 사항
> 
> - dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
> - dirs의 길이는 500 이하의 자연수입니다.

> 입출력 예
> 
> |dirs|answer|
> |:---|:---|
> |"ULURRDLLU"|7|
> |"LULLLLLLU"|7|
