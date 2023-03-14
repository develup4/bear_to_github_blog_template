# 프로젝트 소개
이 곳은 개인 Github 블로그를 운영하던 Repository이지만, 지금은 `Notion`으로 옮겨가서 Blog Template으로 용도가 변경되었습니다. 메모앱인 `Bear🧸`를 통해 게시글을 작성하고 블로그에 배포하는데 최적화되어 있습니다. 이 블로그는 `Minimal Mistakes`를 기본으로 디자인을 일부 수정한 템플릿입니다. 제목 아래 소제목과 이모지가 붙는 형태의 디자인은 `https://parksb.github.io`를 참고했습니다.

## 스크린샷
<img width="1370" alt="image" src="https://user-images.githubusercontent.com/8960704/224723659-593a36f6-5f6d-46f3-8a7c-e2515a5790f7.png">
<img width="1368" alt="image" src="https://user-images.githubusercontent.com/8960704/224723839-f40d5d17-c3ed-4ec9-97a5-dd2f94ad8f4b.png">

## 사용법
### Bear 앱에서 게시글을 작성하십시오
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/8960704/224724866-b98f89f4-c6de-4f32-82cc-683bdfb6a685.png">


양식은 위 사진과 같이,
- 첫 줄에 H1으로 제목을 작성합니다.
- 둘째 줄에 H2로 부제목을 작성합니다.
- 셋째 줄에 H3로 작성 날짜를 적습니다.
- 넷째줄에 해시태그#를 사용하여 태그를 작성합니다. 이때 첫번째 태그는 카테고리가 되며 태그에서는 제외됩니다.
- 그 뒤의 본문은 자유롭게 작성합니다.
- `_posts` 경로의 예제 포스트를 참고하십시오.

### Bear 앱에서 마크다운으로 Export하십시오
<img width="787" alt="image" src="https://user-images.githubusercontent.com/8960704/224726439-060a7fc3-3aea-45aa-af00-482209ad0568.png">


`메모 내보내기` 기능을 선택하고,


<img width="1141" alt="image" src="https://user-images.githubusercontent.com/8960704/224726301-c783cf9c-e0b9-4215-9c9a-eecb12c7e8e3.png">


`마크다운` 형식으로 export합니다. 위치는 `_drafts`로 합니다.


### 완전한 마크다운 형식으로 변환하기
Bear는 깔끔한 메모를 작성할 수 있지만 완벽한 형태의 Markdown을 지원하지 않습니다. 블로그에서도 정상적으로 Bear 앱에서 보는 것처럼 포스트를 보여줄 수 없으므로 스크립트를 통해 이를 변환해야 합니다.
- `scripts/publish.sh`를 실행해서 `_drafts` 디렉토리의 파일들을 변환하고 `_posts` 경로로 이동시킵니다.
- 실제 로직은 `_drafts/publish.py`라는 Python 스크립트로 되어 있습니다.
- `_posts`를 GitHub에 반영하면 포스트가 게시됩니다.


### 로컬 서버 실행하기
실제 포스트되는 모습을 확인하고 싶은 경우에는 `scripts/run_server.sh`을 실행하십시오. 로컬에서 블로그 서버가 실행되며 작성한 포스트가 어떻게 보이는지 확인할 수 있습니다.


## Reference
### [Minimal Mistakes Jekyll theme](https://mmistakes.github.io/minimal-mistakes/)
### 박성범 블로그(https://parksb.github.io)

## License
MIT license
