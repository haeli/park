# Hae-Li Park 홈페이지

Sphinx + PyData Sphinx Theme으로 만든 개인 홈페이지입니다.
내용은 모두 Markdown 파일이라 메모장이나 Obsidian에서 바로 고칠 수 있습니다.

## 파일 구성

| 파일 | 내용 |
|---|---|
| `index.md` | 첫 화면 (소개, 연구 관심사, 연락처) |
| `research.md` | 연구 주제 |
| `publications.md` | 논문, 학위논문, 학회 발표 |
| `cv.md` | 이력 |
| `conf.py` | 사이트 설정 (제목, 메뉴, 프로필 링크) |
| `_static/custom.css` | 글꼴 크기, 간격 등 모양 조정 |
| `.github/workflows/deploy.yml` | GitHub에 올리면 자동으로 사이트를 만들어 주는 설정 |

## GitHub Pages에 올리기

1. GitHub에서 새 저장소를 만듭니다. 이름을 `아이디.github.io`로 하면
   주소가 `https://아이디.github.io`가 됩니다.
2. 이 폴더의 파일을 전부 그 저장소에 올립니다 (`.github` 폴더 포함).
3. 저장소의 Settings → Pages → Source를 **GitHub Actions**로 바꿉니다.
4. 1~2분 뒤 사이트가 열립니다. 이후에는 파일을 고쳐 올릴 때마다 자동으로 갱신됩니다.

## 내 컴퓨터에서 미리 보기

```bash
pip install -r requirements.txt
sphinx-build -b html . _build/html
```

`_build/html/index.html`을 브라우저로 열면 됩니다.

## 자주 하는 수정

- **논문 추가**: `publications.md`에 같은 형식으로 한 줄을 더 씁니다.
- **메뉴 추가**: 새 `.md` 파일을 만들고 `index.md` 맨 아래 `toctree` 목록에 파일 이름을 추가합니다.
- **사진 넣기**: 사진을 `_static/`에 넣고 `index.md`에 `![Hae-Li Park](_static/photo.jpg){width=220px}`를 씁니다.
- **Google Scholar, ORCID, GitHub 아이콘**: `conf.py`의 `icon_links` 부분 주석을 풀고 주소를 넣습니다.
