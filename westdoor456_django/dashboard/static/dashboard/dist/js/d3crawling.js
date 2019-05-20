// Based loosely from this D3 bubble graph https://bl.ocks.org/mbostock/4063269
// And this Forced directed diagram https://bl.ocks.org/mbostock/4062045
let data = [{
	cat: '우유/유제품', name: '우유', value: 30,
	icon: 'dist/img/d3/milk.png',
	desc: `
		D3.js (or just D3 for Data-Driven Documents) is a JavaScript library for
		producing dynamic, interactive data visualizations in web browsers.
			It makes use of the widely implemented SVG, HTML5, and CSS standards.<br>
			This infographic you are viewing is made with D3.
		`
	}, {
		cat: '우유/유제품', name: '두유', value: 10,
		icon: 'dist/img/d3/두유.png',
		desc: `
			Raphaël is a cross-browser JavaScript library that draws Vector graphics for web sites.
			It will use SVG for most browsers, but will use VML for older versions of Internet Explorer.
		`
	}, {
		cat: '라면', name: '신라면', value: 70,
		icon: 'dist/img/d3/신라면.png',
		desc: `
			A JavaScript framework for building data-driven React applications.
			It uses GraphQL as the query language to exchange data between app and server efficiently.
			Queries live next to the views that rely on them, so you can easily reason
			about your app. Relay aggregates queries into efficient network requests to fetch only what you need.
		`
	}, {
		cat: '라면', name: '진라면', value: 40,
		icon: 'dist/img/d3/진라면.png',
		desc: `
			Three.js allows the creation of GPU-accelerated 3D animations using
			the JavaScript language as part of a website without relying on
			proprietary browser plugins. This is possible thanks to the advent of WebGL.
		`
	}, {
		cat: '라면', name: '불닭볶음면', value: 60,
		icon: 'dist/img/d3/불닭볶음면.png',
		desc: `
			Lodash is a JavaScript library which provides <strong>utility functions</strong> for
			common programming tasks using the functional programming paradigm.`
	}, {
		cat: '라면', name: '삼양라면', value: 30,
		icon: 'dist/img/d3/삼양라면.png',
		desc: `
			Handy and resourceful JavaScript library to parse, validate, manipulate, and display dates and times.
		`
	}, {
		cat: '고기', name: '소고기', value: 20,
		icon: 'dist/img/d3/beef.png',
		desc: `
			A javascript library for formatting and manipulating numbers.
		`
	}, {
	cat: '과일', name: '사과', value: 80,
	icon: 'dist/img/d3/apple.png',
	desc: `
			Redux is an open-source JavaScript library designed for managing
			application state. It is primarily used together with React for building user interfaces.
			Redux is inspired by Facebook’s Flux and influenced by functional programming language Elm.
		`
	}, {
		cat: '과일', name: '수박', value: 30,
		icon: 'dist/img/d3/watermelon.png',
		desc: `
			Angular (commonly referred to as 'Angular 2+' or 'Angular 2') is a TypeScript-based
			open-source front-end web application platform led by the Angular Team at Google and
			by a community of individuals and corporations to address all of the parts of the
			developer's workflow while building complex web applications.
		`
	}, {
		cat: '과일', name: '오렌지', value: 50,
		icon: 'dist/img/d3/orange.png',
		desc: `
			Bootstrap is a free and open-source front-end web framework for designing websites
			and web applications. It contains HTML-and CSS-based design templates for typography,
			forms, buttons, navigation and other interface components, as well as optional JavaScript extensions.
		`
	}, {
		cat: '과일', name: '멜론', value: 10,
		icon: 'dist/img/d3/melon.png',
		desc: `
			Ember.js is an open-source JavaScript web framework, based on the Model–view–viewmodel
			(MVVM) pattern. It allows developers to create scalable single-page web applications by
			incorporating common idioms and best practices into the framework.
		`
	}, {
		cat: '채소', name: '당근', value: 30,
		icon: 'dist/img/d3/carrot.png',
		desc: `
			Express.js, or simply Express, is a JavaScript framework designed for building web applications and APIs.
			It is the de facto server framework for Node.js.
		`
	}, {
		cat: '채소', name: '양배추', value: 50,
		icon: 'dist/img/d3/cabbage.png',
		desc: `
			A fast, simple & powerful blog-aware <strong>static website</strong> generator, powered by Node.js.
		`
	}, {
		cat: '채소', name: '무', value: 100,
		icon: 'dist/img/d3/daikon.png',
		desc: `
			React (sometimes written React.js or ReactJS) is an open-source JavaScript framework maintained by Facebook for building user interfaces.
			React processes only user interface in applications and can be used in combination with other JavaScript libraries
			or frameworks such as Redux, Flux, Backbone...
		`
	}, {
		cat: '쌀/잡곡', name: '쌀', value: 40,
		icon: 'dist/img/d3/rice.png',
		desc: `
			Atom is a free and open-source text and source code editor for macOS, Linux, and Windows with support
			for plug-ins written in Node.js, and embedded Git Control, developed by GitHub.
			Atom is a desktop application built using web technologies.
		`
	}, {
		cat: '쌀/잡곡', name: '콩', value: 70,
		icon: 'dist/img/d3/bean.png',
		desc: `
			<strong>Web development tools (devtool)</strong> allow web developers to test and debug their code.
			At Nau, we use the one come with Google Chrome to debug our apps. It is one the the most powerful
			and sophisticated devtool available.
		`
	}, {
		cat: '과자/시리얼', name: '오레오', value: 30,
		icon: 'dist/img/d3/oreo.png',
		desc: `
			Jenkins is an open source automation server. Jenkins helps to automate the non-human part of
			the whole software development process, with now common things like continuous integration,
			but by further empowering teams to implement the technical part of a Continuous Delivery.
		`
	}, {
		cat: '과자/시리얼', name: '나초', value: 100,
		icon: 'dist/img/d3/nacho.png',
		desc: `
			Sublime Text 3 is a powerful and cross-platform source code editor. It is well-known for
			introducing the concept of multi-cursor and lots of text editing command. Besides, its
			plugin ecosystem is very rich which allows enhancing productivity to the fullest.
		`
	}, {
		cat: '과자/시리얼', name: '시리얼', value: 50,
		icon: 'dist/img/d3/cereal.png',
		desc: `
			Visual Studio Code is a cross-platform source code editor developed by Microsoft.
			It includes support for debugging, embedded Git control, syntax highlighting,
			intelligent code completion, snippets, and code refactoring. Its extensions eco system is
			growing quickly and it is becoming the best Front End editors out there.
		`
	}, {
		cat: '음료', name: '콜라', value: 30,
		icon: 'dist/img/d3/cola.png',
		desc: `
			At Nau, web performance is our top priority when development web sites and applications.
			We're practicing code optimization and Front End delivery optimization from day 1.
			To measure the resuslts, we use several tools to audit and benchmark our applications,
			including (but not limit to): Chrome devtool timeline & audit, Google PageSpeed Insights, Web Page Test, Website Grader...
		`
	}, {
		cat: '음료', name: '사이다', value: 20,
		icon: 'dist/img/d3/sprite.png',
		desc: `
			Yeoman is an open source, command-line interface set of tools mainly used to generate
			structure and scaffolding for new projects, especially in JavaScript and Node.js.
			At Nau, we have developed a Yeoman generator that help quickly set up new projects aligned with
			Nau's conventions and standards.
		`
	}, {
		cat: '음료', name: '마운틴 듀', value: 30,
		icon: 'dist/img/d3/mountaindew.png',
		desc: `
			A Node.js-based developer web server for quickly test apps and web pages with some
			magic of 'auto-reload' on the browser.
		`
	}];


let svg = d3.select('svg');
let width = document.body.clientWidth; // get width in pixels
let height = +svg.attr('height');
let centerX = width * 0.5;
let centerY = height * 0.5;
let strength = 0.05;
let focusedNode;
		
let format = d3.format(',d');

let scaleColor = d3.scaleOrdinal(d3.schemeCategory20);

// use pack to calculate radius of the circle
let pack = d3.pack()
	.size([width , height ])
	.padding(1.5);

let forceCollide = d3.forceCollide(d => d.r + 1);

// use the force
let simulation = d3.forceSimulation()
	// .force('link', d3.forceLink().id(d => d.id))
	.force('charge', d3.forceManyBody())
	.force('collide', forceCollide)
	// .force('center', d3.forceCenter(centerX, centerY))
	.force('x', d3.forceX(centerX ).strength(strength))
	.force('y', d3.forceY(centerY ).strength(strength));

// reduce number of circles on mobile screen due to slow computation
if ('matchMedia' in window && window.matchMedia('(max-device-width: 767px)').matches) {
	data = data.filter(el => {
		return el.value >= 50;
		});
	}

let root = d3.hierarchy({ children: data })
	.sum(d => d.value);

// we use pack() to automatically calculate radius conveniently only
// and get only the leaves
let nodes = pack(root).leaves().map(node => {
	console.log('node:', node.x, (node.x - centerX) * 2);
	const data = node.data;
	return {
		x: centerX + (node.x - centerX) * 2.5, // magnify start position to have transition to center movement
		y: centerY + (node.y - centerY) * 2.5,
		r: 0, // for tweening
		radius: node.r, //original radius
		id: data.cat + '.' + (data.name.replace(/\s/g, '-')),
		cat: data.cat,
		name: data.name,
		value: data.value,
		icon: data.icon,
		desc: data.desc,
	}
});
simulation.nodes(nodes).on('tick', ticked);

svg.style('background-color', '#eee');
let node = svg.selectAll('.node')
	.data(nodes)
	.enter().append('g')
	.attr('class', 'node')
	.call(d3.drag()
		.on('start', (d) => {
			if (!d3.event.active) simulation.alphaTarget(0.2).restart();
			d.fx = d.x;
			d.fy = d.y;
		})
		.on('drag', (d) => {
			d.fx = d3.event.x;
			d.fy = d3.event.y;
		})
		.on('end', (d) => {
			if (!d3.event.active) simulation.alphaTarget(0);
			d.fx = null;
			d.fy = null;
		}));

node.append('circle')
	.attr('id', d => d.id)
	.attr('r', 0)
	.style('fill', d => scaleColor(d.cat))
	.transition().duration(2000).ease(d3.easeElasticOut)
		.tween('circleIn', (d) => {
			let i = d3.interpolateNumber(0, d.radius);
			return (t) => {
					d.r = i(t);
				simulation.force('collide', forceCollide);
		}
	})

node.append('clipPath')
	.attr('id', d => `clip-${d.id}`)
	.append('use')
	.attr('xlink:href', d => `#${d.id}`);

// display text as circle icon
node.filter(d => !String(d.icon).includes('img/'))
	.append('text')
	.classed('node-icon', true)
	.attr('clip-path', d => `url(#clip-${d.id})`)
	.selectAll('tspan')
	.data(d => d.icon.split(';'))
	.enter()
		.append('tspan')
		.attr('x', 0)
		.attr('y', (d, i, nodes) => (13 + (i - nodes.length / 2 - 0.5) * 10))
		.text(name => name);

// display image as circle icon
node.filter(d => String(d.icon).includes('img/'))
		.append('image')
		.classed('node-icon', true)
		.attr('clip-path', d => `url(#clip-${d.id})`)
		.attr('xlink:href', d => d.icon)
		.attr('x', d => - d.radius * 0.7)
		.attr('y', d => - d.radius * 0.7)
		.attr('height', d => d.radius * 2 * 0.7)
		.attr('width', d => d.radius * 2 * 0.7)
		
node.append('title')
		.text(d => (d.cat + '::' + d.name + '\n' + format(d.value)));

let legendOrdinal = d3.legendColor()
		.scale(scaleColor)
		.shape('circle');
		
let legend = svg.append('g')
		.classed('legend-color', true)
		.attr('text-anchor', 'start')
		.attr('transform','translate(20,30)')
		.style('font-size','12px')
		.call(legendOrdinal);

let sizeScale = d3.scaleOrdinal()
		.domain(['less use', 'more use'])
		.range([5, 10] );

let legendSize = d3.legendSize()
		.scale(sizeScale)
		.shape('circle')
		.shapePadding(10)
		.labelAlign('end');

let legend2 = svg.append('g')
		.classed('legend-size', true)
		.attr('text-anchor', 'start')
		.attr('transform', 'translate(150, 25)')
		.style('font-size', '12px')
		.call(legendSize);


		/*
		<foreignObject class="circle-overlay" x="10" y="10" width="100" height="150">
			<div class="circle-overlay__inner">
				<h2 class="circle-overlay__title">ReactJS</h2>
				<p class="circle-overlay__body">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, sunt, aspernatur. Autem repudiandae, laboriosam. Nulla quidem nihil aperiam dolorem repellendus pariatur, quaerat sed eligendi inventore ipsa natus fugiat soluta doloremque!</p>
			</div>
		</foreignObject>
		*/
let infoBox = node.append('foreignObject')
		.classed('circle-overlay hidden', true)
		.attr('x', -250 * 0.5 * 0.8)
		.attr('y', -250 * 0.5 * 0.8)
		.attr('height', 250 * 0.8)
		.attr('width', 250 * 0.8)
			.append('xhtml:div')
			.classed('circle-overlay__inner', true);

infoBox.append('h2')
		.classed('circle-overlay__title', true)
		.text(d => d.name);


infoBox.append('p')
		.classed('circle-overlay__body', true)
		.html(d => d.desc);


node.on('click', (currentNode) => {
		d3.event.stopPropagation();
		console.log('currentNode', currentNode);
		let currentTarget = d3.event.currentTarget; // the <g> el

		if (currentNode === focusedNode) {
			// no focusedNode or same focused node is clicked
			return;
		}
		let lastNode = focusedNode;
		focusedNode = currentNode;

		simulation.alphaTarget(0.2).restart();
		// hide all circle-overlay
		d3.selectAll('.circle-overlay').classed('hidden', true);
		d3.selectAll('.node-icon').classed('node-icon--faded', false);

		// don't fix last node to center anymore
		if (lastNode) {
			lastNode.fx = null;
			lastNode.fy = null;
			node.filter((d, i) => i === lastNode.index)
				.transition().duration(2000).ease(d3.easePolyOut)
				.tween('circleOut', () => {
					let irl = d3.interpolateNumber(lastNode.r, lastNode.radius);
					return (t) => {
						lastNode.r = irl(t);
					}
				})
				.on('interrupt', () => {
					lastNode.r = lastNode.radius;
				});
		}

	// if (!d3.event.active) simulation.alphaTarget(0.5).restart();

		d3.transition().duration(2000).ease(d3.easePolyOut)
			.tween('moveIn', () => {
				console.log('tweenMoveIn', currentNode);
				let ix = d3.interpolateNumber(currentNode.x, centerX);
				let iy = d3.interpolateNumber(currentNode.y, centerY);
				let ir = d3.interpolateNumber(currentNode.r, centerY * 0.5);
				return function (t) {
					// console.log('i', ix(t), iy(t));
					currentNode.fx = ix(t);
					currentNode.fy = iy(t);
					currentNode.r = ir(t);
					simulation.force('collide', forceCollide);
				};
			})
			.on('end', () => {
				simulation.alphaTarget(0);
				let $currentGroup = d3.select(currentTarget);
				$currentGroup.select('.circle-overlay')
						.classed('hidden', false);
				$currentGroup.select('.node-icon')
						.classed('node-icon--faded', true);
			})
			.on('interrupt', () => {
					console.log('move interrupt', currentNode);
					currentNode.fx = null;
					currentNode.fy = null;
					simulation.alphaTarget(0);
			});
});

// blur
d3.select(document).on('click', () => {
		let target = d3.event.target;
		// check if click on document but not on the circle overlay
		if (!target.closest('#circle-overlay') && focusedNode) {
				focusedNode.fx = null;
				focusedNode.fy = null;
				simulation.alphaTarget(0.2).restart();
				d3.transition().duration(2000).ease(d3.easePolyOut)
					.tween('moveOut', function () {
						console.log('tweenMoveOut', focusedNode);
						let ir = d3.interpolateNumber(focusedNode.r, focusedNode.radius);
						return function (t) {
							focusedNode.r = ir(t);
							simulation.force('collide', forceCollide);
						};
					})
					.on('end', () => {
						focusedNode = null;
						simulation.alphaTarget(0);
					})
					.on('interrupt', () => {
						simulation.alphaTarget(0);
					});

				// hide all circle-overlay
				d3.selectAll('.circle-overlay').classed('hidden', true);
				d3.selectAll('.node-icon').classed('node-icon--faded', false);
		}
});

function ticked() {
		node
			.attr('transform', d => `translate(${d.x},${d.y})`)
			.select('circle')
				.attr('r', d => d.r);
}