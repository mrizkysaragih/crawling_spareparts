/**
 * Created by muhammad.rizky on 11/2/2017.
 */

 var mygallery=new fadeSlideShow({

	wrapperid: "fadeshow", //ID of blank DIV on page to house Slideshow

	dimensions: [300, 399], //width/height of gallery in pixels. Should reflect dimensions of largest image

	imagearray: [

	["images/nseries/detail/0-01_01_4JB1.gif", "images/nseries/print/0-01_01_4JB1.png", "_new", "01. 4JB1"],["images/nseries/detail/0-01_02_4BE1.gif", "images/nseries/print/0-01_02_4BE1.png", "_new", "02. 4BE1"],["images/nseries/detail/0-01_03_4JB1-TC.gif", "images/nseries/print/0-01_03_4JB1-TC.png", "_new", "03. 4JB1-TC"],["images/nseries/detail/0-01_04_4HF1, 4HG1, 4HG1-T.gif", "images/nseries/print/0-01_04_4HF1, 4HG1, 4HG1-T.png", "_new", "04. 4HF1, 4HG1, 4HG1-T"]
	],

	displaymode: {type:'auto', pause:3000, cycles:0, wraparound:false},

	persist: false, //remember last viewed slide and recall within same session?

	fadeduration: 500, //transition duration (milliseconds)

	descreveal: "ondemand",

	togglerid: ""

 })
