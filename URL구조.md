| **엔티티**             | **HTTP 메서드** | **URL**                                      | **설명**                           |
|------------------------|-----------------|----------------------------------------------|------------------------------------|
| **USER**               | GET             | /users                                       | 모든 사용자 목록 가져오기            |
|                        | POST            | /users                                       | 새로운 사용자 생성                   |
|                        | GET             | /users/{id}                                  | 특정 사용자 정보 가져오기              |
|                        | PUT             | /users/{id}                                  | 특정 사용자 정보 업데이트              |
|                        | DELETE          | /users/{id}                                  | 특정 사용자 삭제                     |
| **POST**               | GET             | /posts                                       | 모든 게시물 목록 가져오기             |
|                        | POST            | /posts                                       | 새로운 게시물 생성                    |
|                        | GET             | /posts/{id}                                  | 특정 게시물 가져오기                  |
|                        | PUT             | /posts/{id}                                  | 특정 게시물 업데이트                  |
|                        | DELETE          | /posts/{id}                                  | 특정 게시물 삭제                     |
|                        | GET             | /posts/{id}/comments                         | 특정 게시물의 댓글 목록 가져오기        |
|                        | POST            | /posts/{id}/comments                         | 특정 게시물에 댓글 작성                |
|                        | GET             | /posts/{id}/reactions                        | 특정 게시물의 반응 목록 가져오기        |
|                        | POST            | /posts/{id}/reactions                        | 특정 게시물에 반응 추가                |
| **COMMENT**            | GET             | /comments/{id}                               | 특정 댓글 가져오기                    |
|                        | PUT             | /comments/{id}                               | 특정 댓글 업데이트                    |
|                        | DELETE          | /comments/{id}                               | 특정 댓글 삭제                       |
| **VERIFICATIONREQUEST**| GET             | /verification-requests                       | 모든 검증 요청 목록 가져오기            |
|                        | POST            | /verification-requests                       | 새로운 검증 요청 생성                  |
|                        | GET             | /verification-requests/{id}                  | 특정 검증 요청 가져오기                |
|                        | PUT             | /verification-requests/{id}                  | 특정 검증 요청 상태 업데이트            |
|                        | DELETE          | /verification-requests/{id}                  | 특정 검증 요청 삭제                   |
| **REACTION**           | GET             | /reactions                                   | 모든 반응 목록 가져오기               |
|                        | POST            | /reactions                                   | 새로운 반응 추가                      |
|                        | GET             | /reactions/{id}                              | 특정 반응 가져오기                    |
|                        | DELETE          | /reactions/{id}                              | 특정 반응 삭제                       |
| **DIRECTMESSAGE**      | GET             | /direct-messages                             | 모든 쪽지 목록 가져오기 (필터링 가능)     |
|                        | POST            | /direct-messages                             | 새로운 쪽지 보내기                    |
|                        | GET             | /direct-messages/{id}                        | 특정 쪽지 가져오기                    |
|                        | PUT             | /direct-messages/{id}                        | 특정 쪽지 읽음 상태 업데이트            |
| **REPORT**             | GET             | /reports                                     | 모든 신고 목록 가져오기               |
|                        | POST            | /reports                                     | 새로운 신고 생성                      |
|                        | GET             | /reports/{id}                                | 특정 신고 가져오기                    |
|                        | DELETE          | /reports/{id}                                | 특정 신고 삭제                       |
| **POSTEDITHISTORY**    | GET             | /post-edit-history                           | 모든 게시물 수정 기록 가져오기          |
|                        | POST            | /post-edit-history                           | 새로운 게시물 수정 기록 추가            |
|                        | GET             | /post-edit-history/{id}                      | 특정 게시물 수정 기록 가져오기          |
| **CATEGORY**           | GET             | /categories                                  | 모든 카테고리 목록 가져오기             |
|                        | POST            | /categories                                  | 새로운 카테고리 생성                   |
|                        | GET             | /categories/{id}                             | 특정 카테고리 가져오기                 |
|                        | PUT             | /categories/{id}                             | 특정 카테고리 업데이트                 |
|                        | DELETE          | /categories/{id}                             | 특정 카테고리 삭제                    |
| **TAG**                | GET             | /tags                                        | 모든 태그 목록 가져오기                |
|                        | POST            | /tags                                        | 새로운 태그 생성                      |
|                        | GET             | /tags/{id}                                   | 특정 태그 가져오기                    |
|                        | PUT             | /tags/{id}                                   | 특정 태그 업데이트                    |
|                        | DELETE          | /tags/{id}                                   | 특정 태그 삭제                       |
| **POST_TAG**           | POST            | /posts/{post_id}/tags/{tag_id}               | 특정 게시물에 특정 태그 추가             |
|                        | DELETE          | /posts/{post_id}/tags/{tag_id}               | 특정 게시물에서 특정 태그 제거            |
