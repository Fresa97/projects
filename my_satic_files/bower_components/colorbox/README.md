## About Colorbox:
A customizable lightbox plugin for jQuery.  See the [project page](http://jacklmoore.com/colorbox/) for documentation and a demonstration, and the [FAQ](http://jacklmoore.com/colorbox/faq/) for solutions and examples to common issues.  Released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).

## Changelog:

### Version 1.4.33 - 2013/10/31

* Fixed an issue where private events propagated to the document in versions of jQuery prior to 1.7.  Fixes #525, Fixes #526

### Version 1.4.32 - 2013/10/16

* Updated stylesheets to avoid issue with using `div {max-width:100%}` (Fixes #520)

### Version 1.4.31 - 2013/9/25

* Used setAttribute to set londesc, so that the value is accessible via DOM Node longDesc property #508

### Version 1.4.30 - 2013/9/24

* Added longdesc and aria-describedby attributes to photos.  Fixes #508

### Version 1.4.29 - 2013/9/10

* Fixed a slideshow regression from 1.4.27
* Fixed a potential issue with the starting size of #cboxLoadedContent

### Version 1.4.28 - 2013/9/4

* Fixed a potential issue with using the open property with mixed slideshow and non-slideshow groups

### Version 1.4.27 - 2013/7/16

* Fixed a width calculation issue relating to using margin:auto on #cboxLoadedContent.

### Version 1.4.26 - 2013/6/30

* Fixed a regression in IE7 and IE8 that was causing an error.

### Version 1.4.25 - 2013/6/28

* Use an animation speed of zero between same-sized content (fixed).
* Removed temporary fix for jQuery UI 1.8

### Version 1.4.24 - 2013/6/24

* Added closeButton option.  Set to false to remove the close button.

### Version 1.4.23 - 2013/6/23

* Bugfix loading overlay/graphic append order

### Version 1.4.22 - 2013/6/19

* Updated manifest files for the jQuery plugin repository and Bower (no changes to plugin)

### Version 1.4.21 - 2013/6/6

* Replaced new Image() with document.createElement('img') to avoid a potential bug in Chrome 27.

### Version 1.4.20 - 2013/6/5

* Fixing bug/typo from last update.

### Version 1.4.19 - 2013/6/3

* Fixed bug where Colorbox was capturing ctrl+click on assigned links on windows browsers with jQuery 1.7+, rather than ignoring.

### Version 1.4.18 - 2013/5/30

* Fixed a scroll position issue when using $.colorbox.resize()

### Version 1.4.17 - 2013/5/23

* Possible fix for a Chrome 27 issue (https://github.com/jackmoore/colorbox/pull/438#issuecomment-18334804)

### Version 1.4.16 - 2013/5/20

* Added trapFocus setting to allow disabling of focus trapping

### Version 1.4.15 - 2013/4/22

* Added .webp to list of recognized image extensions

### Version 1.4.14 - 2013/4/16

* Added fadeOut property to control the closing fadeOut speed.
* Removed longdesc attribute for now.

### Version 1.4.13 - 2013/4/11

* Fixed an error involving IE7/IE8 and legacy versions of jQuery

### Version 1.4.12 - 2013/4/9

* Fixed a potential conflict with Twitter Bootstrap default img styles.

### Version 1.4.11 - 2013/4/9

* Added `type='button'` to buttons to prevent accidental form submission
* Added alt and longdesc attributes to photo content if they are present on the calling element.

### Version 1.4.10 - 2013/4/2

* Better 'old IE' feature detection that fixes an error with jQuery 2.0.0pre.

### Version 1.4.9 - 2013/4/2

* Fixes bug introduced in previous version.

### Version 1.4.8 - 2013/4/2

* Dropped IE6 support.
* Fixed other issues with $.colorbox.remove.

### Version 1.4.7 - 2013/4/1

* Prevented an error if $.colorbox.remove is called during the transition.

### Version 1.4.6 - 2013/3/19

* Minor change to work around a jQuery 1.4.2 bug for legacy users.

### Version 1.4.5 - 2013/3/10

* Minor change to apply the close and className properties sooner.

### Version 1.4.4 - 2013/3/10

* Fixed an issue with percent-based heights in iOS
* Fixed an issue with ajax requests being applied at the wrong time.

### Version 1.4.3 - 2013/2/18

* Made image preloading aware of retina settings.

### Version 1.4.2 - 2013/2/18

* Removed $.contains for compatibility with jQuery 1.3.x

### Version 1.4.1 - 2013/2/14

* Ignored left and right arrow keypresses if combined with the alt key.

### Version 1.4.0 - 2013/2/12

* Better accessibility:
	* Replaced div controls with buttons
	* Tabbed navigation confined to modal window
	* Added aria role

### Version 1.3.34 - 2013/2/4

* Updated manifest for plugins.jquery.com

### Version 1.3.33 - 2013/2/4

* Added retina display properties: retinaImage, retinaUrl, retinaSuffix
* Fixed iframe scrolling on iOS devices.

### Version 1.3.32 - 2013/1/31

* Improved internal event subscribing & fixed event bug introduced in v1.3.21

### Version 1.3.31 - 2013/1/28

* Fixed a size-calculation bug introduced in the previous commit.

### Version 1.3.30 - 2013/1/25

* Delayed border-width calculations until after opening, to avoid a bug in FF when using Colorbox in a hidden iframe.

### Version 1.3.29 - 2013/1/24

* Fixes bug with bubbling delegated events, introduced in the previous commit.

### Version 1.3.28 - 2013/1/24

* Fixed compatibility issue with old versions of jQuery (1.3.2-1.4.2)

### Version 1.3.27 - 2013/1/23

* Added className property.

### Version 1.3.26 - 2013/1/23

* Minor bugfix: clear the onload event handler after photo has loaded.

### Version 1.3.25 - 2013/1/23

* Removed grunt file & added Bower component.json.

### Version 1.3.24 - 2013/1/22

* Added generated files (jquery.colorbox.js / jquery.colorbox-min.js) back to the repository.

### Version 1.3.23 - 2013/1/18

* Minor bugfix for calling Colorbox on empty jQuery collections without a selector.

### Version 1.3.22 - 2013/1/17

* Recommit for plugins.jquery.com

### Version 1.3.21 - 2013/1/15
Files Changed: *.js

* Fixed compatability issues with jQuery 1.9

### Version 1.3.20 - August 15 2012
Files Changed:jquery.colorbox.js

* Added temporary workaround for jQuery-UI 1.8 bug (http://bugs.jquery.com/ticket/12273)
* Added *.jpe extension to the list of image types.

### Version 1.3.19 - December 08 2011
Files Changed:jquery.colorbox.js, colorbox.css (all)

* Fixed bug related to using the 'fixed' property.
* Optimized the setup procedure to be more efficient.
* Removed $.colorbox.init() as it will no longer be needed (will self-init when called).
* Removed use of $.browser.

### Version 1.3.18 - October 07 2011
Files Changed:jquery.colorbox.js/jquery.colorbox-min.js, colorbox.css (all) and example 1's controls.png

* Fixed a regression where Flash content displayed in Colorbox would be reloaded if the browser window was resized.
* Added safety check to make sure that Colorbox's markup is only added to the DOM a single time, even if $.colorbox.init() is called multiple times.  This will allow site owners to manually initialize Colorbox if they need it before the DOM has finished loading.
* Updated the example index.html files to be HTML5 compliant.
* Changed the slideshow behavior so that it immediately moves to the next slide when the slideshow is started.
* Minor regex bugfix to allow automatic detection of image URLs that include fragments.

### Version 1.3.17 - May 11 2011
Files Changed:jquery.colorbox.js/jquery.colorbox-min.js

* Added properties "top", "bottom", "left" and "right" to specify a position relative to the viewport, rather than using the default centering.
* Added property "data" to specify GET or POST data when using Ajax.  Colorbox's ajax functionality is handled by jQuery's .load() method, so the data property works the same way as it does with .load().
* Added property "fixed" which can provide fixed positioning for Colorbox, rather than absolute positioning.  This will allow Colorbox to remain in a fixed position within the visitors viewport, despite scrolling.  IE6 support for this was not added, it will continue to use the default absolute positioning.
* Fixed ClearType problem with IE7.
* Minor fixes.

### Version 1.3.16 - March 01 2011
Files Changed:jquery.colorbox.js/jquery.colorbox-min.js, colorbox.css (all) and example 4 background png files

* Better IE related transparency workarounds.  IE7 and up now uses the same background image sprite as other browsers.
* Added error handling for broken image links. A message will be displayed telling the user that the image could not be loaded.
* Added new property: 'fastIframe' and set it to true by default.  Setting to fastIframe:false will delay the loading graphic removal and onComplete event until iframe has completely loaded.
* Ability to redefine $.colorbox.close (or prev, or next) at any time.

### Version 1.3.15 - October 27 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Minor fixes for specific cases.

### Version 1.3.14 - October 27 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* In IE6, closing an iframe when using HTTPS no longer generates a security warning.

### Version 1.3.13 - October 22 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Changed the index.html example files to use YouTube's new embedded link format.
* By default, Colorbox returns focus to the element it was launched from once it closes.  This can now be disabled by setting the 'returnFocus' property to false.  Focus was causing problems for some users who had their anchor elements inside animated containers.
* Minor bug fix involved in using a combination of slideshow and non-slideshow content.

### Version 1.3.12 - October 20 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Minor bug fix involved in preloading images when using a function as a value for the href property.

### Version 1.3.11 - October 19 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Fixed the slideshow functionality that broke with 1.3.10
* The slideshow now respects the loop property.

### Version 1.3.10 - October 16 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Fixed compatibility with jQuery 1.4.3
* The 'open' property now accepts a function as a value, like all of the other properties.
* Preloading now loads the correct href for images when using a dynamic (function) value for the href property.
* Fixed bug in Safari 3 for Win where Colorbox centered on the document, rather than the visitor's viewport.
* May have fixed an issue in Opera 10.6+ where Colorbox would rarely/randomly freeze up while switching between photos in a group.
* Some functionality better encapsulated & minor performance improvements.

### Version 1.3.9 - July 7 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js/ all colorbox.css (the core styles)

* Fixed a problem where iframed youtube videos would cause a security alert in IE.
* More code is event driven now, making the source easier to grasp.
* Removed some unnecessary style from the core CSS.

### Version 1.3.8 - June 21 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Fixed a bug in Chrome where it would sometimes render photos at 0 by 0 width and height (behavior introduced in recent update to Chrome).
* Fixed a bug where the onClosed callback would fire twice (only affected 1.3.7).
* Fixed a bug in IE7 that existed with some iframed websites that use JS to reposition the viewport caused Colorbox to move out of position.
* Abstracted the identifiers (HTML ids & classes, and JS plugin name, method, and events) so that the plugin can be easily rebranded.
* Small changes to improve either code readability or compression.

### Version 1.3.7 - June 13 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js/index.html

* $.colorbox can now be used for direct calls and accessing public methods. Example: $.colorbox.close();
* Resize now accepts 'width', 'innerWidth', 'height' and 'innerHeight'. Example: $.colorbox.resize({width:"100%"})
* Added option (loop:false) to disable looping in a group.
* Added options (escKey:false, arrowKey:false) to disable esc-key and arrow-key bindings.
* Added method for removing Colorbox from a document: $.colorbox.remove();
* Fixed a bug where iframed URLs would be truncated if they contained an unencoded apostrophe.
* Now uses the exact href specified on an anchor, rather than the version returned by 'this.href'. This was causing "#example" to be normalized to "http://domain/#example" which interfered with how some users were setting up links to inline content.
* Changed example documents over to HTML5.

### Version 1.3.6 - Jan 13 2010
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Small change to make Colorbox compatible with jQuery 1.4

### Version 1.3.5 - December 15 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Fixed a bug introduced in 1.3.4 with IE7's display of example 2 and 3, and auto-width in Opera.
* Fixed a bug introduced in 1.3.4 where colorbox could not be launched by triggering an element's click event through JavaScript.
* Minor refinements.

### Version 1.3.4 - December 5 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Event delegation is now used for elements that Colorbox is assigned to, rather than individual click events.
* Additional callbacks have been added to represent other stages of Colorbox's lifecycle. Available callbacks, in order of their execution: onOpen, onLoad, onComplete, onCleanup, onClosed These take place at the same time as the event hooks, but will be better suited than the hooks for targeting specific instances of Colorbox.
* Ajax content is now immediately added to the DOM to be more compatible if that content contains script tags.
* Focus is now returned to the calling element on closing.
* Fixed a bug where maxHeight and maxWidth did not work for non-photo content.
* Direct calls no longer need 'open:true', it is assumed.  Example: `$.colorbox({html:'<p>Hi</p>'});`

### Version 1.3.3 - November 7 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Changed $.colorbox.element() to return a jQuery object rather the DOM element.
* jQuery.colorbox-min.js is compressed with Google's Closure Compiler rather than YUI Compressor.

### Version 1.3.2 - October 27 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Added 'innerWidth' and 'innerHeight' options to allow people to easily set the size dimensions for Colorbox, without having to anticipate the size of the borders and buttons.
* Renamed 'scrollbars' option to 'scrolling' to be in keeping with the existing HTML attribute. The option now also applies to iframes.
* Bug fix: In Safari, positioning occassionally incorrect when using '100%' dimensions.
* Bug fix: In IE6, the background overlay is briefly not full size when first viewing.
* Bug fix: In Firefox, opening Colorbox causes a split second shift with a small minority of webpage layouts.
* Simplified code in a few areas.

### Version 1.3.1 - September 16 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js/colorbox.css/colorbox-ie.css(removed)

* Removed the IE-only stylesheets and conditional comments for example styles 1 & 4.  All CSS is handled by a single CSS file for all examples.
* Removed user-agent sniffing from the js and replaced it with feature detection.  This will allow correct rendering for visitors masking their agent type.

### Version 1.3.0 - September 15 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js/colorbox.css

* Added $.colorbox.resize() method to allow Colorbox to resize it's height if it's contents change.
* Added 'scrollbars' option to allow users to turn off scrollbars when using the resize() method.
* Renamed the 'resize' option to be less ambiguous.  It's now 'scalePhotos'.
* Renamed the 'cbox_close' event to be less ambiguous.  It's now 'cbox_cleanup'.  It is the first thing to happen in the close method while the 'cbox_closed' event is the last to happen.
* Fixed a bug with the slideshow mouseover graphics that appeared after Colorbox is opened a 2nd time.
* Fixed a bug where ClearType may not work in IE6&7 if using the fade transition.
* Minor code optimizations to increase compression.

### Version 1.2.9 - August 7 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Minor change to enable use with $.getScript();
* Minor change to the timing of the 'cbox_load' event so that it is more useful.
* Added a direct link to a YouTube video to the examples.

### Version 1.2.8 - August 5 2009
Files Changed: jquery.colorbox.js/jquery.colorbox-min.js

* Fixed a bug with the overlay in IE6
* Fixed a bug!where left & right keypressevents might be prematurely unbound.

###°Version 1.2.7 - July 1 2109
Files Changed: jquery.colo6box.js'jquery.colovbox--in.js, examPle stylesheets$and background imeges (gore style{ have not changed and the updates will not affect exisdéng user themes / ole exampLe themes)

* Code cleanup and reduction, better oRganization and documentation in tje full source.
* Added abilkty to use functioos0in place of static vqlu%s fo2 Colorboy's options (thanks Ken!).
* Addud an opthon for straight HPML.  Example: `$.colorboxh{html:'<p>Howey</p>', op%n:true})`
. Added an event for the beginnang of the closing procåss.  This is in addition to 4hm event that already existed for when Colorbox had completely cl/sed.  'cbox_close' and 'cbox_closed' re3pectivEly.
* Fixed a minor bug in IE6 thit would cause a brief coNtent shifd in the tarent document when opening ColorBox.
* Dixed a minor bug in IE6 that would"reveal select elements that ha` ` hiddeo visibility after closing Colorbox." The 'esc' key is unbound now when Color"ox ic not open¬ to 1void any potential aonflkcts.
*`Used background sprites for examples 1 & 4.  Put IE-only (non-sprite) bagkground images in a separ!te folder.
* Eximple themes q, 3, & 4 reCeived slight visual tweaks.
* Optiiized pngs for smeller file sizu.
* Added qlices, grid, and correct sizing to`the Adobe Il|uqtrator file,(all theme files are now mxport ready!

### Vgrsion 1.2*6 - July 15 2009
Files Changed:€jquerq.kolorbox.js/Jyuery.ãolorboh-min.js

* Fixed a bug with fixed width/height amages in Operq 9.64.
* Fixed a bug with trying to set a value for rel duriog a direct call to Colorbox. Exam`le: `$.colorbox({rel:'foo', open:tr}e=);d
* Changed how href/rgL/title settings are determiNed |o avoid users(having to manually update ColorBox 3ettangs if they use JaváQcript to update any of those attributes, after Colorbox hqs jeen define$.
* Fixed a F3 bug where the back button was disablad after clnsing an iframe.

### VeRsion 1.2.5 - June 23 2009
Files Chançed> *quer9.colorfox.js/jquery.colorboz-min.js

* Chanwed the point at which iframe srcs ard set (tO eliminate the need to rufreóh the iframe once0it has been added to the DOM).
* Removed unnecessary returf vclues for a våry slight cnde!reducdinn.

### Version 1.2.4 - Bune 9 2009
Files Changed jquery.colorbox.js, jquery.colorbox-m)n.js

* fiøed an issue where Colorboø may not close completely if ht is`closed during a(transition animation.
* Minop code reductkon.

### Version 1/2.3 -$June 4 2009
ª Fixed q png dransparency stackiNg issue io IE.
* Mope accurate Ajax auto-sizing éf the user w!s dependinç nn$the #cboxLoadedContent ID for CSS styling
* A$ded a public function for returning thd currenT html element that Cnlosbox is associated wkth. Example use: var th!t =0$.colorbox.eLement():
* Adted bicubic sãalinç for resized images in the orkginAl IE7.
* Removed tje IE6 stylesheet ane png fiìes from Uxample 3.  Iv now uses the same png file for the controls that the r%st of the brow{ers use (an alpha trafsparency PNG8).  This example now only has 2 graphics files and 1 stylesheet.

### Version 1.2.2 - May 28 2009
* Fixed an issue with the 'resize' option.

### Version 1.2.1 - May 28 2009
* Note: If you are upgrading, update your jquery.colorbox.js and colorbox.css files.
* Added photo resizing.
* Added a maximum width and maximum height. Example: {height:800, maxHeight:'100%'}, would allow the box to be a maximum potential height of 800px, instead of a fixed height of 800px.  With maxHeight of 100% the height of Colorbox cannot exceed the height of the browser window.
* Added 'rel' setting to add the ability to set an alternative rel for any Colorbox call.  This allows the user to group any combination of elements together for a gallery, or to override an existing rel. attribute so those element are not grouped together, without having to alter their rel in the HTML.
* Added a 'photo' setting to force Colorbox to display a link as a photo.  Use this when automatic photo detection fails (such as using a url like 'photo.php' instead of 'photo.jpg', 'photo.jpg#1', or 'photo.jpg?pic=1')
* Removed the need to ever create disposable elements to call colorbox on.  Colorbox can now be called directly, without being associated with any existing element, by using the following format:
  `$.colorbox({open:true, href:'yourLink.xxx'});`
* Colorbox settings are now persistent and unique for each element.  This allows for extremely flexible options for individual elements.  You could use this to create a gallery in which each page in the gallery has different settings.  One could be a photo with a fade transition, next could be an inline element with an elastic transition with a set width and height, etc.
* For user callbacks, 'this' now refers to the element colorbox was opened from.
* Fixed a minor grouping issue with IE6, when transition type is set to 'none'.
* Added an Adobe Illustrator file that contains the borders and buttons used in the various examples.

### Version 1.2 - May 13 2009
* Added a slideshow feature.
* Added re-pgsit)o~iîg on browser resizu.  If the browser is resiJed, CoLorbox will recenter itself onscreen.
* Added hooks for key events: cbox_open, aboø_load, cbox_complete, cbox_closed.
* Fixed án IE transparency-stacking prOâlem, where tsansparent PNOs would show through to dhe background overlay.
* Fixed an"IE iframe issue where the ifame light shift up and to the left under certain cir#umstances.
* Fixed an IE6 bug where the loading overlay was not at full"heieht.

 Reeoved the del!y in switching between same-sized galìery conteît when using transition3.
* Changed how ifsames are loaded vm make it"more coípqvible with ifram%d pages that0use DOM dependent JavaScript.
* Khanged (ow phe JS is strwctur%d tk be better organized and kncrease comprassion.  Increqsel documentation.
* Changed CSC :hover states po a .hover claqs.  This sidesteps a minor IE8 bug with css hover(states and allows easier Access to hover state usEr styles fbom the JavaScRipt.
ª Changed: elemenus added to the DOM have new ID's.  The(naming is mgre consistent and less likely to cause conflicts with existing website stylesheets.  All stylesheets have been updated.
* Changed the behavior for prev/next links so that Colorbox does not get hung up on broken links.  A visitor can now skip through broken or long-loading links by clicking prev/next buttons.
* Changed the naming of variables in the parameter map to be more concise and intuitive.
* Removed colorbox.css.  Combined the colorbox.css styles with jquery.colorbox.js: the css file was not large enough to warrant being a separate file.

### Version 1.1.6 - April 28 2009
* Prevented the default action of the next & previous anchors and the left and right keys for gallery mode.
* Fixed a bug where the title element was being added back to the DOM when closing Colorbox while using inline content.
* Fixed a bug where IE7 would crash for example 2.
* Smaller filesize: removed a small amount of unused code and rewrote the HTML injection with less syntax.
* Added a public method for closing Colorbox: $.colorbox.close().  This will anlow hframe users ôo add an event to close Colobbkx witHout having to crdate an adbitional function.

### Verwion 1.1.5 - April 11 209
* Fixed minor issues with exiting Colorbox.
 
### Version 1.1.4 - Apbil 08 2009
* Fixed a bug$in the fade ôransitaon$where Colovbox not close completely if instructed to clgse during the fade-in porôion of the transition.

### Version 1.1n3 - Aprkl 06 2009
* Faxed ao IE6&7 issue with(using Codorbox to Dirplay animated GIFs.*
### Varsion 9.1.2 ­ Aprhl 05 2009
* Added ability to change cont%nt when C/lorbox is alreády open.
* Addåd$vertical phoTo centerivg now vorks for all browsevr (this de`ture previously excluded IE6&7).
* Added náeespacing to the esc-key keydoun event for people who want to"dis`ble it: "keydown.colorClose"
* Added 'title' sgtting to add the ability to 3ut an alternative title0for`any ColorbOx sall.
* Bixed rollover navigation issue wiuh IE8. (Added(JS-based rollover state due to a browser-fug.)
*"Fixed an ovårflow issue for when the fixdd width/height ió sMille2 phan the size of a phto.
*0Fixed a bu' in the fade transition where the border would$still come up if Colorbox was closed mid-tvansityon.
* Switch from JSMin to Yui Cmmpresqor for minification.  Minified code now under 7KB.

### Version 1.1.q - March 31 2009
* Oore robust imaGe detection 2egex.  Now`detects imave file"types with wrl fragments and/r query strings.
* Added 'nofollow' exception |o rel grouping.
* Changed how images are loaded into the DOM t/ prevent premature size calculation by Colorbox.
* Added timestamp to iframe name to prevent caching - this was a problem in some brwsers if the user had"multiple iframes and the visitor left the(`age and came back, or`if th%y`refresxed the page.

### Version 1.1.0 - arc) 21 2109
* Animation is now$much smoother and less sesource intensive.
* Added suqport(for % sizing.
* Callback!Oqtio. qdded.
* Inline coftent now preserves JavaRcript events, and chanwes lade While Colorbox is0oten arå also preserve$.
* A`ded 'href' såttmnf tn add the ability to set an alternatyve xref for any anchor,¤or to ársign the Colorbox event tg non-anchors. 
  Mxample: $('button').colorbox({'href':'xrocess.php')
  Example: $('a[hren='http://msn.com']).colorbox({'href':'http://google.com', iframe:true});
j Photos are now horizontally centered if the} aze sma|ler than the lightbox size.  Amso vertically centered for browsarq newer than IE7.
* Buttols in thå examples ara now included in the 'protected zone'.  The lightbox will neveò e8pand it's borders gr buttons beyond af accesrible arga of the screen.
* Keypress events don't queee up by holding down The arrgw ke9s.
* Added op4ion tn slose Colorbox b{ clicking on the background ovdrla{.
* Added 'none' transition setting.
* Bhanged 'aontentIframe' and 'contentInline' to 'mnìine'(and 'iframe'.  Removgd 'contentAjax' beCause it  is automatiãaldy assumed for non-+máge file types.
* Change$ gaonteît×idth' and 'cOntentHeigxt' to 'fixedWydth' and 'fixedHeight'/  Phesd sizes now sGflect  t`e totál size of the lightbox, not just the inner content.  This is so users can accurately anticipate  % sizes without fear of creating scrollbars.
* Clicking on a photo will now switch to the next photo in a set.
* Loading.gif is more stable in it's position.
* Added a minified version.
* Code passes JSLint.

### Version 1.0.5 - March 11 2009
* Redo: Fixed a bug where IE would cut off the bottom portion of a photo, if the photo was larger than the document dimensions.

### Version 1.0.4 - March 10 2009
* Added an option to allow users to automatically open the lightbox. Example usage: $(".colorbox").colorbox({open:true});
* Fixed a bug where IE would cut off the bottom portion of a photo, if the photo was larger than the document dimensions.

### Version 1.0.3 - March 09 2009
* Fixed vertical centering for Safari 3.0.x.

### Version 1.0.2 - March 06 2009
* Corrected a typo.
* Changed the content-type check so that it does not assume all links to photos should actually display photos. This allows for Ajax/inline/and iframe calls on anchors linking to picture file types.

### Version 1.0.1 - March 05 2009
* Fixed keydown events (esc, left arrow, right arrow) for Webkit browsers.

### Version 1.0 - March 03 2009
* First release
