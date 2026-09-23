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
| [홈 화면 개편](features/home/spec.md) · [목업](features/home/mockup.html) | 초안 |
