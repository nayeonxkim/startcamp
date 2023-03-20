## CSS 정의 방법

1. 인라인 inline
- html 파일 내 태그 안에 `style='color:black'` 작성
2. 내부 참조 
- html 파일 내 `<head>` 에 `<style>` 태그 작성
3. 외부참조
- CSS 파일을 따로 작성하고, html 파일에 `<link>` 태그로 불러오기

---

## CSS 적용 우선순위

!important > 인라인 > id > class, 속성 > 요소

![](C:\Users\Nayeon\AppData\Roaming\marktext\images\2023-03-19-16-56-58-image.png)

1 : orange

2 : blue

3 : green

4 : green

5 : red

6 : darkviolet

7 : yellow

8 : darkviolet



**class 두 개인 태그 ?**

- 클래스가 두 개라면 css파일에서 **나중에 정의된 값**이 우선적용된다.

- 3, 4는 blue, green 두 개의 클래스를 가진다. : css 파일 상에서 green에 대한 값이 나중에 정의되어있으므로 두 값모두 green이 적용된다.

---

## CSS 상속

부모 요소의 속성을 자식에게 상속하는 것.

- 상속 되는 것 
  
  - Text관련 요소 : font, color, text-align
  
  - opacity, visibility

- 상속 되지 않는 것
  
  - Box model 관련 요소 : width, height, margin, padding, border, box-sizing, display
  
  - position 관련 요소 : position, top/right/left, z-index

---

## CSS Box Model

- 모든 요소는 **박스 모델**이고 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다. (Normal Flow)

![](C:\Users\Nayeon\AppData\Roaming\marktext\images\2023-03-19-17-09-03-image.png)

content > padding > border > margin

- 기본적으로 모든 요소의 box-sizing은 content-box
  
  - 내가 설정한 width, height가 content를 기준으로 적용된다.
  
  - 따라서 padding, border, margin이 적용된 실제 박스의 크기는 내가 생각한 박스의 크기와 다를 수 있다.

- 따라서 box-sizing을 border-box로 바꾸어주는 것이 사이즈 계산하기 편하다.
  
  - border까지의 사이즈를 박스의 사이즈로 본다.

---

## CSS Display

기본 디스플레이 : block, inline

- block 
  
  - 줄 바꿈이 일어나는 요소
  
  - **가로 폭 전체를 차지한다. : 너비를 전체길이보다 작게 따로 지정해준다면 남은 부분을 자동으로 margin으로 채운다.**
  
  - 블록 요소 안에 인라인 요소 들어갈 수 있다.
  
  - div, ul, p, hr, form 등

- inline
  
  - 줄 바꿈이 일어나지 않는 요소
  
  - 기본 너비는 컨텐츠 영역만큼
  
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  
  - **상하여백은 line-height로 지정한다.**
  
  - span, a, img, input/label 등

- 
  

---

### 블록 요소의 수평 정렬

**block은 이미 가로 전체를 꽉차게 차지하고 있는데, 어떻게 수평정렬을 하나?**

- 블록 자체는 수평 정렬할 수 없다.

- 따라서 margin을 조정하여 content를 옮겨서 **정렬된 것처럼 보이게 하는 것이다.**

---

### 인라인 요소의 수평 정렬

text-align

---

### none 디스플레이

- 해당 요소를 화면에 표시하지 않고 공간도 부여하지 않는다.

- **visibility : hidden 은 화면에 표시하지 않지만 공간은 부여함.**

---

## CSS Position

1. static : 기본값

2. relative : 기존 위치 대비 이동 
   
   - top : 100px; left : 100px;
   
   - 기존 위치가 0, 0임.
   
   - 기존 위치를 기준으로 위쪽 면, 왼쪽 면이 100px씩 이동

3. absolute : **normal flow 벗어남.** 부모/조상위치를 기준으로 이동
   
   - normal flow를 벗어나므로, 아래에 다른 요소가 있었다면 그 요소가 위로 밀고 올라온다.

4. fixed : **normal flow를 벗어남.** Viewport를 기준으로 위치한다. 
   
   - 창의 크기와 상관없이 특정 위치에 고정된다.
   
   - **스크롤해도 같은 자리에 고정된다**.

5. sticky : 원래는 static처럼 있지만 스크롤 위치가 특정 값에 이르면 fixed됨.

**<mark>absolute, fixed는 normal flow를 벗어난다.</mark>**

---

## Float

- 박스를 Normal Flow에서 제거한다.

---

## Flex 디스플레이

- 기존에 요소를 Normal Flow에서 제거하기 위해서 사용한 방법?
  
  - position의 absolute, fixed와 Float
  
  - 아이템 수직 정렬과 아이템을 일정하게 배치하기 어렵다.

- 부모요소 (컨테이너)에 `display : flex `를 지정해주어 사용한다.

---

### flex 디스플레이의 속성들

1. flex-direction : main axis의 방향 설정

2. flex-wrap : wrap하면 화면이 줄어들 때 요소가 아래로 내려간다.

-> flex-flow : direction고 wrap한꺼번에 설정 가능

3. justify-content : main axis를 기준으로 공간 배분
- space-between : 요소 사이의 공간을 일정하게

- space-around : 요소 주변공간 (양옆끝)도 포함하여 일정하게
4. align-content : cross axis를 기준으로 공간 배분 (**두 줄 이상이어야 확인 가능**)

5. align-items : cross axis를 기준으로 정렬

6. align-self : 개별 아이템을 정렬하는 방법

---

## CDN

- 여러 노드를 가진 네트워크에서 데이터를 제공하는 시스템. 

- 개별 end-user와 가까운 서버를 통해 데이터를 빠르게 전달한다.

- 외부 서버를 활용하여 메인 서버의 부하를 줄인다.

---

## Bootstrap Grid system

- flexbox로 제작된다.

- container, rows, column으로 컨텐츠를 배치 및 정렬한다.

- **12개의 column**

- **6개의 grid breakpoints** : none < sm < md < lg < xl < xxl


