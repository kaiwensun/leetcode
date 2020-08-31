/* Generate Markdown and JSON from https://leetcode.com/problemset/all/ */

function Item(item) {

	this.toMarkdown = function() {
		return `|${this.statusString()}|${this._id}|[${this._title}](${this._link})|${this.lockedString()}|${this._difficulty}|`;
	}
	this.toJSON = function() {
		return {
			"id": this._id,
			"status": this._status,
			"title": this._title,
			"link": this._link,
			"difficulty": this._difficulty,
			"locked": this._locked
		}
	}
	this.statusString = function() {
		if (this._status == "ac") {
			return "&check;";
		} else if (this._status == "notac") {
			return "?";
		} else if (this._status === null) {
			return "";
		} else {
			throw `Unknown status: ${this._status}`;
		}
	}
	this.lockedString = function() {
		if (this._locked) {
			return "&#x1f512;";
		} else {
			return "";
		}
	}
	this.specialTreate = function() {
		// temporarily empty
	}
	
	this._id = item.children[1].textContent;
	this._status = item.children[0].getAttribute("value")
	this._title = item.children[2].getAttribute("value");
	this._link = item.children[2].getElementsByTagName("a")[0].href;
	this._difficulty = item.children[5].textContent;
	this._locked = item.children[2].getElementsByClassName("fa-lock").length !== 0;
	this.specialTreate();
	
	return this;
}

Item.genTableHeader = function() {
	let attributes = ["Status", "#", "Title", "Locked", "Difficulty"];
	let line = `${"|---".repeat(attributes.length)}|`;
	return `|${attributes.join("|")}|\n${line}`;
}

function genMarkdown() {
	let items = $("#question-app .reactable-data > tr").get();
	let tableHeader = Item.genTableHeader();
	let tableContent = items.map(item => new Item(item)).map(item => item.toMarkdown()).join("\n");
	return tableHeader + "\n" + tableContent;
}

function genJSON() {
	let items = $("#question-app .reactable-data > tr").get();
	return items.map(item => new Item(item)).map(item => item.toJSON());
}

function reportMarkdown() {
	let report = genMarkdown();
	console.log(report);
}

function reportJSON() {
	let report = genJSON();
	console.log(JSON.stringify(report));
}
