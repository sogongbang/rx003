.. _appendix_001_how_to_edit_the_doc:


RX003 홈 개발 방법
****************************************************************

ubiworks 도구 설치
===========================================================
    * https://ubinos.org --> Getting Started Guide --> 윈도우에 개발 환경 설정하기 참조

ubiworks 소스트리 받아오기
===========================================================
    * https://ubinos.org --> Getting Started Guide 참조

Sphinx 도구 설치
===========================================================
    https://github.com/sogongbang/sphinx_doc_materials --> README 참조

RX003 홈페이지 개발을 위한 ubinos 라이브러리 받아오기
===========================================================

    * ubiworks/make/liblist.json의 내용을 다음으로 대체

        .. code-block:: json

            [
                {
                    "name": "sphinx_doc_materials",
                    "url": "git@github.com:sogongbang/sphinx_doc_materials.git",
                    "branch_tag_commit": {"type": "branch", "name": "ubinos-main"},
                    "description": ""
                },
                {
                    "name": "rx003",
                    "url": "git@github.com:sogongbang/rx003.git",
                    "branch_tag_commit": {"type": "branch", "name": "ubinos-main"},
                    "description": ""
                }
            ]

    * 다음 과정을 수행해 라이브러리 받아오기

        * VSCode --> Menu --> Terminal --> Run build Task... --> make xmgr
            * Check "Hide ubinos default library list"
            * Check "rx003", "sphinx_doc_materials"
            * Press "Install"

RX003 홈를 로컬에서 build 및 확인
===========================================================

    * VSCode --> Menu --> Terminal --> Run build Task... --> make xsel
        * Select rx003_home_html
        * Press "Select"

    * VSCode --> Menu --> Terminal --> Run build Task... --> make rebuildd

    * VSCode --> Menu --> Terminal --> Run build Task... --> make xrun


