(this["webpackJsonpfrontend-bry"]=this["webpackJsonpfrontend-bry"]||[]).push([[0],{25:function(e,t,n){},26:function(e,t,n){},27:function(e,t,n){},40:function(e,t,n){"use strict";n.r(t);var a=n(0),s=n.n(a),c=n(7),o=n.n(c),i=n(15),r=n(16),l=n(17),h=n(20),d=n(19),j=n.p+"static/media/cookie.eab6f1eb.png",b=n.p+"static/media/grandmaskitchen.608174d2.jpg",k=(n(25),n(26),n(27),function(e,t,n){var a=new Date;a.setTime(a.getTime()+24*n*60*60*1e3);var s="expires="+a.toUTCString();document.cookie=e+"="+t+";"+s+";path=/"}),m=n(42),f=n(43),p=n(18),g=n.n(p),u=n(1),x={content:{top:"50%",left:"50%",right:"auto",bottom:"auto",marginRight:"-50%",transform:"translate(-50%, -50%)"}},O=function(e){Object(h.a)(n,e);var t=Object(d.a)(n);function n(e){var a;return Object(r.a)(this,n),(a=t.call(this,e)).CookieConsent=function(){a.setState({showCookieAccept:!1})},a.ManageCookies=function(){a.setState({modalIsOpen:!0})},a.closeModal=function(){a.setState({modalIsOpen:!1})},a.afterOpenModal=function(){},a.setCookieState=function(e){var t=e.target.nextSibling.innerHTML;a.setState(Object(i.a)({},t,(0==a.state[t]||1==a.state[t])&&!a.state[t]))},a.CookieApply=function(e){for(var t=0;t<e.children.length;t++){var n=e.children[t].children[0].checked,s=e.children[t].children[1].innerHTML;"Flag"!=s&&n?k(s,"JA",400):n&&fetch("/cookieconsent",{method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json"},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({Flag:!0})}).then((function(e){return e.json()})).then((function(e){k("Flag",e.Flag)}))}console.log({}),a.closeModal()},a.state={showCookieAccept:!0,modalIsOpen:!1,PST:!0,NSA:!0,FSB:!0,Kripos:!0},a.FormGroup=s.a.createRef(),a}return Object(l.a)(n,[{key:"render",value:function(){var e=this;console.log("I am rendering");var t=this.state,n=t.showCookieAccept,a=t.modalIsOpen;return Object(u.jsxs)("div",{className:"text-center",children:[Object(u.jsx)("div",{className:"bg-image",style:{backgroundImage:"url(".concat(b,")")},children:Object(u.jsx)("img",{src:j,className:"falling-cookie",alt:"cookie"})}),Object(u.jsxs)("div",{className:"cover-container d-flex h-100 p-3 mx-auto flex-column",children:[Object(u.jsx)("header",{className:"masthead mb-auto",children:Object(u.jsxs)("div",{className:"inner",children:[Object(u.jsx)("h3",{className:"masthead-brand",children:"\ud83c\udf6a"}),Object(u.jsxs)("nav",{className:"nav nav-masthead justify-content-center",children:[Object(u.jsx)("a",{className:"nav-link active",href:"#",children:"Hjem"}),Object(u.jsx)("a",{className:"nav-link",href:"#",children:"Kjeksutvalg"}),Object(u.jsx)("a",{className:"nav-link",href:"#",children:"Kontakt"})]})]})}),Object(u.jsxs)("main",{style:{zIndex:1},role:"main",className:"inner cover",children:[Object(u.jsx)("h1",{className:"cover-heading",children:"Bestemor Berthas Hjemmebakte"}),Object(u.jsx)("p",{className:"lead",children:"K\xe5ret til norges beste kjeks"}),Object(u.jsx)("p",{className:"lead",children:Object(u.jsx)("a",{href:"#",className:"btn btn-lg btn-secondary",children:"Bestill kjeks"})})]}),Object(u.jsx)("footer",{style:{zIndex:1},className:"mastfoot mt-auto",children:Object(u.jsx)("div",{className:"inner",children:Object(u.jsxs)("p",{children:["Oppgaven er en del av \xe5rets ",Object(u.jsx)("a",{href:"http://helsectf.no/",children:"HelseCTF"}),", utviklet av ",Object(u.jsx)("a",{href:"https://www.nhn.no/helsecert/",children:"HelseCERT"}),"."]})})})]}),n?Object(u.jsxs)("div",{className:"alert show text-center cookiealert",role:"alert",children:[Object(u.jsx)("b",{children:"Denne siden bruker informasjonskapsler."})," Trykk ",Object(u.jsx)("span",{style:{textDecoration:"underline",cursor:"pointer"},onClick:this.ManageCookies,children:"her"})," for \xe5 lese mer.",Object(u.jsx)("button",{onClick:this.CookieConsent,type:"button",className:"btn btn-primary btn-sm acceptcookies",children:"Godta"})]}):null,Object(u.jsxs)(g.a,{isOpen:a,onAfterOpen:this.afterOpenModal,onRequestClose:this.closeModal,style:x,contentLabel:"Example Modal",children:[Object(u.jsx)("div",{class:"ModalContent",children:Object(u.jsxs)(m.a,{children:[Object(u.jsxs)("div",{className:"cookies",children:[Object(u.jsx)("img",{src:j}),Object(u.jsx)("h2",{children:"Cookies"})]}),Object(u.jsx)("p",{children:"N\xf8dvendige informasjonskapsler hjelper med \xe5 gj\xf8re en hjemmeside brukbar ved \xe5 aktivere grunnleggende funksjoner, slik som side-navigasjon og tilgang til sikre omr\xe5der av hjemmesiden. Hjemmesiden kan ikke fungere optimalt uten disse informasjonskapslene."}),Object(u.jsxs)(m.a.Group,{ref:"FormGroup",controlId:"formBasicCheckbox",children:[Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,disabled:!0,checked:this.state.PST,ref:"c1",type:"checkbox",label:"Fredrik Kanelbakken"}),Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,disabled:!0,checked:this.state.Kripos,ref:"c2",type:"checkbox",label:"Lise Bake Pulver"}),Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,ref:"c3",type:"checkbox",label:"Marthe Mel von Hvete"}),Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,checked:!0,ref:"c4",type:"checkbox",label:"Magnus Sukkerberg"}),Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,disabled:!0,checked:this.state.NSA,ref:"c5",type:"checkbox",label:"Lars Lakris A.Stang"}),Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,disabled:!0,checked:this.state.FSB,ref:"c6",type:"checkbox",label:"Fara M. argarin"}),Object(u.jsx)(m.a.Check,{onChange:this.setCookieState,ref:"c7",className:"flag",type:"checkbox",label:"Flag"})]})]})}),Object(u.jsx)(f.a,{className:"smol",onClick:function(){return e.CookieApply(o.a.findDOMNode(e.refs.FormGroup))},variant:"primary",type:"submit",children:"Ok"})]})]})}}]),n}(a.Component),C=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,44)).then((function(t){var n=t.getCLS,a=t.getFID,s=t.getFCP,c=t.getLCP,o=t.getTTFB;n(e),a(e),s(e),c(e),o(e)}))};o.a.render(Object(u.jsx)(s.a.StrictMode,{children:Object(u.jsx)(O,{})}),document.getElementById("root")),C()}},[[40,1,2]]]);