// http://paislee.io/how-to-use-github-as-a-minimal-cms/
$(document).ready(function() {
    !function(config) {
        $('.nexrise-tag').each(function() {
            var tagName = $(this).data('nexrise-tag');
            $(this).load(config.prefix + tagName + '.html?cb=' + (new Date().getTime()));
        });
    }({
        prefix: 'https://raw.githubusercontent.com/khobaib-nexrise/khobaib-nexrise.github.io/master/tags/'
    });
});
//end


$(document).ready(function(){

	$("#toggle").click(function(){
		$("#togglee").toggleClass("a b");
	});
	
	$("#toggle").click(function(){
		$("#arrowtoggle").toggleClass("arrowimg1 arrowimg2");
	});
	
	$("#menubars").click(function(){
		
		$("#menutoggle").toggleClass("hide show");
	});
	
	$("#menubars").click(function(){
		
		$("#menubars").toggleClass("menu menuon");
	});
	

});