function addClassName(element,className){if(hasClassName(element,className)){return false;}
if(!element.className){element.className=className;}
else{element.className+=' '+className;}
return true;}
function removeClassName(element,className){if(!hasClassName(element,className)){return false;}
var classNames=element.className.split(' ');var newClassNames=[];for(var a=0;a<classNames.length;a++){if(classNames[a]!=className){newClassNames[newClassNames.length]=classNames[a];}}
element.className=newClassNames.join(' ');return true;}
function hasClassName(element,className){var exp=new RegExp("(^|\\s)"+className+"($|\\s)");return(element.className&&exp.exec(element.className))?true:false;}
function elem(name,atts,text){var e=document.createElement(name);if(atts){for(key in atts){if(key=='class'){e.className=atts[key];}
else if(key=='id'){e.id=atts[key];}
else if(key=='href'){e.href=atts[key];}
else if(key=='action'){e.action=atts[key];}
else if(key=='method'){e.method=atts[key];}
else if(key=='title'){e.title=atts[key];}
else if(key=='alt'){e.alt=atts[key];}
else if(key=='border'){e.border=atts[key];}
else if(key=='caption'){e.caption=atts[key];}
else if(key=='cellspacing'){e.cellspacing=atts[key];}
else{e.setAttribute(key,atts[key]);}}}
if(text){e.appendChild(document.createTextNode(text));}
return e;}
function elemText(el){var chlds=el.childNodes;var result='';for(var a=0;a<chlds.length;a++){if(3==chlds[a].nodeType){result+=chlds[a].data;}else if(1==chlds[a].nodeType){result+=elemText(chlds[a]);}}
return result;}
function addEvent(obj,type,fn){if(obj.addEventListener){obj.addEventListener(type,fn,false);EventCache.add(obj,type,fn);}
else if(obj.attachEvent){obj["e"+type+fn]=fn;obj[type+fn]=function(){obj["e"+type+fn](window.event);}
obj.attachEvent("on"+type,obj[type+fn]);EventCache.add(obj,type,fn);}
else{obj["on"+type]=obj["e"+type+fn];}}
var EventCache=function(){var listEvents=[];return{listEvents:listEvents,add:function(node,sEventName,fHandler){listEvents.push(arguments);},flush:function(){var i,item;for(i=listEvents.length-1;i>=0;i=i-1){item=listEvents[i];if(item[0].removeEventListener){item[0].removeEventListener(item[1],item[2],item[3]);};if(item[1].substring(0,2)!="on"){item[1]="on"+item[1];};if(item[0].detachEvent){item[0].detachEvent(item[1],item[2]);};item[0][item[1]]=null;};}};}();addEvent(window,'unload',EventCache.flush);(function(){var setupQueue={};window.registerSetupFunction=function(selector,setup,firstTimeOnly){firstTimeOnly=(firstTimeOnly)?true:false;var sq=setupQueue;var matches=selector.match(/^([a-z][a-z0-9_-]*)?(((#|\.)([a-z][a-z0-9_-]*))|(\[([a-z][a-z0-9_-]*)=(.+)\]))?$/i);if(!matches){throw 'invalid selector: "'+selector+'"';}
var tagName=matches[1];if(!tagName){tagName='*';}
var useId=(matches[4]=='#')?true:false;var classOrId=matches[5];var className=(useId)?'':classOrId;var id=(useId)?classOrId:'';var regObj={'className':className,'id':id,'setup':setup,'ran':false,'firstTimeOnly':(firstTimeOnly||useId),'attName':matches[7],'attPatt':new RegExp(matches[8])};if(!sq[tagName]){sq[tagName]=[regObj];}
else{sq[tagName][sq[tagName].length]=regObj;}}
function runIt(el,regObj){if(regObj.id){regObj.setup(document.getElementById(regObj.id));regObj.ran=true;}else if(regObj.attName){if(regObj.attName=='for'){regObj.attName='htmlFor';}
var attVal=el[regObj.attName];if(!attVal){attVal=el.getAttribute(regObj.attName);}
if(attVal&&attVal.match(regObj.attPatt)){regObj.setup(el);regObj.ran=true;}}else{if((regObj.className&&hasClassName(el,regObj.className))||!regObj.className){regObj.setup(el);regObj.ran=true;}}}
window.runSetupFunctons=function(el){var doc=(el)?el:document;var sq=setupQueue;var els=doc.getElementsByTagName('*');var len=els.length;for(var a=0;a<len;a++){var el=els[a];var lcNodeName=el.nodeName.toLowerCase();var regObjArrayAll=sq['*'];var regObjArrayTag=sq[lcNodeName];if(regObjArrayAll){for(var b=0;b<regObjArrayAll.length;b++){var regObj=regObjArrayAll[b];if(regObj.firstTimeOnly&&regObj.ran){continue;}
runIt(el,regObj);}}
if(regObjArrayTag){for(var b=0;b<regObjArrayTag.length;b++){var regObj=regObjArrayTag[b];if(regObj.firstTimeOnly&&regObj.ran){continue;}
runIt(el,regObj);}}}}
addEvent(window,'load',function(){window.runSetupFunctons(document.body);});})();