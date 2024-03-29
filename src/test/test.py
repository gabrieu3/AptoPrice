# coding: iso-8859-1 -*-
import re
import json
from src.scrap.ApOlx import ApOlx
from src.dco.ApDcoOlx import ApDco
from src.dto.ApDto import ApDto
import time
from bs4 import BeautifulSoup



html = r"""
<html lang="pt-BR" data-reactroot="">
   <head>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <meta charSet="UTF-8"/>
      <link rel="canonical" href="https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamento-a-venda-com-3-dormitorios-em-anita-garibaldi-joinville-cod-299-674853647"/>
      <link rel="alternate" href="olxapp://adpage/?id=674853647"/>
      <meta property="og:title" content="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299"/>
      <meta property="og:site_name" content="OLX"/>
      <meta property="og:url" content="https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamento-a-venda-com-3-dormitorios-em-anita-garibaldi-joinville-cod-299-674853647"/>
      <meta property="og:description" content="C�digo do an�ncio: 299&lt;br&gt;Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos cobertura s�o semelhantes aos aptos tipo, por�m com terra�o privativo. Aproveite e marque sua visita. ** As fotos s�o do apartamento decorado. **"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/222922100060064.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/227922102675525.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/221922101745033.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/223922108582249.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/226922106432034.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/228922109722163.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/222922105111569.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/222922107287253.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/225922100681526.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/229922104698395.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/228922105966788.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/223922102338758.jpg"/>
      <meta property="og:image" content="https://img.olx.com.br/images/22/229922103193977.jpg"/>
      <meta property="og:type" content="website"/>
      <meta property="og:locale" content="pt_BR"/>
      <meta property="al:ios:app_name" content="OLX"/>
      <meta property="al:ios:app_store_id" content="692808319"/>
      <meta property="al:ios:url" content="olxapp://adpage/&amp;id=674853647"/>
      <meta property="fb:app_id" content="106401512762894"/>
      <meta name="description" content="C�digo do an�ncio: 299 Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos..."/>
      <meta name="keywords" content="Apartamento,�,venda,com,3,dormit�rios,em,Anita,garibaldi,,Joinville,cod:299"/>
      <meta name="twitter:app:name:ipad" content="OLX"/>
      <meta name="twitter:app:id:ipad" content="692808319"/>
      <meta name="twitter:app:url:ipad" content="olxapp://adpage/&amp;id=674853647"/>
      <meta name="twitter:app:name:iphone" content="OLX"/>
      <meta name="twitter:app:id:iphone" content="692808319"/>
      <meta name="twitter:app:url:iphone" content="olxapp://adpage/&amp;id=674853647"/>
      <meta name="twitter:url" content="https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamento-a-venda-com-3-dormitorios-em-anita-garibaldi-joinville-cod-299-674853647"/>
      <meta name="twitter:card" content="summary_large_image"/>
      <meta name="twitter:site" content="@OLX_Brasil"/>
      <meta name="twitter:creator" content="@OLX_Brasil"/>
      <meta name="twitter:title" content="Apartamento 3 quartos � venda com Academia - Anita Garibaldi, Joinville - SC 674853647 | OLX"/>
      <meta name="twitter:description" content="C�digo do an�ncio: 299&lt;br&gt;Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos cobertura s�o semelhantes aos aptos tipo, por�m com terra�o privativo. Aproveite e marque sua visita. ** As fotos s�o do apartamento decorado. **"/>
      <meta name="twitter:image" content="https://img.olx.com.br/images/22/222922100060064.jpg"/>
      <link rel="apple-touch-icon" sizes="180x180" href="https://static.olx.com.br/cd/vi/images/icons/apple-touch-icon.png"/>
      <link rel="icon" type="image/png" sizes="32x32" href="https://static.olx.com.br/cd/vi/images/icons/favicon-32x32.png"/>
      <link rel="icon" type="image/png" sizes="192x192" href="https://static.olx.com.br/cd/vi/images/icons/android-chrome-192x192.png"/>
      <link rel="icon" type="image/png" sizes="16x16" href="https://static.olx.com.br/cd/vi/images/icons/favicon-16x16.png"/>
      <link rel="manifest" href="https://static.olx.com.br/cd/vi/images/icons/site.webmanifest"/>
      <link rel="mask-icon" href="https://static.olx.com.br/cd/vi/images/icons/safari-pinned-tab.svg" color="#6e0ad6"/>
      <title>Apartamento 3 quartos � venda com Academia - Anita Garibaldi, Joinville - SC 674853647 | OLX</title>
      <link href="https://static.olx.com.br/upr/umd/mercurie-widget.js" rel="preload" as="script"/>
      <script src="https://www.googletagservices.com/tag/js/gpt.js" type="text/javascript" async=""></script><script>window.googletag = window.googletag || {cmd: []};</script><script src="https://static.bn-static.com/js/prebid.min.js" type="text/javascript" async=""></script><script>
         var pbjs = pbjs || {};
         pbjs.que = pbjs.que || [];
      </script><script src="https://www.google.com/adsense/search/ads.js" type="text/javascript" async=""></script><script charSet="utf-8">(function(g,o){g[o]=g[o]||function(){(g[o]['q']=g[o]['q']||[]).push(
         arguments)},g[o]['t']=1*new Date})(window,'_googCsa');
      </script><script>
         (function(G,o,O,g,L,e){G[g]=G[g]||function(){(G[g]['q']=G[g]['q']||[]).push(
         arguments)},G[g]['t']=1*new
         Date;L=o.createElement(O),e=o.getElementsByTagName(
         O)[0];L.async=1;L.src='//www.google.com/adsense/search/async-ads.js';
         e.parentNode.insertBefore(L,e)})(window,document,'script','_googCsa');
      </script>
      <meta pubid="4235f368-83e5-47e4-8bd4-9a3cf36c0000"/>
      <script>window.dataLayer = [{"page":{"pageType":"ad_detail","detail":{"adDate":1583601579,"state_id":"47","list_id":674853647,"parent_category_id":1000,"category_id":1020,"city_id":2471,"zipcode":"89203307","price":"625697"},"adDetail":{"listId":674853647,"sellerName":"GW Junior Imobiliária","adDate":"1970-01-19 04:53:21","price":"625697","mainCategory":"Im�veis","subCategory":"Apartamentos","mainCategoryID":1000,"subCategoryID":1001,"state":"SC","ddd":"47","brand":null,"model":null,"version":null,"gearbox":null,"region":"Norte de Santa Catarina","category":"Apartamentos","real_estate_type":"Venda - apartamento padr�o","size":184,"rooms":"3","bathrooms":"2","garage_spaces":"2","apartment_features":"Academia"}},"pictures":13,"session":{"user":{"loginType":null,"userID":null}},"pageType":"ad_detail","abtestingEnable":"1","listId":674853647,"state":"SC","region":"Joinville","category":"Apartamentos","site":{"isMobile":false,"source":"web"}}]</script><script>function buildPerformanceDatalayer(){var e=window.dataLayer[0];e.page.detail.memoryStatus={},window&&window.navigator&&(e.page.detail.cpuCores=window.navigator.hardwareConcurrency,window.navigator.connection&&(e.page.detail.connectionType=window.navigator.connection.effectiveType,e.page.detail.downloadLink=window.navigator.connection.downlink,e.page.detail.saveData=window.navigator.connection.saveData),window.navigator.deviceMemory&&(e.page.detail.memoryStatus.deviceMemory=window.navigator.deviceMemory)),window&&window.performance&&window.performance.memory&&(e.page.detail.memoryStatus.totalJSHeapSize=window.performance.memory.totalJSHeapSize,e.page.detail.memoryStatus.usedJSHeapSize=window.performance.memory.usedJSHeapSize,e.page.detail.memoryStatus.jsHeapSizeLimit=window.performance.memory.jsHeapSizeLimit)}buildPerformanceDatalayer();</script><script>window.dfpPageSegmentationDataLayer = [{"ABTest":["advAfshNativo_A","ast-showphone-flow_new","autos-native-vas_a","bj-HelpMeDecide_SellerOnlineTitle","bj-listItemOpenInANewTab_A","fixedBar2_box","mfg-autos-market-place-selected-options_early","mfg-autos-market-place_financing-insurance","payments-boletoProgressButton_A","upr-chat-adview-profilelink_A","upr-chat-listing-profilelink_A"],"uf":"SC","ddd":"47","bairro":"joinville","zona":"regiao-de-joinville-e-norte-do-estado-47","plataforma":"desktop","searchCategoryLevelZero":1000,"searchCategoryLevelOne":1001,"imoveis_preco":"500000-650000","dfp_vas_list_id":674853647,"dfp_vas_user_type":"1","dfp_vas_transaction_id":"4235f368-83e5-47e4-8bd4-9a3cf36c0000","dfp_vas_car_price":"625697","km_carro":"500000-mais","imoveis_area":"180-200","imoveis_quartos":"3","imoveis_tipo":"apartamentos"}]</script><script>
         (function(h,o,t,j,a,r){
           h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
           h._hjSettings={hjid:736533,hjsv:6};
           a=o.getElementsByTagName('head')[0];
           r=o.createElement('script');r.async=1;
           r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
           a.appendChild(r);
         })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
      </script><script>
         var _comscore = _comscore || [];
         _comscore.push({ c1: "2", c2: "29823456" });
         (function() {
           var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
           s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
           el.parentNode.insertBefore(s, el);
         })();      
      </script>
      <noscript><img src="https://sb.scorecardresearch.com/p?c1=2&amp;c2=29823456&amp;cv=2.0&amp;cj=1"/></noscript>
      <noscript>
         <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WGKTT96"
            height="0" width="0" style="display:none;visibility:hidden"></iframe>
      </noscript>
      <script>
         (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
         new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
         j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
         'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
         })(window,document,'script','dataLayer','GTM-WGKTT96');
      </script><script type="text/javascript" src="https://static.olx.com.br/olx/js/lurker.min.js" async=""></script><script src="https://tags.t.tailtarget.com/t3m.js?i=TT-12113-4/CT-886" type="text/javascript" async=""></script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BuyAction","identifier":674853647,"Object":{"@type":"Product","name":"Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299","url":"https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamento-a-venda-com-3-dormitorios-em-anita-garibaldi-joinville-cod-299-674853647","description":"C�digo do an�ncio: 299<br />Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos cobertura s�o semelhantes aos aptos tipo, por�m com terra�o privativo. Aproveite e marque sua visita. ** As fotos s�o do apartamento decorado. **","image":[{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/222922100060064.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/227922102675525.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/221922101745033.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/223922108582249.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/226922106432034.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/228922109722163.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/222922105111569.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/222922107287253.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/225922100681526.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/229922104698395.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/228922105966788.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/223922102338758.jpg"},{"@type":"ImageObject","contentUrl":"https://img.olx.com.br/images/22/229922103193977.jpg"}]},"location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Joinville","addressRegion":"SC","postalCode":"89203307","addressCountry":{"@type":"Country","name":"BR"}}},"priceSpecification":{"@type":"PriceSpecification","priceCurrency":"BRL","price":"625697"},"seller":{"@type":"Person","name":"GW Junior Imobiliária","image":"https://static.olx.com.br/img/no-logo.png"}}</script>
      <style>
         body{
         margin:0;
         text-rendering: geometricPrecision;
         font-family: "Nunito Sans", Arial, Helvetica;
         }
      </style>
      <style data-styled="lcmwPG hRMdWm JXwqS dHRfoT eTwHTY ffdXNo hwognJ jLlbDB bBsenL kIdmZJ briYLB bDzfpu cVNHmY fwIYkU kkjbBk fknPRF ckqtGX jFvQLW kAnOVp jyDaIy gvtffP cBfPri dlWajz jAHFXn cpscHx jyICCp hqKhkd jGvFuF bdQAUC hoRgXC clkGwd gQqMLR ldSSMo hMMGVW jTuobL dXtwXY eenYUc jisuAT bBLtXw cvARbW gNWLDC bEzVbN hWribP heHIon dMoaFE eeNNeS bgSgXX gUqBBc ccSbwB sQyxD eOOllE dUIuRn fZasOH jismrm fXjlVF jKijTl kUmnbD dykXjo bEpZdo fheUFo ghVswA coQACr jvlWsz RdUib bkznnI EAZJj jHoWDW eKHEXW iQypEC kwBdnA enqtXF bZsaea hMcgWM Xfofp fhqRDx kXGTwk ebUpuZ gnyoQn jhVsdW zSAIq bQbWAr hKSfQK lhgKeG dSuMqe kCQFBe hEwMYq iGQsBq gYqcOg TQjCg evwHUf inOGdV krfoAB fDJoux dxiZkQ GtSha gBLONq csYflq iRwHp iLUrMT gabobT bgLcPW jpiGgk dEdfLF bejHmG dHfQOM lkynZT fwXkTr eEEnMS dSADzT xrRab bRVClF gbvMQR izJNjp cEdBUU kZFASz ZAYGT jEmYhm jZKdyj cARDRF hrzRZZ dGzfoF eowFbc jZAxAJ kzqvPB dmyynv irIYwp hTWoyD cvXZub iOixbk jjsysS hpIrNh jvSHiQ bJcANz kcotea htYGeZ dSAaHC gQFNBI dxMPwC fZlUwt cPAPOU elhoyw eSLnCp hAhJaI XtcoW fcSnOq bPLuuE cGChIZ  cmiwUT hABWtd fVNWXx jTVLFf bRWdWv jhxuI dYSSwe eMGorO hHjKok kYeoZc fCtGMR  gJgiaD zvmsw ehNyVo bRswCL bgNpyx ijPgvg fWCKgV bsaFM iwOlty dPJyDS dBeEuJ eOxKth caJVsD koPHXB gOodOV grPiYk byaNVW cvsAxh" data-styled-version="4.2.0">
         /* sc-component-id: h3us20-2 */
         .jGvFuF{display:none;} @media (min-width:45em){.jGvFuF{display:block;}}.bdQAUC{display:none;} @media (min-width:52.5em){.bdQAUC{display:block;}}
         /* sc-component-id: h3us20-3 */
         .csYflq{display:block;} @media (min-width:52.5em){.csYflq{display:none;}}.iRwHp{display:block;} @media (min-width:45em){.iRwHp{display:none;}}
         /* sc-component-id: h3us20-4 */
         .kZFASz{width:100%;} @media (min-width:1em){.kZFASz{height:16px;width:16px;}} @media (min-width:52.5em){.kZFASz{height:16px;width:16px;}}.ZAYGT{width:100%;} @media (min-width:1em){.ZAYGT{height:32px;width:32px;}} @media (min-width:52.5em){.ZAYGT{height:24px;width:24px;}}.jEmYhm{width:100%;} @media (min-width:1em){.jEmYhm{height:16px;width:16px;}}.jZKdyj{width:100%;} @media (min-width:1em){.jZKdyj{height:16px;width:16px;}} @media (min-width:52.5em){.jZKdyj{height:0px;width:0px;}}.cARDRF{width:100%;} @media (min-width:1em){.cARDRF{height:24px;width:24px;}} @media (min-width:52.5em){.cARDRF{height:8px;width:8px;}}.hrzRZZ{width:100%;} @media (min-width:1em){.hrzRZZ{height:32px;width:32px;}}.dGzfoF{width:100%;} @media (min-width:1em){.dGzfoF{height:64px;width:64px;}}.eowFbc{width:100%;} @media (min-width:52.5em){.eowFbc{height:4px;width:4px;}}
         /* sc-component-id: h3us20-5 */
         @media (min-width:52.5em){.ldSSMo{-webkit-order:25;-ms-flex-order:25;order:25;}}@media (min-width:1em){.hMMGVW{-webkit-order:20;-ms-flex-order:20;order:20;}} @media (min-width:52.5em){.hMMGVW{-webkit-order:20;-ms-flex-order:20;order:20;}}@media (min-width:1em){.jTuobL{-webkit-order:30;-ms-flex-order:30;order:30;}} @media (min-width:52.5em){.jTuobL{-webkit-order:10;-ms-flex-order:10;order:10;}}@media (min-width:1em){.dXtwXY{-webkit-order:60;-ms-flex-order:60;order:60;}} @media (min-width:52.5em){.dXtwXY{-webkit-order:40;-ms-flex-order:40;order:40;}}@media (min-width:1em){.eenYUc{-webkit-order:30;-ms-flex-order:30;order:30;}} @media (min-width:52.5em){.eenYUc{-webkit-order:50;-ms-flex-order:50;order:50;}}@media (min-width:1em){.jisuAT{-webkit-order:50;-ms-flex-order:50;order:50;}}@media (min-width:1em){.bBLtXw{-webkit-order:51;-ms-flex-order:51;order:51;}}@media (min-width:1em){.cvARbW{-webkit-order:52;-ms-flex-order:52;order:52;}}@media (min-width:1em){.gNWLDC{-webkit-order:53;-ms-flex-order:53;order:53;}} @media (min-width:52.5em){.gNWLDC{-webkit-order:11;-ms-flex-order:11;order:11;}}@media (min-width:1em){.bEzVbN{-webkit-order:54;-ms-flex-order:54;order:54;}} @media (min-width:52.5em){.bEzVbN{-webkit-order:12;-ms-flex-order:12;order:12;}}@media (min-width:1em){.hWribP{-webkit-order:40;-ms-flex-order:40;order:40;}} @media (min-width:52.5em){.hWribP{-webkit-order:60;-ms-flex-order:60;order:60;}}@media (min-width:1em){.heHIon{-webkit-order:50;-ms-flex-order:50;order:50;}} @media (min-width:52.5em){.heHIon{-webkit-order:10;-ms-flex-order:10;order:10;}}@media (min-width:1em){.dMoaFE{-webkit-order:51;-ms-flex-order:51;order:51;}} @media (min-width:52.5em){.dMoaFE{-webkit-order:11;-ms-flex-order:11;order:11;}}@media (min-width:1em){.eeNNeS{-webkit-order:53;-ms-flex-order:53;order:53;}} @media (min-width:52.5em){.eeNNeS{-webkit-order:12;-ms-flex-order:12;order:12;}}@media (min-width:1em){.bgSgXX{-webkit-order:80;-ms-flex-order:80;order:80;}} @media (min-width:52.5em){.bgSgXX{-webkit-order:80;-ms-flex-order:80;order:80;}}@media (min-width:1em){.gUqBBc{-webkit-order:55;-ms-flex-order:55;order:55;}} @media (min-width:52.5em){.gUqBBc{-webkit-order:11;-ms-flex-order:11;order:11;}}@media (min-width:1em){.ccSbwB{-webkit-order:90;-ms-flex-order:90;order:90;}} @media (min-width:52.5em){.ccSbwB{-webkit-order:90;-ms-flex-order:90;order:90;}}@media (min-width:1em){.sQyxD{-webkit-order:100;-ms-flex-order:100;order:100;}} @media (min-width:52.5em){.sQyxD{-webkit-order:100;-ms-flex-order:100;order:100;}}@media (min-width:1em){.eOOllE{-webkit-order:101;-ms-flex-order:101;order:101;}} @media (min-width:52.5em){.eOOllE{-webkit-order:101;-ms-flex-order:101;order:101;}}@media (min-width:1em){.dUIuRn{-webkit-order:105;-ms-flex-order:105;order:105;}} @media (min-width:52.5em){.dUIuRn{-webkit-order:105;-ms-flex-order:105;order:105;}}@media (min-width:1em){.fZasOH{-webkit-order:110;-ms-flex-order:110;order:110;}} @media (min-width:52.5em){.fZasOH{-webkit-order:110;-ms-flex-order:110;order:110;}}@media (min-width:1em){.jismrm{-webkit-order:120;-ms-flex-order:120;order:120;}} @media (min-width:52.5em){.jismrm{-webkit-order:120;-ms-flex-order:120;order:120;}}@media (min-width:1em){.fXjlVF{-webkit-order:86;-ms-flex-order:86;order:86;}} @media (min-width:52.5em){.fXjlVF{-webkit-order:130;-ms-flex-order:130;order:130;}}@media (min-width:1em){.jKijTl{-webkit-order:87;-ms-flex-order:87;order:87;}} @media (min-width:52.5em){.jKijTl{-webkit-order:140;-ms-flex-order:140;order:140;}}@media (min-width:1em){.kUmnbD{-webkit-order:88;-ms-flex-order:88;order:88;}} @media (min-width:52.5em){.kUmnbD{-webkit-order:150;-ms-flex-order:150;order:150;}}@media (min-width:1em){.dykXjo{-webkit-order:89;-ms-flex-order:89;order:89;}} @media (min-width:52.5em){.dykXjo{-webkit-order:160;-ms-flex-order:160;order:160;}}@media (min-width:1em){.bEpZdo{-webkit-order:130;-ms-flex-order:130;order:130;}} @media (min-width:52.5em){.bEpZdo{-webkit-order:130;-ms-flex-order:130;order:130;}}@media (min-width:1em){.fheUFo{-webkit-order:140;-ms-flex-order:140;order:140;}} @media (min-width:52.5em){.fheUFo{-webkit-order:140;-ms-flex-order:140;order:140;}}@media (min-width:1em){.ghVswA{-webkit-order:150;-ms-flex-order:150;order:150;}} @media (min-width:52.5em){.ghVswA{-webkit-order:150;-ms-flex-order:150;order:150;}}@media (min-width:1em){.coQACr{-webkit-order:160;-ms-flex-order:160;order:160;}} @media (min-width:52.5em){.coQACr{-webkit-order:160;-ms-flex-order:160;order:160;}}@media (min-width:1em){.jvlWsz{-webkit-order:170;-ms-flex-order:170;order:170;}} @media (min-width:52.5em){.jvlWsz{-webkit-order:170;-ms-flex-order:170;order:170;}}@media (min-width:1em){.RdUib{-webkit-order:180;-ms-flex-order:180;order:180;}} @media (min-width:52.5em){.RdUib{-webkit-order:180;-ms-flex-order:180;order:180;}}@media (min-width:1em){.bkznnI{-webkit-order:190;-ms-flex-order:190;order:190;}} @media (min-width:52.5em){.bkznnI{-webkit-order:190;-ms-flex-order:190;order:190;}}@media (min-width:1em){.EAZJj{-webkit-order:200;-ms-flex-order:200;order:200;}} @media (min-width:52.5em){.EAZJj{-webkit-order:200;-ms-flex-order:200;order:200;}}@media (min-width:1em){.jHoWDW{-webkit-order:210;-ms-flex-order:210;order:210;}} @media (min-width:52.5em){.jHoWDW{-webkit-order:210;-ms-flex-order:210;order:210;}}@media (min-width:1em){.eKHEXW{-webkit-order:220;-ms-flex-order:220;order:220;}} @media (min-width:52.5em){.eKHEXW{-webkit-order:220;-ms-flex-order:220;order:220;}}@media (min-width:1em){.iQypEC{-webkit-order:230;-ms-flex-order:230;order:230;}} @media (min-width:52.5em){.iQypEC{-webkit-order:230;-ms-flex-order:230;order:230;}}@media (min-width:1em){.kwBdnA{-webkit-order:240;-ms-flex-order:240;order:240;}} @media (min-width:52.5em){.kwBdnA{-webkit-order:240;-ms-flex-order:240;order:240;}}@media (min-width:1em){.enqtXF{-webkit-order:10;-ms-flex-order:10;order:10;}} @media (min-width:52.5em){.enqtXF{-webkit-order:10;-ms-flex-order:10;order:10;}}@media (min-width:1em){.bZsaea{-webkit-order:30;-ms-flex-order:30;order:30;}} @media (min-width:52.5em){.bZsaea{-webkit-order:30;-ms-flex-order:30;order:30;}}@media (min-width:1em){.hMcgWM{-webkit-order:40;-ms-flex-order:40;order:40;}} @media (min-width:52.5em){.hMcgWM{-webkit-order:40;-ms-flex-order:40;order:40;}}@media (min-width:1em){.Xfofp{-webkit-order:50;-ms-flex-order:50;order:50;}} @media (min-width:52.5em){.Xfofp{-webkit-order:50;-ms-flex-order:50;order:50;}}@media (min-width:1em){.fhqRDx{-webkit-order:60;-ms-flex-order:60;order:60;}} @media (min-width:52.5em){.fhqRDx{-webkit-order:60;-ms-flex-order:60;order:60;}}@media (min-width:1em){.kXGTwk{-webkit-order:70;-ms-flex-order:70;order:70;}} @media (min-width:52.5em){.kXGTwk{-webkit-order:70;-ms-flex-order:70;order:70;}}
         /* sc-component-id: h3us20-0 */
         .gvtffP{margin-right:auto;margin-left:auto;max-width:100%;box-sizing:border-box;box-sizing:border-box;} @media only screen and (min-width:1rem){.gvtffP{padding-left:1rem;padding-right:1rem;}} @media only screen and (min-width:37.5rem){.gvtffP{padding-left:1rem;padding-right:1rem;}} @media only screen and (min-width:45rem){.gvtffP{padding-left:1.5rem;padding-right:1.5rem;}} @media only screen and (min-width:52.5rem){.gvtffP{padding-left:1.5rem;padding-right:1.5rem;}} @media only screen and (min-width:79.5rem){.gvtffP{padding-left:1.5rem;padding-right:1.5rem;}} @media only screen and (min-width:1rem){.gvtffP{width:100%;}} @media only screen and (min-width:37.5rem){.gvtffP{width:100%;}} @media only screen and (min-width:45rem){.gvtffP{width:100%;}} @media only screen and (min-width:52.5rem){.gvtffP{width:79.5rem;}} @media only screen and (min-width:79.5rem){.gvtffP{width:79.5rem;}}.cBfPri{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;} @media only screen and (min-width:1rem){.cBfPri{margin-left:-0.5rem;margin-right:-0.5rem;}} @media only screen and (min-width:37.5rem){.cBfPri{margin-left:-0.5rem;margin-right:-0.5rem;}} @media only screen and (min-width:45rem){.cBfPri{margin-left:-0.75rem;margin-right:-0.75rem;}} @media only screen and (min-width:52.5rem){.cBfPri{margin-left:-0.75rem;margin-right:-0.75rem;}} @media only screen and (min-width:79.5rem){.cBfPri{margin-left:-0.75rem;margin-right:-0.75rem;}}.dlWajz{box-sizing:border-box;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;max-width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;} @media only screen and (min-width:1rem){.dlWajz{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:37.5rem){.dlWajz{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:45rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:52.5rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:71.19rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:78.69rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:79.5rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:91.19rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:103.69rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:116.82rem){.dlWajz{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:1rem){} @media only screen and (min-width:37.5rem){} @media only screen and (min-width:45rem){} @media only screen and (min-width:52.5rem){} @media only screen and (min-width:71.19rem){} @media only screen and (min-width:78.69rem){} @media only screen and (min-width:79.5rem){.dlWajz{-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;max-width:100%;}} @media only screen and (min-width:91.19rem){} @media only screen and (min-width:103.69rem){} @media only screen and (min-width:116.82rem){}.jAHFXn{box-sizing:border-box;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;max-width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;} @media only screen and (min-width:1rem){.jAHFXn{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:37.5rem){.jAHFXn{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:45rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:52.5rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:71.19rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:78.69rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:79.5rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:91.19rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:103.69rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:116.82rem){.jAHFXn{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:1rem){} @media only screen and (min-width:37.5rem){} @media only screen and (min-width:45rem){} @media only screen and (min-width:52.5rem){.jAHFXn{-webkit-flex:1 1 66.66666666666666%;-ms-flex:1 1 66.66666666666666%;flex:1 1 66.66666666666666%;max-width:66.66666666666666%;}} @media only screen and (min-width:71.19rem){.jAHFXn{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;}} @media only screen and (min-width:78.69rem){.jAHFXn{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;}} @media only screen and (min-width:79.5rem){.jAHFXn{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;}} @media only screen and (min-width:91.19rem){.jAHFXn{-webkit-flex:1 1 58.333333333333336%;-ms-flex:1 1 58.333333333333336%;flex:1 1 58.333333333333336%;max-width:58.333333333333336%;}} @media only screen and (min-width:103.69rem){.jAHFXn{-webkit-flex:1 1 66.66666666666666%;-ms-flex:1 1 66.66666666666666%;flex:1 1 66.66666666666666%;max-width:66.66666666666666%;}} @media only screen and (min-width:116.82rem){.jAHFXn{-webkit-flex:1 1 75%;-ms-flex:1 1 75%;flex:1 1 75%;max-width:75%;}}.cpscHx{box-sizing:border-box;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;max-width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;} @media only screen and (min-width:1rem){.cpscHx{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:37.5rem){.cpscHx{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:45rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:52.5rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:71.19rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:78.69rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:79.5rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:91.19rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:103.69rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:116.82rem){.cpscHx{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:1rem){} @media only screen and (min-width:37.5rem){} @media only screen and (min-width:45rem){} @media only screen and (min-width:52.5rem){.cpscHx{-webkit-flex:1 1 33.33333333333333%;-ms-flex:1 1 33.33333333333333%;flex:1 1 33.33333333333333%;max-width:33.33333333333333%;}} @media only screen and (min-width:71.19rem){.cpscHx{-webkit-flex:1 1 33.33333333333333%;-ms-flex:1 1 33.33333333333333%;flex:1 1 33.33333333333333%;max-width:33.33333333333333%;}} @media only screen and (min-width:78.69rem){.cpscHx{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:79.5rem){.cpscHx{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:91.19rem){.cpscHx{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:103.69rem){.cpscHx{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:116.82rem){.cpscHx{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}}.jyICCp{box-sizing:border-box;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;max-width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;} @media only screen and (min-width:1rem){.jyICCp{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:37.5rem){.jyICCp{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:45rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:52.5rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:71.19rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:78.69rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:79.5rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:91.19rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:103.69rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:116.82rem){.jyICCp{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:1rem){.jyICCp{-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;max-width:100%;}} @media only screen and (min-width:37.5rem){} @media only screen and (min-width:45rem){.jyICCp{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:52.5rem){.jyICCp{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:71.19rem){.jyICCp{-webkit-flex:1 1 33.33333333333333%;-ms-flex:1 1 33.33333333333333%;flex:1 1 33.33333333333333%;max-width:33.33333333333333%;}} @media only screen and (min-width:78.69rem){.jyICCp{-webkit-flex:1 1 33.33333333333333%;-ms-flex:1 1 33.33333333333333%;flex:1 1 33.33333333333333%;max-width:33.33333333333333%;}} @media only screen and (min-width:79.5rem){.jyICCp{-webkit-flex:1 1 33.33333333333333%;-ms-flex:1 1 33.33333333333333%;flex:1 1 33.33333333333333%;max-width:33.33333333333333%;}} @media only screen and (min-width:91.19rem){.jyICCp{-webkit-flex:1 1 33.33333333333333%;-ms-flex:1 1 33.33333333333333%;flex:1 1 33.33333333333333%;max-width:33.33333333333333%;}} @media only screen and (min-width:103.69rem){.jyICCp{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:116.82rem){.jyICCp{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}}.hqKhkd{box-sizing:border-box;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;max-width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;} @media only screen and (min-width:1rem){.hqKhkd{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:37.5rem){.hqKhkd{padding-right:0.5rem;padding-left:0.5rem;}} @media only screen and (min-width:45rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:52.5rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:71.19rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:78.69rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:79.5rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:91.19rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:103.69rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:116.82rem){.hqKhkd{padding-right:0.75rem;padding-left:0.75rem;}} @media only screen and (min-width:1rem){} @media only screen and (min-width:37.5rem){} @media only screen and (min-width:45rem){} @media only screen and (min-width:52.5rem){} @media only screen and (min-width:71.19rem){.hqKhkd{-webkit-flex:1 1 16.666666666666664%;-ms-flex:1 1 16.666666666666664%;flex:1 1 16.666666666666664%;max-width:16.666666666666664%;}} @media only screen and (min-width:78.69rem){.hqKhkd{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:79.5rem){.hqKhkd{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;}} @media only screen and (min-width:91.19rem){.hqKhkd{-webkit-flex:1 1 16.666666666666664%;-ms-flex:1 1 16.666666666666664%;flex:1 1 16.666666666666664%;max-width:16.666666666666664%;}} @media only screen and (min-width:103.69rem){.hqKhkd{-webkit-flex:1 1 8.333333333333332%;-ms-flex:1 1 8.333333333333332%;flex:1 1 8.333333333333332%;max-width:8.333333333333332%;}} @media only screen and (min-width:116.82rem){}
         /* sc-component-id: sc-ifAKCX */
         .eMGorO{padding:0px;cursor:unset;}
         /* sc-component-id: sc-bZQynM */
         .lkynZT{color:#ffffff;line-height:20px;font-size:12px;font-weight:400;font-family:'Nunito Sans';margin:0px;}.fwXkTr{color:#4A4A4A;line-height:28px;font-size:20px;font-weight:600;font-family:'Nunito Sans';margin:0px;}.eEEnMS{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;}.dSADzT{line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;}.xrRab{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;}.bRVClF{color:#ffffff;line-height:44px;font-size:36px;font-weight:400;font-family:'Nunito Sans';margin:0px;}.gbvMQR{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:600;font-family:'Nunito Sans';margin:0px;}.izJNjp{color:#4A4A4A;line-height:20px;font-size:14px;font-weight:400;font-family:'Nunito Sans';margin:0px;}.cEdBUU{color:#FF4444;line-height:20px;font-size:14px;font-weight:600;font-family:'Nunito Sans';margin:0px;}
         /* sc-component-id: sc-VigVT */
         .fVNWXx{line-height:24px;font-size:16px;height:40px;min-width:120px;border-width:0px;border-radius:24px;background-color:#f78323;color:#fff;-webkit-flex:1;-ms-flex:1;flex:1;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;cursor:pointer;position:relative;width:100%;padding:0 8px;background:transparent;color:#f78323;border:1px solid;} .fVNWXx:hover{background-color:rgba(0,0,0,0.025);}
         /* sc-component-id: sc-jTzLTM */
         .dYSSwe{box-sizing:border-box;width:24px;height:64px;position:relative;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}
         /* sc-component-id: sc-kpOJdX */
         .eTwHTY{cursor:pointer;position:static;width:30px;min-width:30px;min-height:30px;height:30px;margin-right:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:space-around;-webkit-justify-content:space-around;-ms-flex-pack:space-around;justify-content:space-around;}
         /* sc-component-id: sc-dxgOiQ */
         .ffdXNo,.ffdXNo:before,.ffdXNo:after{width:24px;height:2px;border-radius:2px;background-color:#4a4a4a;position:absolute;display:block;content:"";} .ffdXNo:before{top:-8px;} .ffdXNo:after{top:8px;}
         /* sc-component-id: sc-kEYyzF */
         .jLlbDB{cursor:pointer;}
         /* sc-component-id: sc-dVhcbM */
         .jZAxAJ{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;background-color:#ffffff;}.kzqvPB{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:start;-webkit-justify-content:flex-start;-ms-flex-pack:start;justify-content:flex-start;-webkit-align-items:flex-end;-webkit-box-align:flex-end;-ms-flex-align:flex-end;align-items:flex-end;background-color:#ffffff;}.dmyynv{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}.irIYwp{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:flex-start;-webkit-box-align:flex-start;-ms-flex-align:flex-start;align-items:flex-start;background-color:#ffffff;}.hTWoyD{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;margin-bottom:16px;}.cvXZub{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}.iOixbk{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:flex-start;-webkit-box-align:flex-start;-ms-flex-align:flex-start;align-items:flex-start;}.jjsysS{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;background-color:#ffffff;}.hpIrNh{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;margin-bottom:16px;background-color:#ffffff;}.jvSHiQ{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;background-color:#ffffff;}
         /* sc-component-id: sc-bsbRJL */
         .bDzfpu{background-color:#ffffff;overflow:hidden;white-space:nowrap;font-family:'Nunito Sans';z-index:1000;}
         /* sc-component-id: sc-hZSUBg */
         .cVNHmY{list-style-type:none;padding-inline-start:0;padding-left:0px;margin:4px 0;}
         /* sc-component-id: sc-cMhqgX */
         .fwIYkU{margin:0px;position:relative;} .fwIYkU:hover{background-color:#f6f6f6;} .fwIYkU:hover a{color:#6e0ad6;}
         /* sc-component-id: sc-iuJeZd */
         .fknPRF{box-sizing:border-box;display:none;} @media (max-width:48em){.fknPRF{display:initial;}}
         /* sc-component-id: sc-esOvli */
         .ckqtGX{height:1px;overflow:hidden;border-top:1px solid #d2d2d2;margin:4px 0;}
         /* sc-component-id: sc-cmthru */
         .kkjbBk{line-height:21px;font-size:14px;margin-left:32px;font-weight:600;text-align:center;-webkit-text-decoration:none;text-decoration:none;color:#4a4a4a;cursor:pointer;line-height:26.66px;font-size:20px;font-size:calc(16px + (20 - 16) * ((100vw - 360px) / (1024 - 360)));cursor:pointer;margin:0px;padding:10px 0px;padding-left:24px;font-weight:normal;font-size:14px !important;display:block;text-align:left;} @media (max-width:64em){.kkjbBk{font-size:20px;}} @media (min-width:22.5em){.kkjbBk{font-size:16px;}} @media (max-width:48em){.kkjbBk{padding-left:16px;font-size:16px !important;}}
         /* sc-component-id: sc-gqPbQI */
         .briYLB{display:none;box-shadow:0 1px 2px 0 rgba(153,153,153,0.2);-webkit-transition:left 500ms ease;transition:left 500ms ease;height:auto;width:100%;height:100%;max-width:300px;left:-310px;position:absolute;float:left;} @media (max-width:48em){.briYLB{display:block;}}
         /* sc-component-id: sc-GMQeP */
         .hRMdWm{background-color:#ffffff;border-color:#e5e5e5;border-bottom-width:1px;border-bottom-style:solid;font-family:'Nunito Sans';}
         /* sc-component-id: sc-exAgwC */
         .JXwqS{height:80px;overflow:initial;padding-left:24px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:start;-webkit-justify-content:flex-start;-ms-flex-pack:start;justify-content:flex-start;max-width:1140px;margin:auto;} @media (max-width:48em){.JXwqS{padding-left:16px;overflow:hidden;}}
         /* sc-component-id: sc-cQFLBn */
         .hwognJ{width:48px;height:48px;margin-right:32px;} @media (max-width:62em){.hwognJ{margin-right:0;}}
         /* sc-component-id: sc-daURTG */
         .bBsenL{line-height:21px;font-size:14px;margin-left:32px;font-weight:600;text-align:center;-webkit-text-decoration:none;text-decoration:none;color:#4a4a4a;} .bBsenL:hover{color:#6e0ad6;} @media (max-width:36em){.bBsenL{display:none;}}
         /* sc-component-id: sc-krvtoX */
         .dHRfoT{display:none;margin-right:16px;position:relative;} @media (max-width:48em){.dHRfoT{display:inherit;}}
         /* sc-component-id: sc-fYiAbW */
         .kIdmZJ{z-index:1000;visibility:hidden;background-color:rgba(0,0,0,0);-webkit-transition:visibility 300ms ease,background 300ms ease;transition:visibility 300ms ease,background 300ms ease;width:100%;height:100%;position:absolute;} @media (max-width:48em){.kIdmZJ.visible{visibility:visible;background-color:rgba(0,0,0,0.55);}}
         /* sc-component-id: sc-1o2mpyl-0 */
         .cGChIZ{background-color:rgb(229,229,229);height:1px;} @media (min-width:52.5em){.cGChIZ{width:88px;}}
         /* sc-component-id: lkx530-0 */
         .iLUrMT{text-align:center;-webkit-flex:1;-ms-flex:1;flex:1;margin-left:-1rem;margin-right:-1rem;} @media (min-width:45em){.iLUrMT{margin-left:-1.5rem;margin-right:-1.5rem;}} @media (min-width:52.5em){.iLUrMT{margin-left:0;margin-right:0;}}
         /* sc-component-id: lkx530-1 */
         .gabobT{min-width:100%;max-height:280px;background-color:#E5E5E5;position:relative;font-size:0;vertical-align:middle;}
         /* sc-component-id: lkx530-2 */
         .bgLcPW{white-space:nowrap;overflow:hidden;overflow-x:scroll;-webkit-transform:translateZ(0);-webkit-transform:translateZ(0);-ms-transform:translateZ(0);transform:translateZ(0);-webkit-overflow-scrolling:touch;-webkit-scroll-snap-points-x:repeat(100%);-ms-scroll-snap-points-x:repeat(100%);-webkit-scroll-snap-points-x:repeat(100%);-moz-scroll-snap-points-x:repeat(100%);-ms-scroll-snap-points-x:repeat(100%);scroll-snap-points-x:repeat(100%);-webkit-scroll-snap-type:x mandatory;-ms-scroll-snap-type:x mandatory;-webkit-scroll-snap-type:x mandatory;-moz-scroll-snap-type:x mandatory;-ms-scroll-snap-type:x mandatory;scroll-snap-type:x mandatory;-ms-overflow-style:none;-webkit-transition:all 100ms ease-out;transition:all 100ms ease-out;-webkit-scroll-snap-destination:100% 100%;-ms-scroll-snap-destination:100% 100%;-webkit-scroll-snap-destination:100% 100%;-moz-scroll-snap-destination:100% 100%;-ms-scroll-snap-destination:100% 100%;scroll-snap-destination:100% 100%;-webkit-scroll-behaviour:smooth;-moz-scroll-behaviour:smooth;-ms-scroll-behaviour:smooth;scroll-behaviour:smooth;min-height:280px;} .bgLcPW::-webkit-scrollbar{display:none;width:0 !important;}
         /* sc-component-id: lkx530-4 */
         .jpiGgk{display:inline-block;vertical-align:middle;text-align:center;width:100%;max-height:280px;-webkit-scroll-snap-destination:50% 50%;-ms-scroll-snap-destination:50% 50%;-webkit-scroll-snap-destination:50% 50%;-moz-scroll-snap-destination:50% 50%;-ms-scroll-snap-destination:50% 50%;scroll-snap-destination:50% 50%;-webkit-scroll-snap-align:center none;-moz-scroll-snap-align:center none;-ms-scroll-snap-align:center none;scroll-snap-align:center none;} .jpiGgk img{max-width:100%;max-height:280px;} .jpiGgk #no-photo-placeholder{width:48px;height:48px;top:50%;bottom:50%;position:absolute;-webkit-transform:translate(-50%,-50%);-ms-transform:translate(-50%,-50%);transform:translate(-50%,-50%);}
         /* sc-component-id: lkx530-5 */
         .dHfQOM{right:auto;top:auto;left:50%;bottom:16px;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);border-radius:4px;background-color:#4A4A4A;padding:5px 10px;position:absolute;z-index:0;opacity:1;} .dHfQOM *{opacity:1;}
         /* sc-component-id: lkx530-6 */
         .dEdfLF{position:absolute;padding:50px 15px;top:50%;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);padding:0;left:0;} .dEdfLF svg{-webkit-filter:drop-shadow(0 1px 0px #b4b4b4);filter:drop-shadow(0 1px 0px #b4b4b4);}.bejHmG{position:absolute;padding:50px 15px;top:50%;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);padding:0;right:0;} .bejHmG svg{-webkit-filter:drop-shadow(0 1px 0px #b4b4b4);filter:drop-shadow(0 1px 0px #b4b4b4);}
         /* sc-component-id: sc-28oze1-0 */
         .ebUpuZ{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;background-color:#ffffff;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}
         /* sc-component-id: sc-28oze1-1 */
         .gnyoQn{text-align:center;-webkit-flex:1;-ms-flex:1;flex:1;margin-left:-1rem;margin-right:-1rem;} @media (min-width:45em){.gnyoQn{margin-left:-1.5rem;margin-right:-1.5rem;}} @media (min-width:52.5em){.gnyoQn{margin-left:0;margin-right:0;}}
         /* sc-component-id: sc-28oze1-2 */
         .jhVsdW{min-width:100%;max-height:402px;background-color:#E5E5E5;position:relative;font-size:0;vertical-align:middle;border-radius:8px;overflow:hidden;}
         /* sc-component-id: sc-28oze1-3 */
         .zSAIq{white-space:nowrap;overflow:hidden;-webkit-transform:translateZ(0);-webkit-transform:translateZ(0);-ms-transform:translateZ(0);transform:translateZ(0);-webkit-transition:all 100ms ease-out;transition:all 100ms ease-out;-webkit-scroll-behavior:smooth;-moz-scroll-behavior:smooth;-ms-scroll-behavior:smooth;scroll-behavior:smooth;min-height:402px;border-radius:8px;}
         /* sc-component-id: sc-28oze1-5 */
         .bQbWAr{display:inline-block;vertical-align:middle;text-align:center;overflow:hidden;width:100%;max-height:402px;background-color:#E5E5E5;} .bQbWAr .image{width:100%;max-height:402px;object-fit:contain;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;position:absolute;bottom:50%;right:50%;-webkit-transform:translate(50%,50%);-ms-transform:translate(50%,50%);transform:translate(50%,50%);} .bQbWAr .imageIE{width:auto !important;} .bQbWAr #no-photo-placeholder{width:48px;height:48px;top:50%;bottom:50%;left:50%;right:50%;position:absolute;-webkit-transform:translate(-50%,-50%);-ms-transform:translate(-50%,-50%);transform:translate(-50%,-50%);}
         /* sc-component-id: sc-28oze1-7 */
         .kCQFBe{position:absolute;top:50%;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);left:16px;}.hEwMYq{position:absolute;top:50%;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);right:16px;}
         /* sc-component-id: sc-28oze1-8 */
         .iGQsBq{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:#ffffff;cursor:pointer;width:40px;height:40px;border-radius:50%;box-shadow:0 2px 4px -1px rgba(0,0,0,0.2),0 1px 10px 0 rgba(0,0,0,0.12),0 4px 5px 0 rgba(0,0,0,0.14);} .iGQsBq:hover{background-color:#E5E5E5;}
         /* sc-component-id: sc-28oze1-9 */
         .gYqcOg{position:relative;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}
         /* sc-component-id: sc-28oze1-10 */
         .TQjCg{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;margin-left:auto;margin-right:auto;list-style:none;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;margin:0;padding:0;margin-left:8px;height:402px;overflow:hidden;-webkit-transition:all 450ms ease-out;transition:all 450ms ease-out;-webkit-scroll-behavior:smooth;-moz-scroll-behavior:smooth;-ms-scroll-behavior:smooth;scroll-behavior:smooth;}
         /* sc-component-id: sc-28oze1-11 */
         .evwHUf{line-height:0;padding:0 0 8px;} .evwHUf:last-child{padding-bottom:0;}
         /* sc-component-id: sc-28oze1-12 */
         .inOGdV{height:56px;width:56px;border-radius:4px;overflow:hidden;position:relative;will-change:opacity;cursor:pointer;-webkit-transition:all 0.2s ease-in-out;transition:all 0.2s ease-in-out;opacity:1;}.krfoAB{height:56px;width:56px;border-radius:4px;overflow:hidden;position:relative;will-change:opacity;cursor:pointer;-webkit-transition:all 0.2s ease-in-out;transition:all 0.2s ease-in-out;opacity:0.64;}
         /* sc-component-id: sc-28oze1-13 */
         .fDJoux{position:absolute;left:50%;top:50%;-webkit-transform:translate(-50%,-50%);-ms-transform:translate(-50%,-50%);transform:translate(-50%,-50%);border-radius:4px;height:100%;width:100%;object-fit:cover;}
         /* sc-component-id: sc-28oze1-14 */
         .dxiZkQ{position:absolute;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);padding:0;width:100%;text-align:center;top:0;}.GtSha{position:absolute;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);padding:0;width:100%;text-align:center;bottom:0;}
         /* sc-component-id: sc-28oze1-15 */
         .gBLONq{background-color:#ffffff;cursor:pointer;line-height:0;}
         /* sc-component-id: sc-28oze1-16 */
         .hKSfQK{background-image:url(https://placekitten.com/g/400/300);background-repeat:no-repeat;background-size:cover;background-position:50%;-webkit-filter:blur(32px);filter:blur(32px);position:fixed;height:120%;width:120%;-webkit-transform:translate(-32px,-32px);-ms-transform:translate(-32px,-32px);transform:translate(-32px,-32px);}.lhgKeG{background-image:url(https://placekitten.com/g/800/300);background-repeat:no-repeat;background-size:cover;background-position:50%;-webkit-filter:blur(32px);filter:blur(32px);position:fixed;height:120%;width:120%;-webkit-transform:translate(-32px,-32px);-ms-transform:translate(-32px,-32px);transform:translate(-32px,-32px);}.dSuMqe{background-image:url(https://placekitten.com/g/800/800);background-repeat:no-repeat;background-size:cover;background-position:50%;-webkit-filter:blur(32px);filter:blur(32px);position:fixed;height:120%;width:120%;-webkit-transform:translate(-32px,-32px);-ms-transform:translate(-32px,-32px);transform:translate(-32px,-32px);}
         /* sc-component-id: sc-global-4237316795 */
         .ReactModal__Body--open,.ReactModal__Html--open{overflow:hidden;}
         /* sc-component-id: sc-1wimjbb-0 */
         .dSAaHC{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:44px;font-size:36px;} @media (min-width:52.5em){.dSAaHC{line-height:32px;font-size:24px;}}
         /* sc-component-id: sc-1wimjbb-1 */
         .gQFNBI{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;-webkit-text-decoration:line-through;text-decoration:line-through;} @media (min-width:52.5em){.gQFNBI{line-height:20px;font-size:14px;}}
         /* sc-component-id: sc-1wimjbb-2 */
         .htYGeZ{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:flex-start;-webkit-box-align:flex-start;-ms-flex-align:flex-start;align-items:flex-start;} @media (min-width:52.5em){.htYGeZ{-webkit-flex-direction:column-reverse;-ms-flex-direction:column-reverse;flex-direction:column-reverse;}}
         /* sc-component-id: sc-12l420o-0 */
         .hHjKok{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;background-color:#6E0AD6;border-top-right-radius:8px;border-bottom-right-radius:8px;padding:10px 0 10px 8px;-webkit-flex:1;-ms-flex:1;flex:1;}
         /* sc-component-id: sc-1ukaq78-0 */
         .cvsAxh{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:flex-start;-webkit-box-align:flex-start;-ms-flex-align:flex-start;align-items:flex-start;background-color:#ffffff;} @media (min-width:52.5em){.cvsAxh{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:flex-end;-webkit-box-align:flex-end;-ms-flex-align:flex-end;align-items:flex-end;-webkit-box-pack:start;-webkit-justify-content:flex-start;-ms-flex-pack:start;justify-content:flex-start;}}
         /* sc-component-id: sc-57pm5w-0 */
         .XtcoW{font-family:"Nunito Sans";font-size:16px;line-height:1.5;font-weight:600;color:#9027b0;-webkit-text-decoration:none;text-decoration:none;display:inline-block;}
         /* sc-component-id: sc-1kv8vxj-0 */
         .hAhJaI{margin-block-start:0;margin-block-end:0;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;}
         /* sc-component-id: sc-1sj3nln-0 */
         .eSLnCp{white-space:pre-line;}
         /* sc-component-id: sc-1f2ug0x-0 */
         .iwOlty{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;width:50%;} @media (min-width:45em){.iwOlty{padding-left:0px;width:100%;line-height:20px;font-size:14px;color:#999999;}}
         /* sc-component-id: sc-1f2ug0x-1 */
         .dPJyDS{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:600;font-family:'Nunito Sans';margin:0px;box-sizing:border-box;padding-left:16px;width:50%;} .dPJyDS::before{display:none;} @media (min-width:45em){.dPJyDS{padding-left:0px;width:100%;}}
         /* sc-component-id: sc-1f2ug0x-2 */
         .dBeEuJ{font-family:"Nunito Sans";font-size:16px;line-height:1.5;font-weight:600;color:#9027b0;-webkit-text-decoration:none;text-decoration:none;display:inline-block;box-sizing:border-box;padding-left:16px;width:50%;} @media (min-width:45em){.dBeEuJ{padding-left:0px;width:100%;}}
         /* sc-component-id: sc-1f2ug0x-3 */
         .bsaFM{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;margin-top:16px;background-color:#ffffff;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;} @media (min-width:45em){.bsaFM{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}}
         /* sc-component-id: sc-45jt43-0 */
         .bJcANz{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:28px;font-size:20px;} @media (min-width:52.5em){.bJcANz{line-height:32px;font-size:24px;font-weight:600;}}
         /* sc-component-id: u5u85z-0 */
         .ijPgvg{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;background-color:#ffffff;padding-left:16px;padding-right:16px;padding-top:16px;padding-bottom:16px;border-radius:8px;background-color:white;border-width:1px;border-style:solid;border-color:#E5E5E5;overflow:hidden;padding:8px;border:solid 1px rgb(229,229,229);border-radius:4px;}
         /* sc-component-id: u5u85z-1 */
         .fWCKgV{color:#4a4a4a;font-size:14px;font-weight:500;text-align:center;-webkit-text-decoration:none;text-decoration:none;font-family:'Nunito Sans';cursor:pointer;margin-left:4px;}
         /* sc-component-id: wa4u5y-0 */
         .gJgiaD{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;margin-right:16px;margin-left:16px;background-color:#ffffff;padding-left:16px;padding-right:16px;padding-top:16px;padding-bottom:16px;border-radius:8px;background-color:white;border-width:1px;border-style:solid;border-color:#E5E5E5;overflow:hidden;border-color:#e5e5e5;background-color:#f9f9f9;padding:32px 16px;}
         /* sc-component-id: wa4u5y-1 */
         .fCtGMR{position:relative;margin-bottom:32px;} .fCtGMR .carousel.carousel-slider{overflow:initial;} .fCtGMR .carousel .slide{background-color:initial;} .fCtGMR .carousel .control-dots{padding-inline-start:0px;bottom:-32px;} .fCtGMR .carousel .control-dots .dot{box-shadow:none;background:#D2D2D2;} .fCtGMR .carousel .control-dots .dot.selected,.fCtGMR .carousel .control-dots .dot:hover{background:#6E0AD6;}
         /* sc-component-id: sc-global-516632837 */
         .carousel .control-arrow,.carousel.carousel-slider .control-arrow{-webkit-transition:all .25s ease-in;transition:all .25s ease-in;opacity:.4;position:absolute;z-index:2;top:20px;background:0 0;border:0;font-size:32px;cursor:pointer;} .carousel .control-arrow:hover{opacity:1;} .carousel .control-arrow:before,.carousel.carousel-slider .control-arrow:before{margin:0 5px;display:inline-block;border-top:8px solid transparent;border-bottom:8px solid transparent;content:'';} .carousel .control-disabled.control-arrow{opacity:0;cursor:inherit;display:none;} .carousel .control-prev.control-arrow{left:0;} .carousel .control-prev.control-arrow:before{border-right:8px solid #fff;} .carousel .control-next.control-arrow{right:0;} .carousel .control-next.control-arrow:before{border-left:8px solid #fff;} .carousel{position:relative;width:100%;} .carousel *{box-sizing:border-box;} .carousel img{width:100%;display:inline-block;pointer-events:none;} .carousel .carousel{position:relative;} .carousel .control-arrow{outline:0;border:0;background:0 0;top:50%;margin-top:-13px;font-size:18px;} .carousel .thumbs-wrapper{margin:20px;overflow:hidden;} .carousel .thumbs{-webkit-transition:all .15s ease-in;transition:all .15s ease-in;-webkit-transform:translate3d(0,0,0);-webkit-transform:translate3d(0,0,0);-ms-transform:translate3d(0,0,0);transform:translate3d(0,0,0);position:relative;list-style:none;white-space:nowrap;} .carousel .thumb{-webkit-transition:border .15s ease-in;transition:border .15s ease-in;display:inline-block;width:80px;margin-right:6px;white-space:nowrap;overflow:hidden;border:3px solid #fff;padding:2px;} .carousel .thumb:focus{border:3px solid #ccc;outline:0;} .carousel .thumb.selected,.carousel .thumb:hover{border:3px solid #333;} .carousel .thumb img{vertical-align:top;} .carousel.carousel-slider{position:relative;margin:0;overflow:hidden;} .carousel.carousel-slider .control-arrow{top:0;color:#fff;font-size:26px;bottom:0;margin-top:0;padding:5px;} .carousel.carousel-slider .control-arrow:hover{background:rgba(0,0,0,.2);} .carousel .slider-wrapper{overflow:hidden;margin:auto;width:100%;-webkit-transition:height .15s ease-in;transition:height .15s ease-in;} .carousel .slider-wrapper.axis-horizontal .slider{-ms-box-orient:horizontal;display:-moz-flex;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;} .carousel .slider-wrapper.axis-horizontal .slider .slide{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-flow:column;-ms-flex-flow:column;flex-flow:column;} .carousel .slider-wrapper.axis-vertical{-ms-box-orient:horizontal;display:-moz-flex;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;} .carousel .slider-wrapper.axis-vertical .slider{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;} .carousel .slider{margin:0;padding:0;position:relative;list-style:none;width:100%;} .carousel .slider.animated{-webkit-transition:all .35s ease-in-out;transition:all .35s ease-in-out;} .carousel .slide{min-width:100%;margin:0;position:relative;text-align:center;background:#000;} .carousel .slide img{width:100%;vertical-align:top;border:0;} .carousel .slide iframe{display:inline-block;width:calc(100% - 80px);margin:0 40px 40px;border:0;} .carousel .slide .legend{-webkit-transition:all .5s ease-in-out;transition:all .5s ease-in-out;position:absolute;bottom:40px;left:50%;margin-left:-45%;width:90%;border-radius:10px;background:#000;color:#fff;padding:10px;font-size:12px;text-align:center;opacity:.25;-webkit-transition:opacity .35s ease-in-out;transition:opacity .35s ease-in-out;} .carousel .control-dots{position:absolute;bottom:0;margin:10px 0;text-align:center;width:100%;} @media (min-width:960px){.carousel .control-dots{bottom:0;}} .carousel .control-dots .dot{-webkit-transition:opacity .25s ease-in;transition:opacity .25s ease-in;opacity:.3;box-shadow:1px 1px 2px rgba(0,0,0,.9);background:#fff;border-radius:50%;width:8px;height:8px;cursor:pointer;display:inline-block;margin:0 8px;} .carousel .control-dots .dot.selected,.carousel .control-dots .dot:hover{opacity:1;} .carousel .carousel-status{position:absolute;top:0;right:0;padding:5px;font-size:10px;text-shadow:1px 1px 1px rgba(0,0,0,.9);color:#fff;} .carousel:hover .slide .legend{opacity:1;}
         /* sc-component-id: sc-1mgytjo-0 */
         .kYeoZc{margin-left:-16px;margin-right:-16px;}
         /* sc-component-id: sc-797v4u-0 */
         .bRWdWv .adreply-notification{background:#323232;box-shadow:none;padding:16px 16px;-webkit-transform:translateY(100%);-ms-transform:translateY(100%);transform:translateY(100%);} .bRWdWv .adreply-notification > *{-webkit-transition:opacity 0.1s ease-in;transition:opacity 0.1s ease-in;opacity:0;} .bRWdWv .adreply-notification--slide-up{-webkit-transition:all 0.4s ease-out !important;transition:all 0.4s ease-out !important;-webkit-transform:translateY(0%);-ms-transform:translateY(0%);transform:translateY(0%);} .bRWdWv .adreply-notification--slide-up > *{-webkit-transition:opacity 0.25s ease-out 0.2s;transition:opacity 0.25s ease-out 0.2s;opacity:1;} .bRWdWv .adreply-notification-progressbar{visibility:hidden;}
         /* sc-component-id: sc-15o28wz-0 */
         .grPiYk{padding:0px 4px;}
         /* sc-component-id: sc-15o28wz-1 */
         .gOodOV{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;} @media only screen and (min-width:1rem){.gOodOV{margin-left:-0.5rem;margin-right:-0.5rem;}} @media only screen and (min-width:37.5rem){.gOodOV{margin-left:-0.5rem;margin-right:-0.5rem;}} @media only screen and (min-width:45rem){.gOodOV{margin-left:-0.75rem;margin-right:-0.75rem;}} @media only screen and (min-width:52.5rem){.gOodOV{margin-left:-0.75rem;margin-right:-0.75rem;}} @media only screen and (min-width:79.5rem){.gOodOV{margin-left:-0.75rem;margin-right:-0.75rem;}}
         /* sc-component-id: sc-15o28wz-2 */
         .byaNVW{font-family:"Nunito Sans";font-size:16px;line-height:1.5;font-weight:600;color:#9027b0;-webkit-text-decoration:none;text-decoration:none;display:inline-block;height:20px;width:165px;color:#9129b1;margin-left:4px;opacity:0.8;font-size:14px;font-weight:600;font-style:normal;font-stretch:normal;line-height:1.43;-webkit-letter-spacing:normal;-moz-letter-spacing:normal;-ms-letter-spacing:normal;letter-spacing:normal;}
         /* sc-component-id: pw7c9f-0 */
         .cmiwUT{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;background-color:#ffffff;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-bottom:-16px;}
         /* sc-component-id: pw7c9f-1 */
         .hABWtd{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;padding-left:16px;padding-right:16px;margin-right:16px;margin-bottom:16px;white-space:nowrap;-webkit-flex:unset;-ms-flex:unset;flex:unset;width:auto;} .hABWtd:focus{outline:none;} .hABWtd:hover{background:rgb(247,131,35);color:white;}
         /* sc-component-id: pw7c9f-2 */
         .jTVLFf{display:inline-block;width:8px;}
         /* sc-component-id: hldft4-0 */
         .ehNyVo{height:8px;}
         /* sc-component-id: hldft4-1 */
         .bgNpyx{color:#6E0AD6;line-height:20px;font-size:14px;font-weight:600;font-family:'Nunito Sans';margin:0px;cursor:pointer;}
         /* sc-component-id: hldft4-2 */
         .bRswCL{color:#4A4A4A;line-height:20px;font-size:14px;font-weight:400;font-family:'Nunito Sans';margin:0px;-webkit-line-clamp:2;overflow:hidden;-webkit-box-orient:vertical;display:-webkit-inline-box;}
         /* sc-component-id: hldft4-3 */
         .zvmsw{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-top:16px;padding-right:24px;padding-bottom:16px;padding-left:24px;background-color:#F9F9F9;border-radius:8px;border:solid 1px #E5E5E5;}
         /* sc-component-id: sc-1aze3je-0 */
         .hoRgXC{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-top:16px;margin-bottom:16px;background-color:#ffffff;height:24px;}
         /* sc-component-id: sc-1aze3je-1 */
         .clkGwd{color:#4a4a4a;font-size:14px;font-weight:500;text-align:center;-webkit-text-decoration:none;text-decoration:none;font-family:'Nunito Sans';cursor:pointer;font-size:12px;} .clkGwd:hover{color:#6E0AD6;}
         /* sc-component-id: sc-1aze3je-2 */
         .gQqMLR{margin-right:4px;margin-left:4px;width:12px;height:12px;}
         /* sc-component-id: v1p954-0 */
         .fcSnOq{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;background-color:#ffffff;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;background-color:#F9F9F9;border:solid 1px #E5E5E5;border-radius:4px;padding:12px 16px;}
         /* sc-component-id: v1p954-1 */
         .bPLuuE{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;background-color:#ffffff;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;background-color:inherit;}
         /* sc-component-id: sc-1oq8jzc-0 */
         .dxMPwC{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:20px;font-size:14px;} @media (min-width:52.5em){.dxMPwC{line-height:20px;font-size:12px;}}
         /* sc-component-id: sc-16iz3i7-0 */
         .cPAPOU{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:20px;font-size:14px;} @media (min-width:52.5em){.cPAPOU{line-height:20px;font-size:12px;}}
         /* sc-component-id: sc-16bj9n5-0 */
         .elhoyw{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:20px;font-size:14px;} @media (min-width:52.5em){.elhoyw{line-height:20px;font-size:12px;}}
         /* sc-component-id: sc-1q2spfr-0 */
         .kcotea{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:24px;font-size:16px;} @media (min-width:52.5em){.kcotea{line-height:32px;font-size:24px;font-weight:600;}}
         /* sc-component-id: sc-1leoitd-0 */
         .caJVsD{color:#4A4A4A;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;line-height:32px;font-size:24px;} @media (min-width:52.5em){.caJVsD{line-height:32px;font-size:24px;}}
         /* sc-component-id: sc-1leoitd-1 */
         .koPHXB{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;-webkit-text-decoration:line-through;text-decoration:line-through;} @media (min-width:52.5em){.koPHXB{line-height:20px;font-size:14px;}}
         /* sc-component-id: sc-1leoitd-2 */
         .eOxKth{box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:flex-start;-webkit-box-align:flex-start;-ms-flex-align:flex-start;align-items:flex-start;} @media (min-width:52.5em){.eOxKth{-webkit-flex-direction:column-reverse;-ms-flex-direction:column-reverse;flex-direction:column-reverse;}}
         /* sc-component-id: j3yxk4-0 */
         .fZlUwt{color:#999999;line-height:24px;font-size:16px;font-weight:400;font-family:'Nunito Sans';margin:0px;padding:0 4px;line-height:20px;font-size:14px;} @media (min-width:52.5em){.fZlUwt{line-height:20px;font-size:12px;}}
         /* sc-component-id: sc-1d7g5sb-0 */
         .lcmwPG{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:#ffffff;border-color:#e5e5e5;border-bottom-width:1px;border-bottom-style:solid;}
         /* sc-component-id: sc-1d7g5sb-3 */
         .jyDaIy{display:block;} @media (min-width:116.82em){.jyDaIy{display:block;vertical-align:top;}}
         /* sc-component-id: sc-1d7g5sb-4 */
         @media (min-width:116.82em){.jFvQLW{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;}}
         /* sc-component-id: sc-1d7g5sb-5 */
         .kAnOVp{display:none;} @media (min-width:116.82em){.kAnOVp{display:block;vertical-align:top;min-width:300px;height:100%;}}
      </style>
      <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:400,600,700&amp;display=swap" rel="stylesheet"/>
      <script id="initial-data" type="text/plain" data-json="{&quot;ad&quot;:{&quot;listId&quot;:674853647,&quot;body&quot;:&quot;C�digo do an�ncio: 299&lt;br&gt;Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos cobertura s�o semelhantes aos aptos tipo, por�m com terra�o privativo. Aproveite e marque sua visita. ** As fotos s�o do apartamento decorado. **&quot;,&quot;subject&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299&quot;,&quot;priceLabel&quot;:&quot;Pre�o&quot;,&quot;priceValue&quot;:&quot;R$ 625.697&quot;,&quot;oldPrice&quot;:null,&quot;professionalAd&quot;:true,&quot;category&quot;:1020,&quot;parentCategoryName&quot;:&quot;Im�veis&quot;,&quot;categoryName&quot;:&quot;Apartamentos&quot;,&quot;searchCategoryLevelZero&quot;:1000,&quot;searchCategoryLevelOne&quot;:1001,&quot;searchCategoryLevelTwo&quot;:0,&quot;origListTime&quot;:1583601579,&quot;adReply&quot;:&quot;0&quot;,&quot;friendlyUrl&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamento-a-venda-com-3-dormitorios-em-anita-garibaldi-joinville-cod-299-674853647&quot;,&quot;user&quot;:{&quot;userId&quot;:52848469,&quot;userUid&quot;:51133202,&quot;name&quot;:&quot;GW Junior Imobiliária&quot;},&quot;phone&quot;:{&quot;phone&quot;:&quot;4732024200&quot;,&quot;phoneHidden&quot;:false,&quot;phoneVerified&quot;:true},&quot;images&quot;:[{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/222922100060064.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/222922100060064.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/227922102675525.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 2&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/227922102675525.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/221922101745033.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 3&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/221922101745033.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/223922108582249.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 4&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/223922108582249.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/226922106432034.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 5&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/226922106432034.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/228922109722163.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 6&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/228922109722163.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/222922105111569.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 7&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/222922105111569.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/222922107287253.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 8&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/222922107287253.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/225922100681526.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 9&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/225922100681526.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/229922104698395.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 10&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/229922104698395.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/228922105966788.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 11&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/228922105966788.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/223922102338758.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 12&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/223922102338758.jpg&quot;},{&quot;original&quot;:&quot;https://img.olx.com.br/images/22/229922103193977.jpg&quot;,&quot;originalAlt&quot;:&quot;Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 13&quot;,&quot;thumbnail&quot;:&quot;https://img.olx.com.br/thumbs/22/229922103193977.jpg&quot;}],&quot;location&quot;:{&quot;address&quot;:&quot;Rua Ottokar Doerffel - de 665 a 1739 - lado �mpar&quot;,&quot;neighbourhood&quot;:&quot;Anita Garibaldi&quot;,&quot;neighbourhoodId&quot;:8735,&quot;municipality&quot;:&quot;Joinville&quot;,&quot;municipalityId&quot;:2471,&quot;zipcode&quot;:&quot;89203307&quot;,&quot;mapLati&quot;:0,&quot;mapLong&quot;:0,&quot;uf&quot;:&quot;SC&quot;,&quot;ddd&quot;:&quot;47&quot;,&quot;zoneId&quot;:2481,&quot;zone&quot;:&quot;regiao-de-joinville-e-norte-do-estado&quot;,&quot;region&quot;:&quot;Norte de Santa Catarina e regi�o, SC&quot;},&quot;properties&quot;:[{&quot;name&quot;:&quot;category&quot;,&quot;label&quot;:&quot;Categoria&quot;,&quot;value&quot;:&quot;Apartamentos&quot;,&quot;values&quot;:null,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda&quot;},{&quot;name&quot;:&quot;real_estate_type&quot;,&quot;label&quot;:&quot;Tipo&quot;,&quot;value&quot;:&quot;Venda - apartamento padr�o&quot;,&quot;values&quot;:null,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/apartamentos&quot;},{&quot;name&quot;:&quot;size&quot;,&quot;label&quot;:&quot;�rea �til&quot;,&quot;value&quot;:&quot;184m�&quot;,&quot;values&quot;:null,&quot;url&quot;:null},{&quot;name&quot;:&quot;rooms&quot;,&quot;label&quot;:&quot;Quartos&quot;,&quot;value&quot;:&quot;3&quot;,&quot;values&quot;:null,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/3-quartos&quot;},{&quot;name&quot;:&quot;bathrooms&quot;,&quot;label&quot;:&quot;Banheiros&quot;,&quot;value&quot;:&quot;2&quot;,&quot;values&quot;:null,&quot;url&quot;:null},{&quot;name&quot;:&quot;garage_spaces&quot;,&quot;label&quot;:&quot;Vagas na garagem&quot;,&quot;value&quot;:&quot;2&quot;,&quot;values&quot;:null,&quot;url&quot;:null},{&quot;name&quot;:&quot;apartment_features&quot;,&quot;label&quot;:&quot;Detalhes do im�vel&quot;,&quot;value&quot;:&quot;Academia&quot;,&quot;values&quot;:[{&quot;rawValue&quot;:2,&quot;label&quot;:&quot;Academia&quot;}],&quot;url&quot;:null}],&quot;pubSpecificData&quot;:[{&quot;context&quot;:&quot;width=300,height=250&quot;,&quot;data&quot;:[{&quot;key&quot;:&quot;appnexus_placement_id&quot;,&quot;value&quot;:&quot;11647443&quot;},{&quot;key&quot;:&quot;aol_placement_id&quot;,&quot;value&quot;:&quot;4349217,4349221&quot;},{&quot;key&quot;:&quot;criteo_zone_id&quot;,&quot;value&quot;:&quot;802888&quot;}]},{&quot;context&quot;:&quot;width=*,height=*&quot;,&quot;data&quot;:[{&quot;key&quot;:&quot;afsh_channel_id&quot;,&quot;value&quot;:null},{&quot;key&quot;:&quot;afsh_pub_id&quot;,&quot;value&quot;:&quot;partner-vert-pla-olx-pdp&quot;}]}],&quot;trackingSpecificData&quot;:[{&quot;key&quot;:&quot;region&quot;,&quot;value&quot;:&quot;Norte de Santa Catarina&quot;}],&quot;searchboxes&quot;:[{&quot;label&quot;:&quot;Apartamentos para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/aluguel/apartamentos&quot;},{&quot;label&quot;:&quot;Apartamentos para alugar em RJ&quot;,&quot;link&quot;:&quot;https://rj.olx.com.br/imoveis/aluguel/apartamentos&quot;},{&quot;label&quot;:&quot;Apartamentos para alugar em SP&quot;,&quot;link&quot;:&quot;https://sp.olx.com.br/imoveis/aluguel/apartamentos&quot;},{&quot;label&quot;:&quot;Apartamentos para temporada&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/temporada/apartamentos&quot;},{&quot;label&quot;:&quot;Apartamentos � venda&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/apartamentos&quot;},{&quot;label&quot;:&quot;Apartamentos � venda em RJ&quot;,&quot;link&quot;:&quot;https://rj.olx.com.br/imoveis/venda/apartamentos&quot;},{&quot;label&quot;:&quot;Apartamentos � venda em SP&quot;,&quot;link&quot;:&quot;https://sp.olx.com.br/imoveis/venda/apartamentos&quot;},{&quot;label&quot;:&quot;Casas para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/aluguel/casas&quot;},{&quot;label&quot;:&quot;Casas para alugar em RJ&quot;,&quot;link&quot;:&quot;https://rj.olx.com.br/imoveis/aluguel/casas&quot;},{&quot;label&quot;:&quot;Casas para alugar em SP&quot;,&quot;link&quot;:&quot;https://sp.olx.com.br/imoveis/aluguel/casas&quot;},{&quot;label&quot;:&quot;Casas para temporada&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/temporada/casas&quot;},{&quot;label&quot;:&quot;Casas � venda&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/casas&quot;},{&quot;label&quot;:&quot;Casas � venda em RJ&quot;,&quot;link&quot;:&quot;https://rj.olx.com.br/imoveis/venda/casas&quot;},{&quot;label&quot;:&quot;Casas � venda em SP&quot;,&quot;link&quot;:&quot;https://sp.olx.com.br/imoveis/venda/casas&quot;},{&quot;label&quot;:&quot;Fazendas para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/fazendas/aluguel&quot;},{&quot;label&quot;:&quot;Fazendas � venda&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/fazendas/compra&quot;},{&quot;label&quot;:&quot;Lan�amentos&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/lancamentos/lancamentos&quot;},{&quot;label&quot;:&quot;Lojas para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/comercio-e-industria/aluguel&quot;},{&quot;label&quot;:&quot;Lojas � venda&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/comercio-e-industria/compra&quot;},{&quot;label&quot;:&quot;Quartos para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/aluguel/aluguel-de-quartos&quot;},{&quot;label&quot;:&quot;S�tios para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/sitios-e-chacaras/aluguel&quot;},{&quot;label&quot;:&quot;S�tios � venda&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/sitios-e-chacaras/compra&quot;},{&quot;label&quot;:&quot;Terrenos para alugar&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/lotes/aluguel&quot;},{&quot;label&quot;:&quot;Terrenos � venda&quot;,&quot;link&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/lotes/compra&quot;}],&quot;breadcrumbUrls&quot;:[{&quot;label&quot;:&quot;Santa Catarina&quot;,&quot;url&quot;:&quot;https://sc.olx.com.br&quot;},{&quot;label&quot;:&quot;Norte de Santa Catarina&quot;,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina&quot;},{&quot;label&quot;:&quot;Venda - casas e apartamentos&quot;,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/imoveis/venda&quot;},{&quot;label&quot;:&quot;Regi�o de Joinville e Norte do Estado&quot;,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda&quot;},{&quot;label&quot;:&quot;Joinville&quot;,&quot;url&quot;:&quot;https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/joinville/imoveis/venda&quot;}],&quot;tags&quot;:null,&quot;carSpecificData&quot;:null,&quot;description&quot;:&quot;C�digo do an�ncio: 299&lt;br&gt;Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos cobertura s�o semelhantes aos aptos tipo, por�m com terra�o privativo. Aproveite e marque sua visita. ** As fotos s�o do apartamento decorado. **&quot;,&quot;price&quot;:&quot;R$ 625.697&quot;,&quot;listTime&quot;:&quot;2020-03-07T17:19:39.000Z&quot;,&quot;locationProperties&quot;:[{&quot;label&quot;:&quot;CEP&quot;,&quot;value&quot;:&quot;89203307&quot;},{&quot;label&quot;:&quot;Munic�pio&quot;,&quot;value&quot;:&quot;Joinville&quot;},{&quot;label&quot;:&quot;Bairro&quot;,&quot;value&quot;:&quot;Anita Garibaldi&quot;},{&quot;label&quot;:&quot;Logradouro&quot;,&quot;value&quot;:&quot;Rua Ottokar Doerffel - de 665 a 1739 - lado �mpar&quot;}],&quot;securityTips&quot;:[&quot;N�o fa�a pagamentos antes de verificar o que est� sendo anunciado.&quot;,&quot;Fique atento com excessos de facilidades e pre�os abaixo do mercado.&quot;,&quot;Busque locais p�blicos e movimentados para suas negocia��es.&quot;],&quot;slotsId&quot;:[&quot;adBottomLocation&quot;],&quot;denounceLink&quot;:&quot;https://denuncia.olx.com.br/report?from=web&amp;data=eyJsaXN0SWQiOjY3NDg1MzY0NywidGl0bGUiOiJBcGFydGFtZW50byDDoCB2ZW5kYSBjb20gMyBkb3JtaXTDs3Jpb3MgZW0gQW5pdGEgZ2FyaWJhbGRpLCBKb2ludmlsbGUgY29kOjI5OSIsInByaWNlIjoiNjI1Njk3In0=&quot;,&quot;nativeVas&quot;:[],&quot;isNativeVasTestAbEnabled&quot;:true,&quot;isFeatured&quot;:false},&quot;urls&quot;:{&quot;CHAT_URL&quot;:&quot;https://m.olx.com.br/anuncio/chat?ad_id=&quot;,&quot;CARTEIRO_SERVICE_URL&quot;:&quot;https://apigw.olx.com.br/v1/seller/email&quot;,&quot;POINTS_OF_SALE_URL&quot;:&quot;https://pointsofsales.olx.com.br&quot;,&quot;AUTH_URL&quot;:&quot;https://apigw.olx.com.br/auth/v1/accounts/my&quot;,&quot;AUTH_ACCESS_KEY&quot;:&quot;kkUAvgIi7zuGcj3j18dJSjeq5nnzPv9Z&quot;,&quot;GOLLUM_URL&quot;:&quot;https://gollum.olx.com.br/api/v1/my-precious&quot;,&quot;FAVORITES_API_URL&quot;:&quot;https://apigw.olx.com.br/cdhv/favorite/api/v1&quot;,&quot;FAVORITES_API_SECRET&quot;:&quot;xobt1DEOn8CblfaIFx5Ul5TNI0bKrZ0i&quot;,&quot;MY_ACCOUNTS_API_URL&quot;:&quot;https://apigw.olx.com.br/v3/me&quot;,&quot;MY_ACCOUNTS_API_SECRET&quot;:&quot;rZNX9XwMdF9ZY7deAzKEJEvQ5cC7JOgQ&quot;,&quot;PHONE_RANGER_API_URL&quot;:&quot;https://apigw.olx.com.br/v1/showphone&quot;},&quot;abTestGroups&quot;:&quot;advAfshNativo_A.ast-showphone-flow_new.autos-native-vas_a.bj-HelpMeDecide_SellerOnlineTitle.bj-listItemOpenInANewTab_A.fixedBar2_box.mfg-autos-market-place-selected-options_early.mfg-autos-market-place_financing-insurance.payments-boletoProgressButton_A.upr-chat-adview-profilelink_A.upr-chat-listing-profilelink_A&quot;,&quot;deviceType&quot;:&quot;desktop&quot;}"></script>
   </head>
   <body>
      <div id="root">
         <div class="h3us20-2 jGvFuF">
            <div id="adownerbar"></div>
         </div>
         <div class="sc-1d7g5sb-0 lcmwPG"></div>
         <div>
            <div class="sc-GMQeP hRMdWm">
               <header class="sc-exAgwC JXwqS">
                  <div class="sc-krvtoX dHRfoT sc-kpOJdX eTwHTY">
                     <div class="sc-dxgOiQ ffdXNo"></div>
                  </div>
                  <div class="sc-cQFLBn hwognJ">
                     <a href="https://www.olx.com.br/" class="sc-kEYyzF jLlbDB">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 40 40">
                           <g fill="none" fill-rule="evenodd">
                              <path fill="#6E0AD6" d="M7.579 26.294c-2.282 0-3.855-1.89-3.855-4.683 0-2.82 1.573-4.709 3.855-4.709 2.28 0 3.855 1.889 3.855 4.682 0 2.82-1.574 4.71-3.855 4.71m0 3.538c4.222 0 7.578-3.512 7.578-8.248 0-4.682-3.173-8.22-7.578-8.22C3.357 13.363 0 16.874 0 21.61c0 4.763 3.173 8.221 7.579 8.221"></path>
                              <path fill="#8CE563" d="M18.278 23.553h7.237c.499 0 .787-.292.787-.798V20.44c0-.505-.288-.798-.787-.798h-4.851V9.798c0-.505-.288-.798-.787-.798h-2.386c-.498 0-.787.293-.787.798v12.159c0 1.038.551 1.596 1.574 1.596"></path>
                              <path fill="#F28000" d="M28.112 29.593l4.353-5.082 4.222 5.082c.367.452.839.452 1.258.08l1.705-1.517c.42-.373.472-.851.079-1.277l-4.694-5.321 4.274-4.869c.367-.426.34-.878-.078-1.277l-1.6-1.463c-.42-.4-.892-.373-1.259.08l-3.907 4.602-3.986-4.603c-.367-.425-.84-.479-1.259-.08l-1.652 1.49c-.42.4-.446.825-.053 1.278l4.354 4.868-4.747 5.348c-.393.452-.34.905.079 1.277l1.652 1.464c.42.372.891.345 1.259-.08"></path>
                           </g>
                        </svg>
                     </a>
                  </div>
                  <a class="sc-gojNiO sc-daURTG bBsenL">Buscar</a>
               </header>
            </div>
            <div class="sc-fYiAbW kIdmZJ">
               <nav class="sc-gqPbQI briYLB sc-bsbRJL bDzfpu">
                  <ul class="sc-hZSUBg cVNHmY">
                     <li class="sc-cMhqgX fwIYkU"><a href="https://www3.olx.com.br/account/form_userinfo" class="sc-kIPQKe sc-cmthru kkjbBk">Minha Conta</a></li>
                     <div class="sc-EHOje sc-iuJeZd fknPRF">
                        <li class="sc-cMhqgX fwIYkU"><a href="https://www.olx.com.br/brasil" class="sc-kIPQKe sc-cmthru kkjbBk">Buscar</a></li>
                     </div>
                     <div class="sc-esOvli ckqtGX"></div>
                     <li class="sc-cMhqgX fwIYkU"><a class="sc-kIPQKe sc-cmthru kkjbBk">Meus an�ncios</a></li>
                     <li class="sc-cMhqgX fwIYkU"><a class="sc-kIPQKe sc-cmthru kkjbBk">Chat</a></li>
                  </ul>
               </nav>
            </div>
         </div>
         <div id="content" class="sc-1d7g5sb-4 jFvQLW">
            <div id="leftside" class="sc-1d7g5sb-5 kAnOVp"></div>
            <div class="sc-1d7g5sb-3 jyDaIy">
               <div class="sc-bdVaJa h3us20-1 h3us20-0 gvtffP">
                  <div class="h3us20-2 jGvFuF">
                     <div class="sc-bwzfXH h3us20-0 cBfPri">
                        <div class="sc-1ys3xot-0 h3us20-0 dlWajz">
                           <div alignItems="center" mt="4" mb="4" class="sc-EHOje sc-dVhcbM sc-1aze3je-0 hoRgXC">
                              <a href="https://sc.olx.com.br" theme="[object Object]" color="dark" hovercolor="#6E0AD6" class="sc-jKJlTe sc-1aze3je-1 clkGwd">
                                 <!-- -->Santa Catarina<!-- --> 
                              </a>
                              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="sc-1aze3je-2 gQqMLR">
                                 <path fill="#4A4A4A" d="M9.47 17.47a.75.75 0 0 0 1.06 1.06l6-6a.75.75 0 0 0 0-1.06l-6-6a.75.75 0 0 0-1.06 1.06L14.94 12l-5.47 5.47z" fill-rule="evenodd"></path>
                              </svg>
                              <a href="https://sc.olx.com.br/norte-de-santa-catarina" theme="[object Object]" color="dark" hovercolor="#6E0AD6" class="sc-jKJlTe sc-1aze3je-1 clkGwd">
                                 <!-- -->Norte de Santa Catarina<!-- --> 
                              </a>
                              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="sc-1aze3je-2 gQqMLR">
                                 <path fill="#4A4A4A" d="M9.47 17.47a.75.75 0 0 0 1.06 1.06l6-6a.75.75 0 0 0 0-1.06l-6-6a.75.75 0 0 0-1.06 1.06L14.94 12l-5.47 5.47z" fill-rule="evenodd"></path>
                              </svg>
                              <a href="https://sc.olx.com.br/norte-de-santa-catarina/imoveis/venda" theme="[object Object]" color="dark" hovercolor="#6E0AD6" class="sc-jKJlTe sc-1aze3je-1 clkGwd">
                                 <!-- -->Venda - casas e apartamentos<!-- --> 
                              </a>
                              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="sc-1aze3je-2 gQqMLR">
                                 <path fill="#4A4A4A" d="M9.47 17.47a.75.75 0 0 0 1.06 1.06l6-6a.75.75 0 0 0 0-1.06l-6-6a.75.75 0 0 0-1.06 1.06L14.94 12l-5.47 5.47z" fill-rule="evenodd"></path>
                              </svg>
                              <a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda" theme="[object Object]" color="dark" hovercolor="#6E0AD6" class="sc-jKJlTe sc-1aze3je-1 clkGwd">
                                 <!-- -->Regi�o de Joinville e Norte do Estado<!-- --> 
                              </a>
                              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="sc-1aze3je-2 gQqMLR">
                                 <path fill="#4A4A4A" d="M9.47 17.47a.75.75 0 0 0 1.06 1.06l6-6a.75.75 0 0 0 0-1.06l-6-6a.75.75 0 0 0-1.06 1.06L14.94 12l-5.47 5.47z" fill-rule="evenodd"></path>
                              </svg>
                              <a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/joinville/imoveis/venda" theme="[object Object]" color="dark" hovercolor="#6E0AD6" class="sc-jKJlTe sc-1aze3je-1 clkGwd">
                                 <!-- -->Joinville<!-- --> 
                              </a>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="sc-bwzfXH h3us20-0 cBfPri">
                     <div class="sc-1ys3xot-0 h3us20-0 jAHFXn">
                        <div class="h3us20-5 ebKott">
                           <div class="h3us20-3 csYflq">
                              <div class="lkx530-0 iLUrMT">
                                 <div class="lkx530-1 gabobT">
                                    <div data-testid="slides-wrapper" class="lkx530-2 bgLcPW">
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/222922100060064.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/227922102675525.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 2"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/221922101745033.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 3"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/223922108582249.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 4"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/226922106432034.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 5"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/228922109722163.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 6"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/222922105111569.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 7"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/222922107287253.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 8"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/225922100681526.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 9"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/229922104698395.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 10"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/228922105966788.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 11"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/223922102338758.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 12"/></div>
                                       <div class="lkx530-4 jpiGgk"><img src="https://img.olx.com.br/images/22/229922103193977.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 13"/></div>
                                    </div>
                                    <div>
                                       <div direction="left" class="lkx530-6 dEdfLF"></div>
                                       <div direction="right" class="lkx530-6 bejHmG">
                                          <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" data-testid="right-nav">
                                             <path fill="white" d="M9.47 17.47a.75.75 0 0 0 1.06 1.06l6-6a.75.75 0 0 0 0-1.06l-6-6a.75.75 0 0 0-1.06 1.06L14.94 12l-5.47 5.47z" fill-rule="evenodd"></path>
                                          </svg>
                                       </div>
                                    </div>
                                    <div data-testid="index" class="lkx530-5 dHfQOM">
                                       <span color="clear" theme="[object Object]" tag="span" weight="" font-weight="400" class="sc-bZQynM lkynZT">
                                          1<!-- --> / <!-- -->13
                                       </span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 hMMGVW">
                           <div class="h3us20-4 kZFASz"></div>
                        </div>
                        <div class="h3us20-5 ldSSMo">
                           <div class="h3us20-2 bdQAUC">
                              <div class="sc-EHOje sc-dVhcbM sc-28oze1-0 ebUpuZ">
                                 <div class="sc-28oze1-1 gnyoQn">
                                    <div style="overflow:hidden" class="sc-28oze1-2 jhVsdW">
                                       <div data-testid="slides-wrapper" class="sc-28oze1-3 zSAIq">
                                          <div style="display:inline-block" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 cxxzCf"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/222922100060064.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 dDmUZN"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/227922102675525.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 2"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 imRhvD"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/221922101745033.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 3"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 ksNXwL"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/223922108582249.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 4"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 ZxebW"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/226922106432034.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 5"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 hETXqo"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/228922109722163.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 6"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 jKRYzY"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/222922105111569.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 7"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 cNgpst"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/222922107287253.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 8"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 dMGHVZ"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/225922100681526.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 9"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 jHADTm"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/229922104698395.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 10"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 hYTBRw"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/228922105966788.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 11"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 eSuhwU"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/223922102338758.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 12"/>
                                          </div>
                                          <div style="display:none" class="sc-28oze1-5 bQbWAr">
                                             <div class="sc-28oze1-16 kMdTGq"></div>
                                             <img class="image " src="https://img.olx.com.br/images/22/229922103193977.jpg" alt="Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299 - Foto 13"/>
                                          </div>
                                       </div>
                                       <div>
                                          <div direction="left" class="sc-28oze1-7 kCQFBe"></div>
                                          <div direction="right" class="sc-28oze1-7 hEwMYq">
                                             <div justifyContent="center" alignItems="center" data-testid="right-nav" class="sc-EHOje sc-dVhcbM sc-28oze1-8 iGQsBq">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                                   <path fill="#4A4A4A" d="M9.47 17.47a.75.75 0 0 0 1.06 1.06l6-6a.75.75 0 0 0 0-1.06l-6-6a.75.75 0 0 0-1.06 1.06L14.94 12l-5.47 5.47z" fill-rule="evenodd"></path>
                                                </svg>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <div class="sc-28oze1-9 gYqcOg">
                                    <ul data-testid="thumbnails-wrapper" class="sc-28oze1-10 TQjCg">
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 inOGdV"><img src="https://img.olx.com.br/thumbs/22/222922100060064.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/227922102675525.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/221922101745033.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/223922108582249.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/226922106432034.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/228922109722163.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/222922105111569.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/222922107287253.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/225922100681526.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/229922104698395.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/228922105966788.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/223922102338758.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                       <li class="sc-28oze1-11 evwHUf">
                                          <div class="sc-28oze1-12 krfoAB"><img src="https://img.olx.com.br/thumbs/22/229922103193977.jpg" class="sc-28oze1-13 fDJoux"/></div>
                                       </li>
                                    </ul>
                                    <div>
                                       <div direction="top" class="sc-28oze1-14 dxiZkQ"></div>
                                       <div direction="bottom" class="sc-28oze1-14 GtSha">
                                          <div data-testid="down-nav" class="sc-28oze1-15 gBLONq">
                                             <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                                <path fill="#4A4A4A" d="M6.28 8.22a.75.75 0 0 0-1.06 1.06l6 6a.75.75 0 0 0 1.06 0l6-6a.75.75 0 0 0-1.06-1.06l-5.47 5.47-5.47-5.47z" fill-rule="evenodd"></path>
                                             </svg>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 eenYUc">
                           <div flexDirection="column" alignItems="flex-start" class="sc-EHOje sc-dVhcbM sc-1ukaq78-0 cvsAxh">
                              <div class="en9h1n-0 iFTjq">
                                 <div flexDirection="column" alignItems="flex-start" backgroundColor="transparent" class="sc-EHOje sc-dVhcbM sc-1wimjbb-2 htYGeZ">
                                    <h2 tag="h2" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1wimjbb-0 dSAaHC">R$ 625.697</h2>
                                 </div>
                              </div>
                              <div class="h3us20-4 jEmYhm"></div>
                              <div class="wrapper_advertisement"></div>
                              <div class="wrapper_advertisement"></div>
                              <div class="wrapper_advertisement"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 hWribP">
                           <div class="h3us20-4 jZKdyj"></div>
                        </div>
                        <div class="h3us20-5 heHIon">
                           <h1 tag="h1" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-45jt43-0 bJcANz">Apartamento � venda com 3 dormit�rios em Anita garibaldi, Joinville cod:299</h1>
                        </div>
                        <div class="h3us20-5 dMoaFE">
                           <div class="h3us20-4 cARDRF"></div>
                        </div>
                        <div class="h3us20-5 eeNNeS">
                           <div class="h3us20-3 csYflq">
                              <span color="grayscale.darker" tag="span" weight="" font-weight="400" class="sc-bZQynM sc-1oq8jzc-0 dxMPwC">
                                 Publicado em <!-- -->07/03 �s 14:19
                              </span>
                           </div>
                           <div class="h3us20-2 bdQAUC">
                              <div backgroundColor="transparent" class="sc-EHOje sc-dVhcbM dmyynv">
                                 <span color="grayscale.darker" tag="span" weight="" font-weight="400" class="sc-bZQynM sc-1oq8jzc-0 dxMPwC">
                                    Publicado em <!-- -->07/03 �s 14:19
                                 </span>
                                 <span color="grayscale.darker" tag="span" weight="" font-weight="400" class="sc-bZQynM j3yxk4-0 fZlUwt">-</span>
                                 <span color="grayscale.darker" tag="span" weight="" font-weight="400" class="sc-bZQynM sc-16iz3i7-0 cPAPOU">
                                    c�d. <!-- -->674853647
                                 </span>
                                 <span color="grayscale.darker" tag="span" weight="" font-weight="400" class="sc-bZQynM j3yxk4-0 fZlUwt">-</span><span color="grayscale.darker" tag="span" weight="" font-weight="400" class="sc-bZQynM sc-16bj9n5-0 elhoyw">an�ncio profissional</span>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 dXtwXY">
                           <div class="h3us20-4 ZAYGT"></div>
                        </div>
                        <div class="h3us20-5 kXGTwk">
                           <div class="h3us20-3 csYflq">
                              <div class="sc-1o2mpyl-0 cGChIZ"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 bgSgXX">
                           <div class="h3us20-4 ZAYGT"></div>
                        </div>
                        <div class="h3us20-5 ciKSei"></div>
                        <div class="h3us20-5 ccSbwB">
                           <div flexDirection="column" alignItems="flex-start" class="sc-EHOje sc-dVhcbM irIYwp">
                              <div class="h3us20-3 csYflq">
                                 <span weight="semiBold" theme="[object Object]" tag="span" color="dark" font-weight="400" class="sc-bZQynM fwXkTr">Descri��o</span>
                                 <div class="h3us20-4 kZFASz"></div>
                              </div>
                              <div class="sc-1sj3nln-0 eSLnCp">
                                 <div flexDirection="column" alignItems="flex-start" class="sc-EHOje sc-dVhcbM irIYwp">
                                    <p class="sc-1kv8vxj-0 hAhJaI"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM eEEnMS">C�digo do an�ncio: 299
                                       Excelente Home Club com infraestrutura completa. Localizado no bairro Atiradores, pr�ximo ao centro e acesso a BR101. Apartamento com 3 dormit�rios, sendo 1 suite, sacada com churrasqueira e demais depend�ncias. Os apartamentos cobertura s�o semelhantes aos aptos tipo, por�m com terra�o privativo. Aproveite e marque sua visita. ** As fotos s�o do apartamento decorado. **</span>
                                    </p>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 sQyxD">
                           <div class="h3us20-4 hrzRZZ"></div>
                        </div>
                        <div class="h3us20-5 eOOllE"></div>
                        <div class="h3us20-5 dUIuRn">
                           <div class="h3us20-2 jGvFuF">
                              <div class="sc-EHOje sc-dVhcbM pw7c9f-0 cmiwUT">
                                 <button type="text" class="pw7c9f-1 hABWtd sc-VigVT fVNWXx">
                                    <div>
                                       <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                          <path fill="currentColor" d="M20.141 11.92A4.637 4.637 0 0 0 16.861 4c-1.23 0-2.41.489-3.28 1.36l-.52.52a1.5 1.5 0 0 1-2.122 0l-.52-.52a4.639 4.639 0 0 0-6.56 6.56l8.14 8.14 8.142-8.14zM12 4.818l.52-.52A6.14 6.14 0 1 1 21.2 12.98l-8.68 8.681a.737.737 0 0 1-1.042 0l-8.681-8.68a6.139 6.139 0 0 1 8.682-8.682l.52.52z" fill-rule="evenodd"></path>
                                       </svg>
                                       <div width="8" class="pw7c9f-2 jTVLFf"></div>
                                    </div>
                                    Favoritar
                                 </button>
                                 <button type="text" class="pw7c9f-1 hABWtd sc-VigVT fVNWXx">
                                    <div>
                                       <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                          <path fill="currentColor" d="M14.449 17.792l-5.652-3.294a3.75 3.75 0 1 1 0-4.997l5.65-3.298a3.75 3.75 0 1 1 .756 1.295l-5.65 3.299c.128.377.197.782.197 1.203 0 .42-.07.825-.197 1.203l5.654 3.295a3.75 3.75 0 1 1-.758 1.294zm1.555.17a2.25 2.25 0 1 0 .113-.192.756.756 0 0 1-.113.191zm-8.034-7.05a.761.761 0 0 1-.052-.09A2.25 2.25 0 1 0 8.25 12a2.24 2.24 0 0 0-.28-1.087zm8.06-4.824a.761.761 0 0 1 .052.09A2.25 2.25 0 1 0 15.75 5c0 .394.102.765.28 1.087z" fill-rule="evenodd"></path>
                                       </svg>
                                    </div>
                                    <div width="8" class="pw7c9f-2 jTVLFf"></div>
                                    Compartilhar
                                 </button>
                                 <div class="h3us20-2 jGvFuF">
                                    <button type="text" class="pw7c9f-1 hABWtd sc-VigVT fVNWXx">
                                       <div>
                                          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                             <path fill="currentColor" d="M3.25 22V3a.75.75 0 0 1 .22-.53c.196-.196.562-.44 1.126-.666C5.47 1.454 6.595 1.25 8 1.25c1.375 0 2.318.27 4.279 1.054 1.79.716 2.596.946 3.721.946 1.22 0 2.156-.17 2.846-.446.226-.09.402-.183.535-.272.064-.042.092-.066.089-.062a.75.75 0 0 1 1.28.53v12a.75.75 0 0 1-.22.53c-.196.196-.562.44-1.126.666-.873.35-1.999.554-3.404.554-1.375 0-2.318-.27-4.279-1.054-1.79-.716-2.596-.946-3.721-.946-1.22 0-2.156.17-2.846.446a3.309 3.309 0 0 0-.404.191V22a.75.75 0 1 1-1.5 0zM8 13.25c1.375 0 2.318.27 4.279 1.054 1.79.716 2.596.946 3.721.946 1.22 0 2.156-.17 2.846-.446.158-.064.292-.128.404-.191V4.255c-.85.313-1.926.495-3.25.495-1.375 0-2.318-.27-4.279-1.054C9.931 2.98 9.125 2.75 8 2.75c-1.22 0-2.156.17-2.846.446a3.309 3.309 0 0 0-.404.191v10.358c.85-.313 1.926-.495 3.25-.495z" fill-rule="evenodd"></path>
                                          </svg>
                                       </div>
                                       <div width="8" class="pw7c9f-2 jTVLFf"></div>
                                       Denunciar
                                    </button>
                                 </div>
                                 <div></div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 fZasOH">
                           <div class="sc-1o2mpyl-0 cGChIZ"></div>
                        </div>
                        <div class="h3us20-5 kaNXxX">
                           <div class="wrapper_advertisement"></div>
                        </div>
                        <div class="h3us20-5 gyABPM">
                           <div class="sc-1o2mpyl-0 cGChIZ"></div>
                        </div>
                        <div class="h3us20-5 jismrm">
                           <div class="h3us20-4 hrzRZZ"></div>
                        </div>
                        <div class="h3us20-5 bEpZdo">
                           <div flexDirection="column" class="sc-EHOje sc-dVhcbM jjsysS">
                              <span weight="semiBold" theme="[object Object]" tag="span" color="dark" font-weight="400" class="sc-bZQynM fwXkTr">Detalhes</span>
                              <div class="h3us20-4 eowFbc"></div>
                              <div data-testid="ad-properties" class="sc-bwzfXH h3us20-0 cBfPri">
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Categoria</dt>
                                       <a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda" class="sc-57pm5w-0 sc-1f2ug0x-2 dBeEuJ">Apartamentos</a>
                                    </div>
                                 </div>
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Tipo</dt>
                                       <a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/apartamentos" class="sc-57pm5w-0 sc-1f2ug0x-2 dBeEuJ">Venda - apartamento padr�o</a>
                                    </div>
                                 </div>
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">�rea �til</dt>
                                       <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">184m�</dd>
                                    </div>
                                 </div>
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Quartos</dt>
                                       <a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/3-quartos" class="sc-57pm5w-0 sc-1f2ug0x-2 dBeEuJ">3</a>
                                    </div>
                                 </div>
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Banheiros</dt>
                                       <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">2</dd>
                                    </div>
                                 </div>
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Vagas na garagem</dt>
                                       <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">2</dd>
                                    </div>
                                 </div>
                                 <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                    <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                       <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Detalhes do im�vel</dt>
                                       <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">Academia</dd>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 fheUFo">
                           <div class="h3us20-4 hHjYSJ"></div>
                        </div>
                        <div class="h3us20-5 ghVswA">
                           <div class="sc-1o2mpyl-0 cGChIZ"></div>
                        </div>
                        <div class="h3us20-5 coQACr">
                           <div class="h3us20-4 hrzRZZ"></div>
                        </div>
                        <div class="h3us20-5 jvlWsz">
                           <div>
                              <div id="recommendation"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 RdUib">
                           <div class="h3us20-4 fiIBIx"></div>
                        </div>
                        <div class="h3us20-5 bkznnI">
                           <div class="sc-1o2mpyl-0 cGChIZ"></div>
                        </div>
                        <div class="h3us20-5 EAZJj">
                           <div class="h3us20-4 hrzRZZ"></div>
                        </div>
                        <div class="h3us20-5 jHoWDW">
                           <div class="h3us20-2 fMOiyI">
                              <div flexDirection="column" class="sc-EHOje sc-dVhcbM jjsysS">
                                 <span weight="semiBold" theme="[object Object]" tag="span" color="dark" font-weight="400" class="sc-bZQynM fwXkTr">Localiza��o</span>
                                 <div class="h3us20-4 eowFbc"></div>
                                 <div data-testid="ad-properties" class="sc-bwzfXH h3us20-0 cBfPri">
                                    <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                       <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                          <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">CEP</dt>
                                          <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">89203307</dd>
                                       </div>
                                    </div>
                                    <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                       <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                          <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Munic�pio</dt>
                                          <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">Joinville</dd>
                                       </div>
                                    </div>
                                    <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                       <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                          <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Bairro</dt>
                                          <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">Anita Garibaldi</dd>
                                       </div>
                                    </div>
                                    <div class="sc-1ys3xot-0 h3us20-0 jyICCp">
                                       <div mt="4" block="true" class="sc-EHOje sc-dVhcbM sc-1f2ug0x-3 bsaFM">
                                          <dt tag="dt" theme="[object Object]" color="dark" weight="" font-weight="400" class="sc-bZQynM sc-1f2ug0x-0 iwOlty">Logradouro</dt>
                                          <dd weight="semiBold" tag="dd" theme="[object Object]" color="dark" font-weight="400" class="sc-bZQynM sc-1f2ug0x-1 dPJyDS">Rua Ottokar Doerffel - de 665 a 1739 - lado �mpar</dd>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                              <div class="h3us20-4 hrzRZZ"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 iQypEC">
                           <div class="h3us20-2 bdQAUC"></div>
                        </div>
                        <div class="h3us20-5 kwBdnA">
                           <div class="h3us20-2 bdQAUC">
                              <div class="h3us20-4 hrzRZZ"></div>
                           </div>
                        </div>
                     </div>
                     <div class="sc-1ys3xot-0 h3us20-0 cpscHx">
                        <div class="h3us20-5 enqtXF">
                           <div class="h3us20-3 csYflq">
                              <div class="sc-1o2mpyl-0 cGChIZ"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 hMMGVW">
                           <div class="h3us20-4 iVqVEN"></div>
                        </div>
                        <div class="h3us20-5 bZsaea">
                           <div class="h3us20-3 csYflq">
                              <div></div>
                           </div>
                        </div>
                        <div class="h3us20-5 hMcgWM">
                           <div class="h3us20-4 iVqVEN"></div>
                        </div>
                        <div class="h3us20-5 Xfofp">
                           <div class="h3us20-3 csYflq">
                              <div class="sc-1o2mpyl-0 cGChIZ"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 fhqRDx">
                           <div class="h3us20-4 iVqVEN"></div>
                        </div>
                        <div class="h3us20-5 kXGTwk">
                           <div class="h3us20-2 bdQAUC">
                              <div flexDirection="row" alignItems="flex-start" backgroundColor="transparent" class="sc-EHOje sc-dVhcbM iOixbk">
                                 <div width="24" height="64" class="sc-EHOje sc-12l420o-1 jhxuI sc-jTzLTM dYSSwe">
                                    <svg class="sc-ifAKCX eMGorO" width="24px" height="64px" viewBox="0 0 24 64">
                                       <path fill="#6E0AD6" d="M22.5567837,4.9542595e-15 L23.9989109,0 L23.9989109,63.9999716 L22.5567837,63.9999716 C19.760336,63.9999716 17.1668634,62.5397636 15.7166337,60.1487484 L1.15985004,36.1487626 C-0.38661668,33.5990799 -0.38661668,30.4008918 1.15985004,27.8512091 L15.7166337,3.85122325 C17.1668634,1.46020804 19.760336,2.2883175e-14 22.5567837,1.24344979e-14 Z"></path>
                                    </svg>
                                 </div>
                                 <div backgroundColor="secondary" class="sc-EHOje sc-dVhcbM sc-12l420o-0 hHjKok">
                                    <h2 tag="h2" color="clear" theme="[object Object]" weight="" font-weight="400" class="sc-bZQynM bRVClF">R$ 625.697</h2>
                                 </div>
                              </div>
                              <div class="h3us20-4 jEmYhm"></div>
                           </div>
                        </div>
                        <div class="h3us20-5 bgSgXX">
                           <div class="h3us20-3 csYflq">
                              <span weight="semiBold" theme="[object Object]" tag="span" color="dark" font-weight="400" class="sc-bZQynM fwXkTr">Anunciante</span>
                              <div class="h3us20-4 jEmYhm"></div>
                           </div>
                           <div class="sc-1ut0abb-0 CDLTm">
                              <div class="sc-1ut0abb-1 fgnfjG" width="0">
                                 <div id="miniprofile" class="sc-EHOje sc-dVhcbM jZAxAJ"></div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 ccSbwB">
                           <div class="h3us20-4 kPEGwP"></div>
                        </div>
                        <div class="h3us20-5 sQyxD">
                           <div class="wrapper_advertisement"></div>
                           <div class="h3us20-4 kPEGwP"></div>
                           <div class="h3us20-3 iRwHp">
                              <div flexDirection="column" class="sc-EHOje sc-dVhcbM jjsysS">
                                 <div mb="4" class="sc-EHOje sc-dVhcbM hpIrNh"><span weight="semiBold" theme="[object Object]" tag="span" color="dark" font-weight="400" class="sc-bZQynM fwXkTr">Dicas de seguran�a</span></div>
                                 <div class="sc-1mgytjo-0 kYeoZc">
                                    <div theme="[object Object]" data-testid="react-responsive-carousel" class="wa4u5y-1 fCtGMR">
                                       <div>
                                          <div class="carousel carousel-slider" style="width:100%">
                                             <button type="button" class="control-arrow control-prev control-disabled"></button>
                                             <div class="slider-wrapper axis-horizontal" style="height:auto">
                                                <ul class="slider animated" style="-webkit-transform:translate3d(-100%,0,0);-moz-transform:translate3d(-100%,0,0);-ms-transform:translate3d(-100%,0,0);-o-transform:translate3d(-100%,0,0);transform:translate3d(-100%,0,0);-ms-transform:translate3d(-100%,0,0);-webkit-transition-duration:350ms;-moz-transition-duration:350ms;-ms-transition-duration:350ms;-o-transition-duration:350ms;transition-duration:350ms;-ms-transition-duration:350ms;height:auto">
                                                   <li class="slide">
                                                      <div ml="4" mr="4" class="sc-EHOje sc-dVhcbM sc-eqIVtm wa4u5y-0 gJgiaD"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM eEEnMS">Busque locais p�blicos e movimentados para suas negocia��es.</span></div>
                                                   </li>
                                                   <li class="slide selected">
                                                      <div ml="4" mr="4" class="sc-EHOje sc-dVhcbM sc-eqIVtm wa4u5y-0 gJgiaD"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM eEEnMS">N�o fa�a pagamentos antes de verificar o que est� sendo anunciado.</span></div>
                                                   </li>
                                                   <li class="slide">
                                                      <div ml="4" mr="4" class="sc-EHOje sc-dVhcbM sc-eqIVtm wa4u5y-0 gJgiaD"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM eEEnMS">Fique atento com excessos de facilidades e pre�os abaixo do mercado.</span></div>
                                                   </li>
                                                   <li class="slide">
                                                      <div ml="4" mr="4" class="sc-EHOje sc-dVhcbM sc-eqIVtm wa4u5y-0 gJgiaD"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM eEEnMS">Busque locais p�blicos e movimentados para suas negocia��es.</span></div>
                                                   </li>
                                                   <li class="slide selected">
                                                      <div ml="4" mr="4" class="sc-EHOje sc-dVhcbM sc-eqIVtm wa4u5y-0 gJgiaD"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM eEEnMS">N�o fa�a pagamentos antes de verificar o que est� sendo anunciado.</span></div>
                                                   </li>
                                                </ul>
                                             </div>
                                             <button type="button" class="control-arrow control-next control-disabled"></button>
                                             <ul class="control-dots">
                                                <li class="dot selected" value="0" role="button" tabindex="0"></li>
                                                <li class="dot" value="1" role="button" tabindex="0"></li>
                                                <li class="dot" value="2" role="button" tabindex="0"></li>
                                             </ul>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="h3us20-2 jGvFuF">
                              <div pl="5" pr="5" pt="4" pb="4" backgroundColor="grayscale.light" alignItems="center" theme="[object Object]" class="sc-EHOje sc-dVhcbM hldft4-3 zvmsw">
                                 <img src="https://static.olx.com.br/cd/vi/images/tip-badge.svg" style="width:40px;height:40px;margin-right:24px"/>
                                 <div flexDirection="column" backgroundColor="transparent" class="sc-EHOje sc-dVhcbM cvXZub">
                                    <span theme="[object Object]" weight="semiBold" tag="span" color="dark" font-weight="400" class="sc-bZQynM gbvMQR">Dicas de seguran�a</span>
                                    <div height="8" class="hldft4-0 ehNyVo"></div>
                                    <div><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM hldft4-2 bRswCL">N�o fa�a pagamentos antes de verificar o que est� sendo anunciado.</span><span theme="[object Object]" color="secondary" weight="semiBold" tag="span" font-weight="400" class="sc-bZQynM hldft4-1 bgNpyx">Ver todas as dicas.</span></div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="h3us20-5 fZasOH">
                           <div class="h3us20-4 kZFASz"></div>
                        </div>
                        <div class="h3us20-5 jismrm">
                           <div class="h3us20-3 iRwHp">
                              <div justifyContent="center" theme="[object Object]" class="sc-EHOje sc-dVhcbM sc-eqIVtm u5u85z-0 ijPgvg"><span theme="[object Object]" tag="span" color="dark" weight="" font-weight="400" class="sc-bZQynM izJNjp">Irregularidades no an�ncio?</span><a href="https://denuncia.olx.com.br/report?from=web&amp;data=eyJsaXN0SWQiOjY3NDg1MzY0NywidGl0bGUiOiJBcGFydGFtZW50byDDoCB2ZW5kYSBjb20gMyBkb3JtaXTDs3Jpb3MgZW0gQW5pdGEgZ2FyaWJhbGRpLCBKb2ludmlsbGUgY29kOjI5OSIsInByaWNlIjoiNjI1Njk3In0=" theme="[object Object]" class="sc-jKJlTe u5u85z-1 fWCKgV"><span color="red" weight="semiBold" theme="[object Object]" tag="span" font-weight="400" class="sc-bZQynM cEdBUU">Denunciar</span></a></div>
                           </div>
                        </div>
                        <div class="h3us20-5 bEpZdo">
                           <div class="h3us20-4 jEmYhm"></div>
                        </div>
                        <div class="h3us20-5 fheUFo">
                           <div id="adsense-slot" style="margin-left:-4px"></div>
                        </div>
                        <div class="h3us20-5 jvlWsz">
                           <div backgroundColor="none" class="sc-EHOje sc-dVhcbM qp0wh1-0 buabox"></div>
                        </div>
                     </div>
                     <div class="sc-1ys3xot-0 h3us20-0 hqKhkd"></div>
                  </div>
               </div>
            </div>
            <div id="rightside" class="sc-1d7g5sb-5 kAnOVp">
               <div class="qp0wh1-2 bEobhK"></div>
            </div>
         </div>
         <div class="hb5mou-0 llPTRe">
            <div class="h3us20-3 csYflq">
               <div class="h3us20-4 hHjYSJ"></div>
               <div flexDirection="column" alignItems="center" backgroundColor="none" class="sc-EHOje sc-dVhcbM iFijkn">
                  <span weight="semiBold" tag="span" color="dark" font-weight="400" class="sc-bZQynM gbvMQR">Baixe gr�tis o aplicativo!</span>
                  <div class="sc-bwzfXH h3us20-0 lfgRpk">
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL"><a href="https://itunes.apple.com/br/app/apple-store/id692808319?pt=839460&amp;ct=footer-mobile&amp;mt=8" target="_blank" class="sc-jKJlTe eQpqjL"><img src="https://static.olx.com.br/img/baixar-na-app-store-botao-3.png" alt="App Store" class="c9d34d-0 dBCfLJ"/></a></div>
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL"><a href="https://play.google.com/store/apps/details?id=com.schibsted.bomnegocio.androidApp&amp;hl=pt_BR&amp;utm_source=mobile&amp;utm_campaign=footer" target="_blank" class="sc-jKJlTe eQpqjL"><img src="https://static.olx.com.br/img/google-play-badge.png" alt="Google Play" class="c9d34d-0 dBCfLJ"/></a></div>
                  </div>
               </div>
               <div class="h3us20-4 hHjYSJ"></div>
               <div class="sc-1o2mpyl-0 cGChIZ"></div>
               <div class="h3us20-4 hrzRZZ"></div>
               <div flexDirection="column" alignItems="center" backgroundColor="none" class="sc-EHOje sc-dVhcbM iFijkn">
                  <div class="sc-bwzfXH h3us20-0 cBfPri">
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL">
                        <a href="https://www.facebook.com/olxbrasil" target="_blank" color="#3a5998" class="sc-jKJlTe pprrbb-0 gkJwMx">
                           <div width="24" height="24" class="sc-EHOje sc-jTzLTM gqIPSz">
                              <svg class="sc-ifAKCX eMGorO" width="24px" height="24px" viewBox="0 0 24 24">
                                 <path fill="#999999" d="M9.21567432,23 L9.21567432,12.4986746 L7,12.4986746 L7,8.88027013 L9.21567432,8.88027013 L9.21567432,6.70790204 C9.21567432,3.75618531 10.4660977,2 14.0209307,2 L16.9796789,2 L16.9796789,5.61972987 L15.1304613,5.61972987 C13.7465962,5.61972987 13.6551514,6.12537869 13.6551514,7.06907978 L13.6490551,8.88027013 L17,8.88027013 L16.6078033,12.4986746 L13.6490551,12.4986746 L13.6490551,23 L9.21567432,23 Z"></path>
                              </svg>
                           </div>
                        </a>
                     </div>
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL">
                        <a href="https://www.linkedin.com/company/olx-brasil" target="_blank" color="#0084bf" class="sc-jKJlTe pprrbb-0 jrdvYV">
                           <div width="24" height="24" class="sc-EHOje sc-jTzLTM gqIPSz">
                              <svg class="sc-ifAKCX eMGorO" width="24px" height="24px" viewBox="0 0 24 24">
                                 <path fill="#999999" d="M3.45402164,8.77180177 L6.96237065,8.77180177 L6.96237065,20.9988475 L3.45402164,20.9988475 L3.45402164,8.77180177 Z M5.11876764,7.2424126 L5.09336783,7.2424126 C3.82337723,7.2424126 3,6.30772186 3,5.12408759 C3,3.91625048 3.84771872,3 5.14310913,3 C6.4374412,3 7.23330198,3.91394545 7.25870179,5.12063004 C7.25870179,6.30426431 6.4374412,7.2424126 5.11876764,7.2424126 L5.11876764,7.2424126 Z M21,21 L17.0217545,21 L17.0217545,14.6715328 C17.0217545,13.0153669 16.3994591,11.8859009 15.0310442,11.8859009 C13.9843603,11.8859009 13.4022813,12.6477142 13.13135,13.3841721 C13.0297507,13.6469458 13.0456256,14.0145985 13.0456256,14.3834038 L13.0456256,21 L9.10442145,21 C9.10442145,21 9.15522107,9.7906262 9.10442145,8.77180177 L13.0456256,8.77180177 L13.0456256,10.6907415 C13.2784572,9.85170957 14.5378645,8.6542451 16.5476246,8.6542451 C19.0410395,8.6542451 21,10.4141375 21,14.2001537 L21,21 L21,21 Z"></path>
                              </svg>
                           </div>
                        </a>
                     </div>
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL">
                        <a href="https://instagram.com/olxbrasil" target="_blank" color="#e1306c" class="sc-jKJlTe pprrbb-0 imqbFB">
                           <div width="24" height="24" class="sc-EHOje sc-jTzLTM gqIPSz">
                              <svg class="sc-ifAKCX eMGorO" width="24px" height="24px" viewBox="0 0 24 24">
                                 <path fill="#999999" d="M11.9999802,2 C14.7158369,2 15.0563809,2.01151157 16.1229475,2.06017771 C17.1873706,2.10876447 17.9142666,2.27778605 18.55038,2.5250069 C19.2079684,2.78056371 19.7656443,3.12249698 20.3215737,3.67842633 C20.877503,4.23435568 21.2194363,4.79203161 21.4749931,5.44962002 C21.722214,6.0857334 21.8912355,6.81262938 21.9398223,7.87705248 C21.9884884,8.94361912 22,9.28416306 22,12.0000198 C22,14.7158766 21.9884884,15.0564206 21.9398223,16.1229872 C21.8912355,17.1874103 21.722214,17.9143063 21.4749931,18.5504197 C21.2194363,19.2080081 20.877503,19.765684 20.3215737,20.3216134 C19.7656443,20.8775427 19.2079684,21.219476 18.55038,21.4750328 C17.9142666,21.7222536 17.1873706,21.8912752 16.1229475,21.939862 C15.0563809,21.9885281 14.7158369,22 11.9999802,22 C9.28412336,22 8.94361912,21.9885281 7.87701279,21.939862 C6.81258969,21.8912752 6.0856937,21.7222536 5.44958032,21.4750328 C4.79199192,21.219476 4.23431598,20.8775427 3.67838663,20.3216134 C3.12245728,19.765684 2.78052401,19.2079684 2.5249672,18.5504197 C2.27774635,17.9143063 2.10872478,17.1874103 2.06013802,16.1229872 C2.01147187,15.0564206 2,14.7158766 2,12.0000198 C2,9.28416306 2.01147187,8.94361912 2.06013802,7.87705248 C2.10872478,6.81262938 2.27774635,6.0857334 2.5249672,5.44962002 C2.78052401,4.79203161 3.12245728,4.23435568 3.67838663,3.67842633 C4.23431598,3.12249698 4.79199192,2.78056371 5.44958032,2.5250069 C6.0856937,2.27778605 6.81258969,2.10876447 7.87701279,2.06017771 C8.94361912,2.01151157 9.28412336,2 11.9999802,2 Z M11.9999802,3.80183828 C9.32985208,3.80183828 9.01360151,3.81200021 7.95910218,3.86011063 C6.98415175,3.9046088 6.45465931,4.06751733 6.10228624,4.2044256 C5.635512,4.38583204 5.30235134,4.60256708 4.95243936,4.95247906 C4.60252738,5.30239103 4.38579234,5.63555169 4.2044256,6.10228624 C4.06747764,6.454699 3.9045691,6.98419144 3.86007094,7.95918157 C3.81196052,9.01364121 3.80179858,9.32989177 3.80179858,12.0000198 C3.80179858,14.6701479 3.81196052,14.9863985 3.86007094,16.0408978 C3.9045691,17.0158483 4.06747764,17.5453407 4.2044256,17.8977535 C4.38579234,18.364488 4.60252738,18.6976487 4.95243936,19.0475606 C5.30235134,19.3974726 5.635512,19.6142077 6.10228624,19.7955744 C6.45465931,19.9325224 6.98415175,20.0954309 7.95914187,20.1399291 C9.01344273,20.1880395 9.3296933,20.1982014 11.9999802,20.1982014 C14.670267,20.1982014 14.9865176,20.1880395 16.0408184,20.1399291 C17.0158086,20.0954309 17.545301,19.9325224 17.8977138,19.7955744 C18.3644483,19.6142077 18.697609,19.3974726 19.0475209,19.0475606 C19.3974329,18.6976487 19.614168,18.364488 19.7955347,17.8977535 C19.9324827,17.5453407 20.0953912,17.0158483 20.1398894,16.0408581 C20.1879998,14.9863985 20.1981617,14.6701479 20.1981617,12.0000198 C20.1981617,9.32989177 20.1879998,9.01364121 20.1398894,7.95914187 C20.0953912,6.98419144 19.9324827,6.454699 19.7955347,6.10228624 C19.614168,5.63555169 19.3974329,5.30239103 19.0475209,4.95247906 C18.697609,4.60256708 18.3644483,4.38583204 17.8977138,4.2044256 C17.545301,4.06751733 17.0158086,3.9046088 16.0408184,3.86011063 C14.9863588,3.81200021 14.6701082,3.80183828 11.9999802,3.80183828 Z M12.0198413,6.88095238 C14.8579587,6.88095238 17.1587302,9.18172388 17.1587302,12.0198413 C17.1587302,14.8579587 14.8579587,17.1587302 12.0198413,17.1587302 C9.18172388,17.1587302 6.88095238,14.8579587 6.88095238,12.0198413 C6.88095238,9.18172388 9.18172388,6.88095238 12.0198413,6.88095238 Z M12.0198413,15.3556203 C13.8621189,15.3556203 15.3556203,13.8621189 15.3556203,12.0198413 C15.3556203,10.1775636 13.8621189,8.68406223 12.0198413,8.68406223 C10.1775636,8.68406223 8.68406223,10.1775636 8.68406223,12.0198413 C8.68406223,13.8621189 10.1775636,15.3556203 12.0198413,15.3556203 Z M18.5079365,6.64283745 C18.5079365,7.30032544 17.974968,7.83333333 17.31748,7.83333333 C16.659992,7.83333333 16.1269841,7.30032544 16.1269841,6.64283745 C16.1269841,5.98534947 16.659992,5.45238095 17.31748,5.45238095 C17.974968,5.45238095 18.5079365,5.98534947 18.5079365,6.64283745 Z"></path>
                              </svg>
                           </div>
                        </a>
                     </div>
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL">
                        <a href="https://twitter.com/olx_Brasil" target="_blank" color="#1da1f2" class="sc-jKJlTe pprrbb-0 xAxyS">
                           <div width="24" height="24" class="sc-EHOje sc-jTzLTM gqIPSz">
                              <svg class="sc-ifAKCX eMGorO" width="24px" height="24px" viewBox="0 0 24 24">
                                 <path fill="#999999" d="M19.7617538,6.52953922 C20.5669425,6.03033367 21.1847743,5.23876932 21.4747315,4.29582551 C20.7208429,4.75920844 19.8877737,5.09432327 18.9989435,5.27574751 C18.2896637,4.489961 17.2759289,4 16.1540177,4 C14.0016435,4 12.2574397,5.80846454 12.2574397,8.03871154 C12.2574397,8.35533728 12.2897811,8.66387404 12.3566943,8.95854398 C9.11809591,8.789831 6.24640488,7.18359093 4.3226507,4.7384082 C3.98696954,5.33699263 3.79515173,6.03033367 3.79515173,6.76989744 C3.79515173,8.17044634 4.48324235,9.40690452 5.52931854,10.1326015 C4.89029759,10.1118012 4.28919411,9.92806587 3.76281035,9.62761808 L3.76281035,9.67730753 C3.76281035,11.6348404 5.10553501,13.2676585 6.89100194,13.6374404 C6.56312731,13.732197 6.21963961,13.7795753 5.86276927,13.7795753 C5.61184481,13.7795753 5.36649645,13.7553084 5.13006985,13.7079301 C5.62522745,15.311859 7.06497623,16.4812942 8.77126255,16.5124946 C7.43634443,17.5964177 5.75570816,18.2412249 3.93009333,18.2412249 C3.61560134,18.2412249 3.30445501,18.2238914 3,18.1857576 C4.72524505,19.3309259 6.77390386,20 8.97534777,20 C16.1462112,20 20.0650936,13.8454427 20.0650936,8.50787231 C20.0650936,8.33222591 20.0628632,8.15773509 20.0550566,7.9855554 C20.8167518,7.41586018 21.4791923,6.70403004 22,5.8939766 C21.3007572,6.21522461 20.549099,6.43247147 19.7617538,6.52953922 Z"></path>
                              </svg>
                           </div>
                        </a>
                     </div>
                     <div class="sc-1ys3xot-0 h3us20-0 bcHDBL">
                        <a href="https://www.youtube.com/user/OLXBrasil" target="_blank" color="#ff0000" class="sc-jKJlTe pprrbb-0 laETac">
                           <div width="24" height="24" class="sc-EHOje sc-jTzLTM gqIPSz">
                              <svg class="sc-ifAKCX eMGorO" width="24px" height="24px" viewBox="0 0 24 24">
                                 <path fill="#999999" d="M21,15.6037999 L21,9.12347286 C21,9.12347286 21,6 17.898048,6 L6.1008937,6 C6.1008937,6 3,6 3,9.12347286 L3,15.6037999 C3,15.6037999 3,18.7272727 6.1008937,18.7272727 L17.898048,18.7272727 C17.898048,18.7272727 21,18.7272727 21,15.6037999 M15.4945908,12.3726945 L9.60183443,15.8574288 L9.60183443,8.88689457 L15.4945908,12.3726945"></path>
                              </svg>
                           </div>
                        </a>
                     </div>
                  </div>
               </div>
               <div class="h3us20-4 hrzRZZ"></div>
               <div class="sc-1o2mpyl-0 cGChIZ"></div>
               <div class="h3us20-4 hrzRZZ"></div>
               <div class="sc-bwzfXH h3us20-0 cBfPri">
                  <div class="sc-1ys3xot-0 h3us20-0 fQnMUj"><span weight="bold" tag="span" color="dark" font-weight="400" class="sc-bZQynM jjXBiT">Pesquisas populares</span></div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/aluguel/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://rj.olx.com.br/imoveis/aluguel/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos para alugar em RJ</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sp.olx.com.br/imoveis/aluguel/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos para alugar em SP</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/temporada/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos para temporada</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos � venda</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://rj.olx.com.br/imoveis/venda/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos � venda em RJ</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sp.olx.com.br/imoveis/venda/apartamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Apartamentos � venda em SP</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/aluguel/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://rj.olx.com.br/imoveis/aluguel/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas para alugar em RJ</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sp.olx.com.br/imoveis/aluguel/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas para alugar em SP</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/temporada/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas para temporada</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/venda/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas � venda</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://rj.olx.com.br/imoveis/venda/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas � venda em RJ</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sp.olx.com.br/imoveis/venda/casas" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Casas � venda em SP</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/fazendas/aluguel" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Fazendas para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/fazendas/compra" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Fazendas � venda</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/lancamentos/lancamentos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Lan�amentos</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/comercio-e-industria/aluguel" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Lojas para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/comercio-e-industria/compra" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Lojas � venda</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/imoveis/aluguel/aluguel-de-quartos" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Quartos para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/sitios-e-chacaras/aluguel" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">S�tios para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/sitios-e-chacaras/compra" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">S�tios � venda</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/lotes/aluguel" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Terrenos para alugar</span></a></div>
                  </div>
                  <div class="sc-1ys3xot-0 h3us20-0 bbzKUS">
                     <div backgroundColor="none" class="sc-EHOje sc-dVhcbM dmyynv"><a href="https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/terrenos/lotes/compra" fontAdjust="text-align: left;" class="sc-jKJlTe kQgXCR"><span weight="light" tag="span" color="dark" font-weight="400" class="sc-bZQynM chp44w-0 ceUXAm">Terrenos � venda</span></a></div>
                  </div>
               </div>
               <div class="h3us20-4 hrzRZZ"></div>
            </div>
            <footer class="sc-cmTdod eDrhyx">
               <div class="sc-jwKygS etZSDD">
                  <div class="sc-btzYZH kxmFLL">
                     <div class="sc-lhVmIH gAyffy"><a href="https://www.olx.com.br/faq.htm" class="sc-elJkPf lptTRt">Ajuda e contato</a><a href="https://www.olx.com.br/seguranca" class="sc-elJkPf sc-jtRfpW iaXsuS">Dicas de seguran�a</a><a target="_blank" href="https://www.olx.com.br/vender" class="sc-elJkPf sc-dqBHgY flxlNT">Vender na OLX</a><a target="_blank" href="https://www.olx.com.br/planos" class="sc-elJkPf sc-kTUwUJ lmXGph">Plano Profissional</a></div>
                     <div class="sc-bYSBpT gdmSRR">
                        <a bgColor="#3a5998" fill="#FFFFFF" href="https://www.facebook.com/olxbrasil" class="sc-feJyhm jcRxkx">
                           <svg width="24" height="24" class="sc-iELTvK jluBXE">
                              <path d="M9.21567432,23 L9.21567432,12.4986746 L7,12.4986746 L7,8.88027013 L9.21567432,8.88027013 L9.21567432,6.70790204 C9.21567432,3.75618531 10.4660977,2 14.0209307,2 L16.9796789,2 L16.9796789,5.61972987 L15.1304613,5.61972987 C13.7465962,5.61972987 13.6551514,6.12537869 13.6551514,7.06907978 L13.6490551,8.88027013 L17,8.88027013 L16.6078033,12.4986746 L13.6490551,12.4986746 L13.6490551,23 L9.21567432,23 Z" class="socialIcon" viewBox="0 0 24 24"></path>
                           </svg>
                        </a>
                        <a bgColor="#ff0000" fill="#FFFFFF" href="https://www.youtube.com/user/OLXBrasil" class="sc-feJyhm HvvMP">
                           <svg width="24" height="24" class="sc-iELTvK jluBXE">
                              <path d="M21,15.6037999 L21,9.12347286 C21,9.12347286 21,6 17.898048,6 L6.1008937,6 C6.1008937,6 3,6 3,9.12347286 L3,15.6037999 C3,15.6037999 3,18.7272727 6.1008937,18.7272727 L17.898048,18.7272727 C17.898048,18.7272727 21,18.7272727 21,15.6037999 M15.4945908,12.3726945 L9.60183443,15.8574288 L9.60183443,8.88689457 L15.4945908,12.3726945" class="socialIcon" viewBox="0 0 24 24"></path>
                           </svg>
                        </a>
                        <a bgColor="#0084bf" fill="#FFFFFF" href="https://www.linkedin.com/company/olx-brasil" class="sc-feJyhm jxAOyn">
                           <svg width="24" height="24" class="sc-iELTvK jluBXE">
                              <path d="M3.45402164,8.77180177 L6.96237065,8.77180177 L6.96237065,20.9988475 L3.45402164,20.9988475 L3.45402164,8.77180177 Z M5.11876764,7.2424126 L5.09336783,7.2424126 C3.82337723,7.2424126 3,6.30772186 3,5.12408759 C3,3.91625048 3.84771872,3 5.14310913,3 C6.4374412,3 7.23330198,3.91394545 7.25870179,5.12063004 C7.25870179,6.30426431 6.4374412,7.2424126 5.11876764,7.2424126 L5.11876764,7.2424126 Z M21,21 L17.0217545,21 L17.0217545,14.6715328 C17.0217545,13.0153669 16.3994591,11.8859009 15.0310442,11.8859009 C13.9843603,11.8859009 13.4022813,12.6477142 13.13135,13.3841721 C13.0297507,13.6469458 13.0456256,14.0145985 13.0456256,14.3834038 L13.0456256,21 L9.10442145,21 C9.10442145,21 9.15522107,9.7906262 9.10442145,8.77180177 L13.0456256,8.77180177 L13.0456256,10.6907415 C13.2784572,9.85170957 14.5378645,8.6542451 16.5476246,8.6542451 C19.0410395,8.6542451 21,10.4141375 21,14.2001537 L21,21 L21,21 Z" class="socialIcon" viewBox="0 0 24 24"></path>
                           </svg>
                        </a>
                        <a bgColor="#e1306c" fill="#FFFFFF" href="https://instagram.com/olxbrasil" class="sc-feJyhm ctISzB">
                           <svg width="24" height="24" class="sc-iELTvK jluBXE">
                              <path d="M11.9999802,2 C14.7158369,2 15.0563809,2.01151157 16.1229475,2.06017771 C17.1873706,2.10876447 17.9142666,2.27778605 18.55038,2.5250069 C19.2079684,2.78056371 19.7656443,3.12249698 20.3215737,3.67842633 C20.877503,4.23435568 21.2194363,4.79203161 21.4749931,5.44962002 C21.722214,6.0857334 21.8912355,6.81262938 21.9398223,7.87705248 C21.9884884,8.94361912 22,9.28416306 22,12.0000198 C22,14.7158766 21.9884884,15.0564206 21.9398223,16.1229872 C21.8912355,17.1874103 21.722214,17.9143063 21.4749931,18.5504197 C21.2194363,19.2080081 20.877503,19.765684 20.3215737,20.3216134 C19.7656443,20.8775427 19.2079684,21.219476 18.55038,21.4750328 C17.9142666,21.7222536 17.1873706,21.8912752 16.1229475,21.939862 C15.0563809,21.9885281 14.7158369,22 11.9999802,22 C9.28412336,22 8.94361912,21.9885281 7.87701279,21.939862 C6.81258969,21.8912752 6.0856937,21.7222536 5.44958032,21.4750328 C4.79199192,21.219476 4.23431598,20.8775427 3.67838663,20.3216134 C3.12245728,19.765684 2.78052401,19.2079684 2.5249672,18.5504197 C2.27774635,17.9143063 2.10872478,17.1874103 2.06013802,16.1229872 C2.01147187,15.0564206 2,14.7158766 2,12.0000198 C2,9.28416306 2.01147187,8.94361912 2.06013802,7.87705248 C2.10872478,6.81262938 2.27774635,6.0857334 2.5249672,5.44962002 C2.78052401,4.79203161 3.12245728,4.23435568 3.67838663,3.67842633 C4.23431598,3.12249698 4.79199192,2.78056371 5.44958032,2.5250069 C6.0856937,2.27778605 6.81258969,2.10876447 7.87701279,2.06017771 C8.94361912,2.01151157 9.28412336,2 11.9999802,2 Z M11.9999802,3.80183828 C9.32985208,3.80183828 9.01360151,3.81200021 7.95910218,3.86011063 C6.98415175,3.9046088 6.45465931,4.06751733 6.10228624,4.2044256 C5.635512,4.38583204 5.30235134,4.60256708 4.95243936,4.95247906 C4.60252738,5.30239103 4.38579234,5.63555169 4.2044256,6.10228624 C4.06747764,6.454699 3.9045691,6.98419144 3.86007094,7.95918157 C3.81196052,9.01364121 3.80179858,9.32989177 3.80179858,12.0000198 C3.80179858,14.6701479 3.81196052,14.9863985 3.86007094,16.0408978 C3.9045691,17.0158483 4.06747764,17.5453407 4.2044256,17.8977535 C4.38579234,18.364488 4.60252738,18.6976487 4.95243936,19.0475606 C5.30235134,19.3974726 5.635512,19.6142077 6.10228624,19.7955744 C6.45465931,19.9325224 6.98415175,20.0954309 7.95914187,20.1399291 C9.01344273,20.1880395 9.3296933,20.1982014 11.9999802,20.1982014 C14.670267,20.1982014 14.9865176,20.1880395 16.0408184,20.1399291 C17.0158086,20.0954309 17.545301,19.9325224 17.8977138,19.7955744 C18.3644483,19.6142077 18.697609,19.3974726 19.0475209,19.0475606 C19.3974329,18.6976487 19.614168,18.364488 19.7955347,17.8977535 C19.9324827,17.5453407 20.0953912,17.0158483 20.1398894,16.0408581 C20.1879998,14.9863985 20.1981617,14.6701479 20.1981617,12.0000198 C20.1981617,9.32989177 20.1879998,9.01364121 20.1398894,7.95914187 C20.0953912,6.98419144 19.9324827,6.454699 19.7955347,6.10228624 C19.614168,5.63555169 19.3974329,5.30239103 19.0475209,4.95247906 C18.697609,4.60256708 18.3644483,4.38583204 17.8977138,4.2044256 C17.545301,4.06751733 17.0158086,3.9046088 16.0408184,3.86011063 C14.9863588,3.81200021 14.6701082,3.80183828 11.9999802,3.80183828 Z M12.0198413,6.88095238 C14.8579587,6.88095238 17.1587302,9.18172388 17.1587302,12.0198413 C17.1587302,14.8579587 14.8579587,17.1587302 12.0198413,17.1587302 C9.18172388,17.1587302 6.88095238,14.8579587 6.88095238,12.0198413 C6.88095238,9.18172388 9.18172388,6.88095238 12.0198413,6.88095238 Z M12.0198413,15.3556203 C13.8621189,15.3556203 15.3556203,13.8621189 15.3556203,12.0198413 C15.3556203,10.1775636 13.8621189,8.68406223 12.0198413,8.68406223 C10.1775636,8.68406223 8.68406223,10.1775636 8.68406223,12.0198413 C8.68406223,13.8621189 10.1775636,15.3556203 12.0198413,15.3556203 Z M18.5079365,6.64283745 C18.5079365,7.30032544 17.974968,7.83333333 17.31748,7.83333333 C16.659992,7.83333333 16.1269841,7.30032544 16.1269841,6.64283745 C16.1269841,5.98534947 16.659992,5.45238095 17.31748,5.45238095 C17.974968,5.45238095 18.5079365,5.98534947 18.5079365,6.64283745 Z" class="socialIcon" viewBox="0 0 24 24"></path>
                           </svg>
                        </a>
                        <a bgColor="#1da1f2" fill="#FFFFFF" href="https://twitter.com/olx_Brasil" class="sc-feJyhm dLlrzL">
                           <svg width="24" height="24" class="sc-iELTvK jluBXE">
                              <path d="M19.7617538,6.52953922 C20.5669425,6.03033367 21.1847743,5.23876932 21.4747315,4.29582551 C20.7208429,4.75920844 19.8877737,5.09432327 18.9989435,5.27574751 C18.2896637,4.489961 17.2759289,4 16.1540177,4 C14.0016435,4 12.2574397,5.80846454 12.2574397,8.03871154 C12.2574397,8.35533728 12.2897811,8.66387404 12.3566943,8.95854398 C9.11809591,8.789831 6.24640488,7.18359093 4.3226507,4.7384082 C3.98696954,5.33699263 3.79515173,6.03033367 3.79515173,6.76989744 C3.79515173,8.17044634 4.48324235,9.40690452 5.52931854,10.1326015 C4.89029759,10.1118012 4.28919411,9.92806587 3.76281035,9.62761808 L3.76281035,9.67730753 C3.76281035,11.6348404 5.10553501,13.2676585 6.89100194,13.6374404 C6.56312731,13.732197 6.21963961,13.7795753 5.86276927,13.7795753 C5.61184481,13.7795753 5.36649645,13.7553084 5.13006985,13.7079301 C5.62522745,15.311859 7.06497623,16.4812942 8.77126255,16.5124946 C7.43634443,17.5964177 5.75570816,18.2412249 3.93009333,18.2412249 C3.61560134,18.2412249 3.30445501,18.2238914 3,18.1857576 C4.72524505,19.3309259 6.77390386,20 8.97534777,20 C16.1462112,20 20.0650936,13.8454427 20.0650936,8.50787231 C20.0650936,8.33222591 20.0628632,8.15773509 20.0550566,7.9855554 C20.8167518,7.41586018 21.4791923,6.70403004 22,5.8939766 C21.3007572,6.21522461 20.549099,6.43247147 19.7617538,6.52953922 Z" class="socialIcon" viewBox="0 0 24 24"></path>
                           </svg>
                        </a>
                     </div>
                  </div>
                  <div color="#f2f2f2" class="sc-EHOje sc-cIShpX htsqvh"></div>
                  <div class="sc-gxMtzJ kDGdTi">
                     <div class="sc-dfVpRl cubwyQ">
                        <nav class="sc-kfGgVZ dJRXJ"><a href="https://ajuda.olx.com.br/s/topic/0TOf4000000HaGYGA0/sobre-olx" class="sc-iyvyFf hSgffZ">Sobre a OLX</a><span class="sc-esjQYD fWDvIg">, </span><a href="https://www.olx.com.br/copyright.htm" class="sc-iyvyFf hSgffZ">Termos de uso</a><span class="sc-esjQYD fWDvIg"> e </span><a href="https://ajuda.olx.com.br/s/article/politica-de-privacidade" class="sc-iyvyFf hSgffZ">Pol�tica de privacidade</a></nav>
                        <address class="sc-kPVwWT gThXzB">� Bom Neg�cio Atividades de Internet Ltda. Rua do Catete, 359, Flamengo - 22220-001 - Rio de Janeiro, RJ</address>
                     </div>
                     <div class="sc-gzOgki hmblNr">Comprar ou alugar imoveis no <a href="https://www.storiaimoveis.com.br" class="sc-iyvyFf sc-hwwEjo irZGon">Storia Im�veis</a></div>
                  </div>
               </div>
            </footer>
         </div>
      </div>
      <script src="https://static.olx.com.br/cd/vi/js/adview-v2/bb0c76560f33cec17a81.bundle_vendors.js" defer="" async=""></script><script src="https://static.olx.com.br/cd/vi/js/adview-v2/06999fee0aa7573623cd.bundle_adview.js" defer="" async=""></script>
   </body>
</html>"""
'''
soup = BeautifulSoup(html, 'html.parser')

js = soup.find("script", {"id": "initial-data"})


try:
    js = json.loads(js["data-json"])
except Exception as e:
    js = ''

print(js["ad"]["body"])



a = ApOlx()
b = a.get_data(html)
print(b.id)
print(b.title)
print(b.description)
print(b.price)
print(b.old_price)
print(b.category)
print(b.url)
print(b.seller)
print(b.phone)
print(b.image)
print(b.city)
print(b.uf)
print(b.cep)
print(b.neighbourhood)
print(b.address)
print(b.dateInsert) '''

print('oi')
time.sleep(5)
print('tchau')
a = ApDco()
b = ApDto('html')
b.title = 'Primeiro'
c = ApDto('html')
c.title = 'Segundo'
aptos=[]
aptos.append(b)
aptos.append(c)
a.write_results(aptos)

