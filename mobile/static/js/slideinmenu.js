/**
 * 
 * Find more about the slide down menu at
 * http://cubiq.org/slide-in-menu
 *
 * Copyright (c) 2010 Matteo Spinelli, http://cubiq.org/
 * Released under MIT license
 * http://cubiq.org/dropbox/mit-license.txt
 * 
 * Version 0.1beta1 - Last updated: 2010.05.28
 * 
 */

function slideInMenu (el, closed) {
	this.container = document.getElementById(el);
	this.handle = this.container.querySelector('.handle');
	
	this.openedPosition = this.container.clientHeight;

	this.container.style.opacity = '1';
	this.container.style.top = '-' + this.openedPosition + 'px';
	this.container.style.webkitTransitionProperty = '-webkit-transform';
	this.container.style.webkitTransitionDuration = '400ms';

	if ( opened===true ) {
		this.open();
	}

	this.handle.addEventListener('touchstart', this);
}

slideInMenu.prototype = {
	pos: 0,
	opened: false,
	
	handleEvent: function(e) {
		switch (e.type) {
			case 'touchstart': this.touchStart(e); break;
			case 'touchmove': this.touchMove(e); break;
			case 'touchend': this.touchEnd(e); break;
		}		
	},
	
	setPosition: function(pos) {
		this.pos = pos;
		this.container.style.webkitTransform = 'translate3d(0,' + pos + 'px,0)';
		
		if (this.pos == this.openedPosition) {
			this.opened = true;
		} else if (this.pos == 0) {
			this.opened = false;
		}
	},
	
	touchStart: function(e) {
		e.preventDefault();
		e.stopPropagation();
		
		this.container.style.webkitTransitionDuration = '0';
		this.startPos = this.pos;
		this.startDelta = e.touches[0].pageY - this.pos;
		
		this.handle.addEventListener('touchmove', this);
		this.handle.addEventListener('touchend', this);
	},
	
	touchMove: function(e) {
		var delta = e.touches[0].pageY - this.startDelta;

		if (delta < 0) {
			delta = 0;
		} else if (delta > this.openedPosition) {
			delta = this.openedPosition;
		}
		
		this.setPosition(delta);
	},
	
	touchEnd: function(e) {
		var strokeLength = this.pos - this.startPos;
		strokeLength*= strokeLength < 0 ? -1 : 1;
		
		if (strokeLength > 3) {		// It seems that on Android is almost impossibile to have a tap without a minimal shift, 3 pixels seems a good compromise
			this.container.style.webkitTransitionDuration = '200ms';
			if (this.pos==this.openedPosition || !this.opened) {
				this.setPosition(this.pos > this.openedPosition/3 ? this.openedPosition : 0);
			} else {
				this.setPosition(this.pos > this.openedPosition ? this.openedPosition : 0);
			}
		} else {
			this.container.style.webkitTransitionDuration = '400ms';
			this.setPosition(!this.opened ? this.openedPosition : 0);
		}

		this.handle.removeEventListener('touchmove', this);
		this.handle.removeEventListener('touchend', this);
	},
	
	open: function() {
		this.setPosition(this.openedPosition);
	},

	close: function() {
		this.setPosition(0);
	},
	
	toggle: function() {
		if (this.opened) {
			this.close();
		} else {
			this.open();
		}
	}
}