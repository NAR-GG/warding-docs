# warding-docs

Warding 앱의 기획과 디자인 초안을 두는 곳이다. 계정이 달라도 모두 같은 파일을 보고, 각자의 Claude도 같은 규칙을 읽게 하려고 만들었다.

- 앱 코드: [warding-mobile-repo](https://github.com/NAR-GG/warding-mobile-repo)
- 백엔드: [nar-back-repo](https://github.com/NAR-GG/nar-back-repo)

## 규칙

1. **기획은 md, 디자인은 html로 만든다.** 결정과 미결은 md에 쓰고, html에는 화면만 그린다. 스크린샷은 빠르게 확인할 때만 쓴다.
2. **확정본은 이 레포에만 있다.** PR을 올리고 리뷰어가 승인해서 `main`에 머지되면 확정이다. 슬랙이나 개인 artifact에 있는 버전은 초안으로 본다.
3. **기능마다 작성자와 리뷰어를 정한다.** spec 맨 위 표에 적는다.
4. **공개 레포다.** 실유저 닉네임, `memberId`, 유저가 올린 이미지, 글 본문은 넣지 않고 예시 데이터로 바꾼다. 경기·순위·선수처럼 원래 공개된 정보는 prod 값을 그대로 써도 된다.
5. **색은 [assets/tokens.css](assets/tokens.css)만 쓴다.** 이 파일은 앱의 `AppColors`에서 자동으로 만들어진다. 목업에서 hex를 직접 쓰지 않는다.

## 폴더

```
policy/            기능을 가로지르는 정책 (디자인 규칙 등)
features/<slug>/   기능 하나 = spec.md + mockup.html
templates/spec.md  새 기능 spec 템플릿
assets/tokens.css  앱 색 토큰 (scripts/sync-tokens.py 가 생성)
```

## 어디에 두나

| 무엇 | 어디 |
|---|---|
| 기능 하나의 기획·결정·미결 | `features/<slug>/spec.md` |
| 기능 하나의 화면 | `features/<slug>/mockup.html` |
| 여러 기능에 걸친 정책 | `policy/<주제>.md`. 없으면 그때 새로 만든다(예: `community.md`, `notification.md`) |
| 디자인 규칙(색 쓰는 법, 폰트, 표시 관례) | `policy/design.md` |
| 색 값 자체 | 앱 `AppColors`(모바일 레포 PR) → `sync-tokens.py`로 `tokens.css` 갱신 |
| Figma 시안과 코멘트 | Figma에 둔다. 거기서 정해진 것은 spec이나 policy로 옮겨 적는다 |
| 이미 있는 API | 모바일 레포 `docs/api-reference.md`(자동 생성)를 보고 spec에 링크한다 |
| 약관·개인정보처리방침 | 모바일 레포 `docs/policies/`. 앱이 링크하는 법적 문서라 옮기지 않는다 |
| 지금 코드가 어떻게 동작하는지 | 모바일 레포 `wiki/` |

- **spec인지 policy인지**: 결정이 한 기능 안에서만 쓰이면 spec에 둔다. 두 번째 기능에서도 쓰이게 되면 policy로 옮기고, spec에는 링크만 남긴다.
- **결정이 바뀌면**: 그 줄을 고치고 날짜를 새로 쓴다. 이전 결정은 git 기록에 남는다. 뒤집은 이유가 중요하면 "(이전: …)"을 붙인다.
- **슬랙·Figma·개인 위키에서 정한 것**은 여기 PR로 올라와야 확정이다.

## 보는 법

- **main**: https://nar-gg.github.io/warding-docs/ (md도 페이지로 렌더된다)
- **PR 브랜치**: `https://raw.githack.com/NAR-GG/warding-docs/<브랜치>/features/<slug>/mockup.html`
  PR 본문 템플릿에 이 링크를 넣는 칸이 있다.

## 새 기능 시작하기

1. `main`에서 브랜치를 딴다(`feat/<slug>`).
2. `templates/spec.md`를 `features/<slug>/spec.md`로 복사해서 채운다.
3. 목업은 `features/<slug>/mockup.html`에 둔다. 규칙은 [CLAUDE.md](CLAUDE.md)의 "목업" 절을 따른다.
4. PR을 올리고 프리뷰 링크를 붙인다. 피드백은 PR 코멘트로 남긴다.

## 앱 색이 바뀌면

```bash
python3 scripts/sync-tokens.py
```

## 목록

| 기능 | 상태 |
|---|---|
