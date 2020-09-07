registerSetupFunction("div#content",function(content){var sidebars=document.getElementById("sidebars");if(!sidebars){return;}
if((sidebars.offsetHeight-20)>content.offsetHeight){addClassName(content,'shorter')}},true);registerSetupFunction('label[for=^q$]',function(label){var labelFor=label.htmlFor;var input=document.getElementById(labelFor);if(!input){return;}
if(input.defaultValue.match(/^\s*$/)){input.defaultValue=input.value=elemText(label);}
input.onfocus=function(){if(this.value==this.defaultValue){this.value='';};};input.onblur=function(){if(this.value==''){this.value=this.defaultValue;}};});registerSetupFunction('img[src=big\-feed\-icon\.gif]',function(img){if(lteie6){return;}
img.src=img.src.replace(/\.gif$/,'.png');},true);