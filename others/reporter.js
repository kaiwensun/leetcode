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
		// AC'ed in anonymous session
		const otherSession = [
			4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
			16, 18, 21, 24, 25, 26, 31, 34, 36, 38,
			39, 40, 46, 47, 51, 52, 54, 56, 57, 58,
			59, 61, 63, 68, 69, 71, 73, 74, 77, 82,
			83, 86, 98, 101, 102, 104, 105, 110, 111, 112,
			113, 118, 135, 138, 139, 141, 145, 153, 160, 165,
			167, 175, 181, 182, 183, 189, 191, 198, 205, 206,
			209, 216, 218, 223, 225, 228, 232, 233, 234, 235,
			236, 240, 241, 242, 257, 273, 289, 290, 292, 303,
			312, 316, 318, 319, 322, 331, 343, 349, 350, 375,
			376, 377, 378, 388, 394, 397, 398, 404, 414, 415,
			419, 433, 447, 458];
		if (otherSession.includes(this._id)) {
			this._status = "ac";
		}
		if (this._title == "Most Visited Sector in  a Circular Track") {
			this._title = "Most Visited Sector in a Circular Track";
		}
		if (this._title == "Longest Uncommon Subsequence I ") {
			this._title = "Longest Uncommon Subsequence I";
		}
	}
	
	this._id = parseInt(item.children[1].textContent);
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
