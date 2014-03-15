function shouldShowClippy() {
    return Math.random() < .005
}

$(document).ready(function() {
    var clippyMessages = [
	"Wow. much DrunkWithMe. very drink",
	"hmmm, I'd go for the car bomb.",
	"I can't believe this got rejected from the App Store",
	"Your drink better have whiskey in it.",
	"Happy St. Patrick's Day!",
	"Go find someone not wearing green and pinch them.",
	"DRINKING CHALLENGE! Challenge current leader to an Irish Car Bomb.",
	"Top of the morning to you!",
	"Have you had a car bomb today?",
	"Rob, Diane and Franklin are so smart.",
	"Poor decisions hurt more than a hangover. Drink Responsibly.",
	"How about a glass of water? Drink Responsibly.",
	"We don't actually have a legal team. Please Drink Responsibly.",
	"I can't believe this got rejected by the App Store!",
	"WTF Rob. Marketing never approved me!!"
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
