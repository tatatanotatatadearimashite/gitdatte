
// $(function(){
const box = document.querySelector('.box');

setInterval(setBorderRadius, 300);

function setBorderRadius() {
	box.style.setProperty('--br-blobby', generateBorderRadiusValue());
	box.style.setProperty('--br-blobby-after', generateBorderRadiusValue());
	box.style.setProperty('--br-blobby-before', generateBorderRadiusValue());
}

function generateBorderRadiusValue() {
	return `${getRandomValue()}% ${getRandomValue()}% ${getRandomValue()}% ${getRandomValue()}% / ${getRandomValue()}% ${getRandomValue()}% ${getRandomValue()}%`;
}
	
function getRandomValue() {
	return Math.floor(Math.random() * 50) + 50;
}




const box2 = document.querySelector('.box2');

setInterval(setBorderRadius2, 300);

function setBorderRadius2() {
	box2.style.setProperty('--br-blobby', generateBorderRadiusValue2());
	box2.style.setProperty('--br-blobby-after', generateBorderRadiusValue2());
	box2.style.setProperty('--br-blobby-before', generateBorderRadiusValue2());
}

function generateBorderRadiusValue2() {
	return `${getRandomValue2()}% ${getRandomValue2()}% ${getRandomValue2()}% ${getRandomValue2()}% / ${getRandomValue2()}% ${getRandomValue2()}% ${getRandomValue2()}%`;
}
	
function getRandomValue2() {
	return Math.floor(Math.random() * 50) + 50;
}





const box3 = document.querySelector('.box3');

setInterval(setBorderRadius3, 300);

function setBorderRadius3() {
	box3.style.setProperty('--br-blobby', generateBorderRadiusValue3());
	box3.style.setProperty('--br-blobby-after', generateBorderRadiusValue3());
	box3.style.setProperty('--br-blobby-before', generateBorderRadiusValue3());
}

function generateBorderRadiusValue3() {
	return `${getRandomValue3()}% ${getRandomValue3()}% ${getRandomValue3()}% ${getRandomValue3()}% / ${getRandomValue3()}% ${getRandomValue3()}% ${getRandomValue3()}%`;
}
	
function getRandomValue3() {
	return Math.floor(Math.random() * 50) + 50;
}





const box4 = document.querySelector('.box4');

setInterval(setBorderRadius4, 300);

function setBorderRadius4() {
	box4.style.setProperty('--br-blobby', generateBorderRadiusValue4());
	box4.style.setProperty('--br-blobby-after', generateBorderRadiusValue4());
	box4.style.setProperty('--br-blobby-before', generateBorderRadiusValue4());
}

function generateBorderRadiusValue4() {
	return `${getRandomValue4()}% ${getRandomValue4()}% ${getRandomValue4()}% ${getRandomValue4()}% / ${getRandomValue4()}% ${getRandomValue4()}% ${getRandomValue4()}%`;
}
	
function getRandomValue4() {
	return Math.floor(Math.random() * 50) + 50;
}





const box5 = document.querySelector('.box5');

setInterval(setBorderRadius5, 300);

function setBorderRadius5() {
	box5.style.setProperty('--br-blobby', generateBorderRadiusValue5());
	box5.style.setProperty('--br-blobby-after', generateBorderRadiusValue5());
	box5.style.setProperty('--br-blobby-before', generateBorderRadiusValue5());
}

function generateBorderRadiusValue5() {
	return `${getRandomValue5()}% ${getRandomValue5()}% ${getRandomValue5()}% ${getRandomValue5()}% / ${getRandomValue5()}% ${getRandomValue5()}% ${getRandomValue5()}%`;
}
	
function getRandomValue5() {
	return Math.floor(Math.random() * 50) + 50;
}

// $(function(){

// $(document).ready(function() {
// 	$('.box').jqFloat({
// 		width: 100,
// 		height: 100,
// 		speed: 1000
// 	});
// });
// });