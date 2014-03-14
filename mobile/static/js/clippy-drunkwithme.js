function shouldShowClippy() {
    return Math.random() < .005
}

$(document).ready(function() {
    var clippyMessages = [
	"Wow. much DrunkWithMe. very drink",
	"hmmm, I'd go for the car bomb.",
	"Is there something I can help you with?",
	"I can't believe this got rejected from the App Store"
    ];

    if (shouldShowClippy()) {
	console.log("SHOWING CLIPPY");
	clippy.load('Clippy',function(agent) {
	    a = agent;
	    agent.show();
	    agent.moveTo(100,100);
	    agent.speak(clippyMessages[Math.floor(Math.random()*clippyMessages.length)]);
	    agent.animate();
	    setTimeout(function() {agent.hide()},8000);
	});
    }

});
