# CLAUDE.md

Warding 앱의 기획·디자인 초안 레포다. 코드는 두지 않는다. 사람용 규칙은 [README.md](README.md)에 있고, 이 파일은 Claude가 작업할 때 지키는 규칙이다. claude.ai 채팅에서 작업한다면 이 파일, `README.md`, `policy/design.md`, `assets/tokens.css`를 Project 지식에 올린다.

모든 산출물은 **한국어**로 쓴다.

## 기획 (md)

- 새 기능은 `templates/spec.md`를 `features/<slug>/spec.md`로 복사해서 시작한다. 섹션은 지우지 않는다. 쓸 게 없으면 "해당 없음"이나 "안 그림"이라고 적는다.
- **결정**에는 날짜, 누가 정했는지, 근거를 같이 쓴다. 근거가 없는 결정은 **미결**에 둔다.
- **필요한 API · 데이터**에는 이미 있는 것과 새로 필요한 것을 나눠 적는다. 엔드포인트가 있는지 모르겠으면 추측하지 말고 "확인 필요"라고 쓴다.
- 결정과 미결은 md에만 쓴다. 목업 html에 노트를 길게 달지 않는다. html은 무거워서 다른 사람의 Claude가 읽기 비싸다.

## 목업 (html)

- 파일 하나로 만든다(`features/<slug>/mockup.html`). 외부 의존은 Google Fonts와 `../../assets/tokens.css`만 쓴다.
- 폰 프레임 폭은 **375px**, 다크 전용이다. 배경은 `var(--narDark800)`이다.
- 색은 `tokens.css`의 변수만 쓴다. 필요한 색이 없으면 hex를 박지 말고 PR 설명에 "토큰 추가 필요"라고 적는다. 앱의 `AppColors`에 먼저 추가돼야 한다.
- 디자인 규칙은 [policy/design.md](policy/design.md)를 따른다.
- 이미지는 prod URL(Cloudinary, `static.lolesports.com`)을 직접 참조한다. **base64로 박지 않는다.** diff가 안 보인다.
- **공개 레포다.** 실유저 닉네임#태그, `memberId`, 유저 업로드 이미지 URL(`community/<memberId>/...`), 글 제목·본문을 넣지 않는다. 커뮤니티류 데이터는 예시 데이터로 만든다.
- 어떤 값이 실데이터이고 어떤 값이 지어낸 것인지 spec의 미결 또는 한계 항목에 적는다.

## 작업 흐름

- `main`에 직접 커밋하지 않는다. `feat/<slug>` 브랜치에서 PR을 올린다.
- PR 본문의 프리뷰 링크 칸을 채운다. `https://htmlpreview.github.io/?https://github.com/NAR-GG/warding-docs/blob/<브랜치>/<경로>` 형식이다.
- 새 기능을 추가하면 `README.md`의 목록 표에 한 줄을 넣는다.
