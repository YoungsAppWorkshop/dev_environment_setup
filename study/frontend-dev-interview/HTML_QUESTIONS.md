# HTML Questions



### Q. What does a `doctype` do?

### A.
In HTML, the doctype is the required `<!DOCTYPE html>` preamble found at the top of all documents. Its sole purpose is to prevent a browser from switching into so-called "quirks mode" when rendering a document; that is, the `<!DOCTYPE html>` doctype ensures that the browser makes a best-effort attempt at following the relevant specifications, rather than using a different rendering mode that is incompatible with some specifications.


### Q. What are `data-` attributes good for?

### A.
`data-*` attributes allow us to store extra information on standard, semantic HTML elements without other hacks such as non-standard attributes, extra properties on DOM, or `Node.setUserData()`.


### Q. Consider HTML5 as an open web platform. What are the building blocks of HTML5?

### A.

* Semantics: allowing you to describe more precisely what your content is.
* Connectivity: allowing you to communicate with the server in new and innovative ways.
* Offline and storage: allowing webpages to store data on the client-side locally and operate offline more efficiently.
* Multimedia: making video and audio first-class citizens in the Open Web.
* 2D/3D graphics and effects: allowing a much more diverse range of presentation options.
* Performance and integration: providing greater speed optimization and better usage of computer hardware.
* Device access: allowing for the usage of various input and output devices.
Styling: letting authors write more sophisticated themes.


### Q. Describe the difference between a cookie, sessionStorage and localStorage.

### A.

* Cookies:
  - An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. The browser may store it and send it back with the next request to the same server. Typically, it's used to tell if two requests came from the same browser — keeping a user logged-in, for example. It remembers stateful information for the stateless HTTP protocol.
  - The data is sent back to the server for every HTTP request (HTML, images, JavaScript, CSS, etc) - increasing the amount of traffic between client and server.
  - We can set the expiration time for each cookie
  - The 4K limit is for the entire cookie, including name, value, expiry date etc. To support most browsers, keep the name under 4000 bytes, and the overall cookie size under 4093 bytes.
  - Vulnerable to CSRF attack

The Web Storage API provides mechanisms by which browsers can store key/value pairs, in a much more intuitive fashion than using cookies.

* LocalStorage:
  - The data stored in localStorage persists until explicitly deleted. Changes made are saved and available for all current and future visits to the site.
  - The data is not sent back to the server for every HTTP request (HTML, images, JavaScript, CSS, etc) - reducing the amount of traffic between client and server.
  - Web storage can be viewed simplistically as an improvement on cookies, providing much greater storage capacity. Available size is 5MB which considerably more space to work with than a typical 4KB cookie.
  - It works on same-origin policy. So, data stored will only be available on the same origin.
  - Vulnerable to XSS attack


* sessionStorage:
  - It is similar to localStorage. Changes are only available per window (or tab in browsers like Chrome and Firefox). Changes made are saved and available for the current page, as well as future visits to the site on the same window. Once the window is closed, the storage is deleted
  - The data is available only inside the window/tab in which it was set.
  - The data is not persistent i.e. it will be lost once the window/tab is closed. Like localStorage, it works on same-origin policy. So, data stored will only be available on the same origin.
  - Vulnerable to XSS attack


### Q. Describe the difference between `<script>`, `<script async>` and `<script defer>`.

### A.
`<script>`
* This is the default behavior of the `<script>` element. Parsing of the HTML code pauses while the script is executing. For slow servers and heavy scripts this means that displaying the webpage will be delayed.
* HTML parsing paused while fetching/executing script.

`<script async>`
* The HTML parser does not need to pause at the point it reaches the script tag to fetch and execute, the execution can happen whenever the script becomes ready after being fetched in parallel with the document parsing.
* Async is more useful when you really don't care when the script loads and nothing else that is user dependent depends upon that script loading. The most often cited example for using async is an analytics script like Google Analytics

`<script defer>`
* The defer attribute tells the browser to only execute the script file once the HTML document has been fully parsed.
* If your second script depends upon the first script (e.g. your second script uses the jQuery loaded in the first script), then you can't make them async without additional code to control execution order, but you can make them defer because defer scripts will still be executed in order, just not until after the document has been parsed.

Asynchronous and deferred execution of scripts are more important when the `<script>` element is not located at the very end of the document.


### Q. Why is it generally a good idea to position CSS `<link>`s between `<head></head>` and JS `<script>` just before `</body>`? Do you know any exceptions?

### A.
It is recommended because when you have the CSS declared before `<body>` starts, your styles has actually loaded already. So very quickly users see something appear on their screen (e.g. background colors). If not, users see blank screen for some time before the CSS reaches the user.

Also, if you leave the the styles somewhere in the `<body>`, the browser has to re-render the page (new and old when loading) when the styles declared has been parsed.

JavaScript is considered a "parser blocking resource". This means that the parsing of the HTML document itself is blocked by JavaScript.


### Q. Why you would use a `srcset` attribute in an image tag? Explain the process the browser uses when evaluating the content of this attribute.

### A.
You would use the `srcset` attribute when you want to serve different images to users depending on their device display width – serve higher quality images to devices with retina display enhances the user experience while serving lower resolution images to low-end devices increase performance and decrease data wastage.

So, with these attributes in place, the browser will:
1. Look at its device width.
2. Work out which media condition in the sizes list is the first one to be true.
3. Look at the slot size given to that media query.
4. Load the image referenced in the srcset list that most closely matches the chosen slot size.


### Q. What is progressive rendering?

### A.
Progressive rendering is the name given to techniques used to render content for display as quickly as possible.

It used to be much more prevalent in the days before broadband internet but it's still useful in modern development as mobile data connections are becoming increasingly popular.

Examples of such techniques :
* Lazy loading of images where (typically) some javascript will load an image when it comes into the browsers viewport instead of loading all images at page load.
* Prioritizing visible content (or above the fold rendering) where you include only the minimum css/content/scripts necessary for the amount of page that would be rendered in the users browser first to display as quickly as possible, you can then use deferred javascript (domready/load) to load in other resources and content.


### Not Completed
* Have you used different HTML templating languages before?
* How do you serve a page with content in multiple languages?
* What kind of things must you be wary of when design or developing for multilingual sites?
