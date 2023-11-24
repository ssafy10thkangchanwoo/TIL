

어제자 오류에 대해 강사님께 피드백을 받았다.
 App.vue에서는 RouterLink 경로에 id값이 없이 작성하였다.
 <RouterLink :to="{ name: 'BoardDetailView' }">BoardDetail</RouterLink>

 게시글목록페이지에서는 id값을 포함하여 작성하였다.
<RouterLink :to="{ name: 'BoardDetailView', params: { id: article.id } }"></RouterLink>

그래서 router/index의 경로상에 :id를 추가하면 전체 페이지가 먹통이 된 것이었다.
생각해보면 일부 페이지가 아니라 전체페이지가 작동하지 않는 것에 대하여 App에 원인이 있음을 충분히 유추할 수 있기에
다음에 같은 오류가 발생했을 시 신속한 원인파악이 가능할 것으로 보인다.


이후 게시판 detail을 확인할 때
옵셔널체이닝을 사용하지 않으면 or v-if=article을 사용하지 않으면 에러가 발생하는 현상이 발생했다.
위의 방법으로 작동에는 문제가 없으나
그러나 article은 분명히 들어와있고 출력도 잘 되어 근본적인 원인 파악이 필요하다.


게시글 수정같은 경우 장고서버에 get요청을 하여 기존 게시글을 불러온 이후 수정 후 수정버튼을 누르면
서버에 put요청을 하게끔 작성하였다. 그러나 수정된 내용이 반영되지 않아 디버깅 중이다.
