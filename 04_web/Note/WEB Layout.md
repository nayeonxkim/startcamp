# WEB Layout

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-09-09-35-15-image.png)

Normal Flow : 왼쪽 -> 오른쪽, 위 -> 아래로 붙는 구조

---

# Float

- 좀 옛날거임

>  float 주고난 다음 박스는 `clear:both;` 해주어야 기존의 Nomal Flow 를 그대로 따라가지 않고, float이 없을 때의 Normal Flow에서의 위치를 지킨다,



### clear : both; 설정하지 않은 경우

![](WEB%20Layout_assets/2023-03-09-09-55-18-image.png)



### clear : both; 설정한 경우

![](WEB%20Layout_assets/2023-03-09-09-56-05-image.png)

---

# Flexbox

### justify-content

- 메인축을 기준으로 공간배분

![](WEB%20Layout_assets/2023-03-09-10-24-07-image.png)




- space-between : 아이템 사이의 간격이 일정

- space-around : 아이템을 둘러싼 간격이 일정

- space-evenly : 모든 여백을 일정하게



### align

- 교차축을 기준으로 정렬
