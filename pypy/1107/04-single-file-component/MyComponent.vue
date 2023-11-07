<!-- 
    Vue SFC(single file conponent)는 HTML, CSS 및 JS 3개를 하나로 합친 것 
 -->
 <!-- 
    순서
    vbase-3-setup   
    lang="scss" 지우기
    template, script, style 작성

    
    npm init vue@latest
    cd vue-project , vue-project로 이동
    npm install
-->
<!-- 
    NPM(Node Package Manager): Node.js의 기본 패키지 관리자
    (파이썬의 pip같은 것)
 -->
 <!-- JS는 브라우저에서만 쓸 수 있었는데 밖(서버)에서도 쓸 수 있게 만드는 Node.js -->

<!-- 
    node_module : 외부 패키지가 저장되는 디렉토리, 프로젝트의 의존성 모듈이 저장되는 공간, .gitignore에 작성됨 
    package-lock.json : 패키지 설치에 필요한 정보(django의 requirements같은 것), npm install 명령을 통해 패키지를 설치할 때 필요
    package.json : package-lock.json과 함께 프로젝트의 의존성을 관리, 버전충돌 방지 및 일관성을 유지
    public: 소스코드에서 참조되지 않는, 항상 같은 이름을 갖는, import 할 필요가 없는, 항상 root 절대경로 참조
    src : 프로젝트 주요 소스 코드를 포함하는 곳
        - asset : 프로젝트 내에서 사용되는 자원(이미지,폰트,스타일시트 등), component 자체에서 참조하는 내부파일 저장
        - components : component를 작성하는 곳
        - App : Root 컴포넌트, 최종결과물
        - main : VUe인스턴스를 생성
        - index : VUe앱의 기본 HTML, entry point,
                  app.vue가 해당 페이지에 mount됨. bootstrap 사용 가능
-->

<!-- 
    Module: 프로그램을 구성하는 독립적인 코드 블록(*.js 파일)
    애플리케이션이 크고 복잡해지면서 나눴음
    나누니까 모듈수가 많아지고 의존성이 높아짐
    의존성이 높아지니 문제가 발생하면 원인 파악이 어려워짐
    이를 해결하기 위해 Bundler 만들었음

    Bundler: 모듈과 파일을 묶어 최적화, 개발자가 신경안써도 되게끔 되어있음

 -->

 <!-- 
    컴포넌트 사용 절차
    1. 컴포넌트 파일 생성
    2. 컴포넌트 등록import 
  -->

<!-- 
    싱글파일컴포넌트 파일명은 항상 파스칼케이스거나 항상 케밥케이스여야한다.
    기본 컴포넌트 Base, App, V 같은 접두사로 알아먹을 수 있게
    한번만 쓸 것은 The 붙이고
    자식컴포넌트는 부모컴포넌트의 이름을 접두사로 포함해야 한다.
    약어지양

 -->

 <!--
     Virtual DOM 
    가상의 DOM 메모리에 저장하고 변경된 부분만 DOM에 저장하는 기법
    DOM 조작 최소화로 성능향상
    자동 변화 감지
    실제 DOM조작은 Vue에게 맡김


    js에서 사용하는 DOM접근 메서드 사용 X 
    querySelector, createElement, addEventListenr 등 
    접근은 Vue의 ref나 LifecycleHook 사용
    ref= "something" ,  const something = ref()
    -->


<!-- 
    자식의 최상위 요소는 부모와 본인의 CSS 모두의 영향을 받음

    최상위 HTML 요소는 하나만 작성되는 것을 권장 

-->


 <!-- 템플릿은 하나의 vue파일에 한번만 등장한다. -->
 <template>
    <div class = "greeting">{{ msg  }} </div>
 </template>
 
 <!-- 이전 setup함수에서 작성했던 내용을 이제는 바로 작성 
다소 문법 바뀜, return, mount 사라짐-->
 <script setup>
 import { ref } from 'vue'

 const msg = ref('hello world')

 </script>
 

 <!-- scoped는 이 영역에서만 적용된다라는 뜻 
독립적인 개발 가능-->
 <style scoped>
 .greeting {
    color : crimson;
 }
 </style>