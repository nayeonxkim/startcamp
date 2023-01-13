# GitHub

GitLab: <mark>컴퓨터 옮기면 git 작성자 선언 다시</mark>

GItHub: <mark>자격 증명 관리자 → Windows 자격 증명의 깃허브 제거 → </mark>

### TIL 폴더 생성

desktop 디렉토리에 TIL 디렉토리 생성

- TIL을 working directory로 만듦
  
  - `git init`
  
  - <span style="color:mediumturquoise">(master)</span> 붙음, repository 생성됨 (git이라는 숨은 폴더)

- READEME.md 파일 생성
  
  - `touch README.md`

- README.md를 Staging Area에 add
  
  - `git add README.md`
  
  - 새로운 버전을 만들기 위해 변경사항을 모아둔 장소

- README.md를 Repository에 commit
  
  - `git commit -m "메시지"`
  
  - 새로운 버전으로 커밋

---

### README.md를 열어 내용 작성하기

- `start README.md`

- 내용작성

- `git add README.md`

- `git commit -m "add text"`

---

### Commit 시에 메시지를 입력하지 않은 경우

- 메시지 입력창 뜸

- **Insert** 키: 메시지 입력 모드, **Esc** 키: 입력 완료

- 공백은 **#** 입력

- **: w q Enter** : 메시지 입력 종료

---

### GitHub에 올리기

- `git remote add origin 주소` : 주소를 origin이라는 원격저장소로 만든다.

- `git push origin master` : origin저장소에 master가 작업한 것을 올린다.

- 로그인 토큰: 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

---

### GitHub에서 파일 받아오기

- `git clone 레파지토리http` : 원격저장소에서 최초로 프로젝트를 받아올 때

- `git pull origin master` : clone 해 둔 repository를 최신 버전으로 받아오는 것
