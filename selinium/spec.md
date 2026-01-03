BATCH EXPORT: SeleniumBase Videos (Python web automation)
Playlist ID: PL-6a317c6a
Generated on: 2026-01-01 13:41:43
============================================================

[1/44] VIDEO: Python Selenium: Fundamentals to Frameworks (with SeleniumBase and live demos!)
URL: https://www.youtube.com/watch?v=EablmOazy-k
------------------------------
(Source: Original Transcript)
All right, hey everybody, and welcome to Python Slenium, Fundamentals to Frameworks, and we'll be using the Slenium-based framework in order to tie everything together on Michael Mintz, and welcome to Chicago.
All right, so a few shout-outs for starting. I'd like to thank the Slenium org. They created Slenium, and of course the conference organizers are doing an awesome job, you know, maintaining everything.
My wife also supports me in a huge way, and she even came out today to watch, and I boss my employer. They support my work, and I use Slenium-based framework all over for their cybersecurity automation stuff.
So yeah, I'm the creator of Slenium-based, and I also lead the automation team at I boss, so I'm going to quickly jump in and talk about what's going on.
So this is the only dedicated Python session at Slenium Comp, so I'll hopefully be holding the Python ecosystem on my shoulders, and you're going to see lots of Python, a lot of live demos, and if the one session is not enough, come see me afterward, there'll be a lot more to come.
So by the end of this presentation, very important, you're going to learn a bunch of things. So Python Slenium fundamentals, we're going to start with the basics, so things that you may not know if you don't use Python at all.
If you're ready to use Python Slenium, then we're going to evolve that into something more advanced, and we'll get to that later. So we're also going to find out how Slenium-based can make Python web automation easier.
All right, so let's move in. The format is a lot of slides, they're going to be GitHub readme files that I'll go through, and of course lots of live demos, some videos with automation, some actual demos, assuming the internet connection does not fail, we can run some real automation on real websites and see how things go.
So it should be exciting for that. So let's start, what does Slenium provide? It's an automation library, and it says so right on the website. It automates browsers, but it does not provide a test framework.
That's where all the other people come in, developers can write test frameworks on top of Slenium to wrap it and make Slenium a lot more powerful than it is on its own.
So how do you get Slenium for your Python user? Well, there's this really cool tool called PIP. If you've downloaded Python or installed it, it's going to be available from the command line, and you can install packages using the PIP installer.
So just do PIP install Slenium, and then all of a sudden you've got the latest version which as of today was 483. So what are some of the building blocks of basic Slenium that you get from installing Slenium?
Well, of course there's importing the library, that is the main line that you want in most of your programs. From Slenium import web driver, you've got that, you've got access to the Slenium library, and all the Slenium methods that go with it.
After that, you can spin up a web browser, and for instance, let's say we're using Chrome, but you can also do automation with any of the other browsers such as Firefox, Edge, even Safari.
So that is the main command, a very simplified version of it for spinning up a web browser.
After that, you've got the driver.get command, which allows you just open any URL on the internet, and in that particular example, your web browser after you've opened Chrome is going to take you to Slenium.dev.
So basic building block will cover the basics so that you know what they are, and then we're going to get a little more advanced.
So here's the command for finding an element, and first you have to specify what type of selector, so you could have an expath or CSS selector.
Normally you would import the buy library and do buy.css selector, but that just translates into that, and then if you're using a CSS selector, you can then specify the CSS selector.
And this is going to find the element and then return a Slenium web element.
Once you have a web element, you can then say element.click as one of many different APIs available to you to say click on that element element.
Let's say you also want to find an element and then type text into it.
Well, there's another method. It's called send keys. So once you've found your element using driver.find element, you can do element.send keys and then the text that you want to type into the text field.
And then another basic command driver.quit, which quits your web driver at the end so that you can free up resources and not have like 100 different browsers open if you keep running the command, but not closing your web browser.
So launching a browser can get a lot more complicated than just web driver dot chrome.
There's lots of different options that you can specify and you can use all the same options that are available from regular Chrome.
So for instance, you can disable notifications, you can add experimental options such as the exclude switches, which lets you like set something else, enable logging, enable automation.
There's hundreds of different options that you can specify and you can even change like say the password manager and not enable that, et cetera, or the credentials enable service.
All these like are built into Chrome. So if you want to take control of a web browser and like change the settings, this is like one way to do that.
And then you do driver equals web driver dot chrome with the additional options that you want to put in.
So that's a typical example of advanced options where you want to do more than just spin up a web browser.
You want to set all the configuration and it uses the browser for that.
So up next test frameworks can wrap Selenium in order to improve things and give you a lot of additional behavior.
So in this particular example, this is right from the Selenium website.
You have a test framework wrapping web driver and then from there you can add additional methods such as driver management.
And there are different tools that can wrap Selenium such as web driver manager and that basically allows you to automatically download your web driver into a special folder so that the tests are ready to go.
Because before you can even start your first test, you need to make sure that you have the driver such as Chrome driver for Chrome, Gecko driver for Firefox, MS edge driver for edge.
And I think with Safari all you have to do is change an option and then you can run your tests on Safari.
So that's where frameworks fit in.
So what are some of the disadvantages of using raw Selenium without additional libraries or frameworks?
Well, the default timeout is zero and a lot of people have probably seen this particular error message before where if something goes wrong, you get a giant stack trace and it's not very pretty.
And you see just a lot of Chrome driver messages that aren't very legible, but this is like a typical thing where you try to just click on an element that isn't fully there yet, you get big stack trace.
So this can be improved on and simplified. A test framework might wrap all that and instead of just throwing a giant message like that, it'll just be like this element with this selector is not visible after 10 seconds of waiting.
So these are just some of the ways that a test framework can improve on the standard Selenium library.
So the commands can get quite long with standard Selenium, for instance, driver.find element, then you have to specify the buy and then put the selector and then dot click if you want to click on a button.
However, there are test frameworks where it's just self dot click and then you put the selector and it will auto detect between CSS selectors and expath because expath and CSS are quite distinguishable.
Like, for instance, if the selector starts with dot slash or slash slash, you're going to know it's like, okay, that's an expath selector because CSS can't do that.
So because there's a difference between CSS selectors and expath selectors, a framework could just auto detect what the selector is and be like, okay, instead of specifying what kind of selector it is, just like immediately click the thing because it knows this is expath and this is CSS.
So that's just a few ways that frameworks can improve on some of the fundamentals. So self dot click is better.
So with raw Selenium, you're not going to get fancy HTML reports, the dashboards, like the special results display, even automatic screenshots.
These are some of the things that test frameworks can build on top of Selenium so that when you run your test suite, all of a sudden you have like a screenshot for every failure instead of just like an error message.
So there are frameworks that already handle this sort of thing.
So here's an example of an HTML report that combines pi test HTML reports with the Selenium based dashboard giving you a pie chart of your tests, stack traces in the logs and of course a screenshot from an xkcd website, essentially saying, like, okay, this is the failure that was here.
It's nice and red and here's the screenshot of the last pager on. So if you have a failing test, it can immediately say, okay, there's a problem here.
Here's the report that you got you clearly see from all the tests that you ran, what went wrong, and it's very clear what you need to fix.
So more things with raw Selenium, it might take a lot more lines of code to perform the same thing that a framework could do with a single line of code.
So for instance, with regular Selenium, you might have to first find the element and then clear out the text field and then do like send keys to like type in text.
So for instance, that is the how to log into the sauce labs of demo website, and then you go into element dot submit, and then that will like do a whole sl, that'll let you log in automatically to the website.
So method like self dot type, where you put in the selector, and then what you want to type in, and then use a backslash end, which will automatically perform a submit action.
You can do all those four lines of code in one line of code with test frameworks, and this particular line is coming from the Selenium based framework.
Basically, a few lines of code or one line of code can perform the same amount as maybe four more lines of code from raw Selenium.
So what else can test frameworks provide? We've got driver management, and you've already seen for at Selenium Comp, there was web driver manager.
Selenium based also has its own driver manager, so it works pretty similarly.
There are also advanced methods such as a certain obroken links, so basically you could have action, it checks all the links, and if any of them return a 404, it will tell you that and be an error inside your report.
You also have test assertions such as self dot assert text, so that you can check whether certain text appears in a selector on a web page, and if it doesn't, then you have a failed assertion.
So this is an example of an advanced assertion that you could have.
You also have additional command line options that you can do, and this is something really huge from regular Selenium.
Remember, you'd have to modify your test if you want to like change which browser you're using.
With a test framework, it might add a PyTest command line option so that you can say, okay, instead of the default browser of Chrome, I want to use Edge, and then I want to add an HTML report on top of that.
All of a sudden, you no longer have to modify your tests every time you want to change a little bit of behavior and change the browser and many other things right from the command line with a lot of these frameworks.
And you've got advanced tools such as test recorders that will generate full scripts for you automatically, similar to the old Selenium IDE, but now a new modern version of that.
Those might also exist within test frameworks, and you have easy to read error messages such as element H2 was not visible after 10 seconds.
Instead of going back before we had a giant long list of Chrome driver stack traces, that was kind of hard to decipher, and you generally make you have to scroll a lot in order to see what went wrong.
So up next, what about test runners? Well, Python is a very powerful programming language, and it has tons of existing test runners available to it.
One of the most popular test runners for Python is the PyTest framework, and it has lots of ways for automatically running tests from the command line where you can specify folder to run all the test from or file,
or even like a regular expression so that you can only run the tests that contain a certain string within the name.
So that's one of the cool things that PyTest provides.
So here are all the things that PyTest can do. Auto-collect tests to run, as you saw, or you will see soon, you can use markers for organizing tests.
I'll get into that in a bit, so you can essentially say this test is A, this test is B, run all the B tests, run all the A tests, and all of a sudden you can organize all your Selenium tests quite easily.
Generate test reports, you saw that, provide test assertions, that's also available.
You can multi-thread your tests by just saying dash N8 on the command line, and all of a sudden you'll spin up eight browsers, you'll see that in a bit.
There's a large number of existing plugins already available, the PyTest, such as the PyTest HTML, which generate reports, and there's a lot of additional ones too, such as for multi-threading support, and a lot more that we'll get into in a bit.
So what about complete frameworks? Selenium-based combines the best of Selenium, Python, PyTest, all that into a powerful framework, and we're going to do some live demos for that in a sec.
So you already saw most of these things. The features that I was covering before were actually from Selenium-based, where you have the self-doubt, certain o-broken links, assert text, command line options, where you can just change your browser, easy to read error messages, and you can see exactly what went wrong, and the reports, etc.
To get that, it's just instead of PyTest all Selenium, it's PyTest all Selenium-based. So quite easy to get, and that is a screen from the GitHub page.
So now that we've covered the first 15 minutes, just a few slides, we're going to start jumping into some GitHub readme files, some live demos, running some scripts, etc.
I will, we're basically going to talk how we can evolve raw Selenium into something more advanced like Selenium-based, but if you want to see a few examples of this running a test with Selenium-based, let's run a quick test, my first test, from the Selenium-based examples folder.
And that ran pretty fast, so you might not have seen what it was doing, but there's a cool mode called demo mode, which actually highlights the browser actions so that you can see what the test is doing, and what it's asserting at every step of the way.
So you have element assertions, you have text-based assertions, certain title, etc. The JavaScript will go right onto the page and show you exactly what it's doing.
But if you don't run with demo mode, it just runs in like instantly, like a few seconds, it does all those things. We're now slowing it down so you can actually see all the various things that are going on in this particular example test, such as adding a backpack to a cart, and then going through the checkout process, and then making sure that you've got the thinking for your order at the end.
So let's take a look at what this particular test looks like, and then we're going to take a few steps back and take a look at how raw Selenium evolves into something like this.
So if we open my first test.py, you'll see it's just a simple command such as opening a web browser.
Actually, let's see if I can make this a little bigger to see if you can make it easier for everyone to read. Okay, is that a little better for the audience? Okay, cool.
So the spinning up of the web browser is done automatically, and you can change what type of browser you use.
For instance, if I wanted to run that with like a safari browser instead of Chrome, I would just do pi test, my first test.py, and then do dash dash safari, and you can see that it's now using a safari browser.
If you look carefully at the top left, it is doing that. So that was it running in safari.
So command line options that you really control and customize the various tests that you have. So back to here, here's a simple command for opening a web URL, then you can type text into a text field, and then type in the password, and then the backslash end will give you a submit action automatically.
So one line of code handled the four lines of code that you saw earlier.
You can easily assert that an element is on a page or assert exact text. You can click a link easily or click an element like the button here.
Click a shopping cart, assert exact text. So the difference between assert text and assert exact text is that assert text lets you know if the text is in the full text.
Whereas exact text means an full text match instead of a substring match.
So yeah, lots of simple actions, but it performed a lot of things. And of course, there's also a JS click available instead of a regular click.
When you ever want to click something that is maybe hidden behind another element, otherwise you might get like an element click intercepted exception or like another element was over yours.
There's lots of different APIs that you can use for that. So that's just a basic test, and it's a lot more simplified because it takes care of the browser management.
Now let's take a look at how we evolved from regular Selenium to something more advanced like Selenium base.
So let's go over to the raw Selenium and let's take a look at a flaky messy raw example where you have to specify.
So quick step back. So there is a built-in framework for Python called unit test. And unit test dot test case is something that test classes can inherit in order to gain additional assertions and they'll gain automatic setup and tear down methods like you see here setup and tear down, which will be called automatically at the start and end of tests whenever you run that.
So let's see if I can make a little bigger so you can see. So unit test provides automatic setup and tear down so that you don't have to call it directly from your test.
It's automatic before and after your test starts and ends. And inside the setup and tear down methods, you can specify how you wanted to launch your browser.
And this particular example, it's using raw Selenium not Selenium base. So we're just using regular from Selenium and port web driver. And all of a sudden you see that you have to define all those things like how you want to launch your web browser because that's not automatic because Selenium on its own doesn't include a test framework that does all that for you.
And of course in a tear down step you'll have a quit process. So you might then have to define your own methods such as is element visible and you'll check that if there is an exception returned after trying to do a self dot driver dot find element action.
Then you'll return false otherwise you'll return true if say the element is displayed. So when you're not using a test framework, you have to actually define all these methods on your own and it can become little cumbersome but that's why test frameworks exist in order to simplify things for you.
So here's the test that we're creating here with raw Selenium test add item to cart. You're doing a self dot driver dot get action. You're going to instead of using the buy dot CSS selector maybe you'll put that into a variable so that you don't have to type that in. And then you have to say element dot clear but maybe in this particular example the text field is already empty when you went to the page.
So you didn't necessarily have to clear it but a lot of times you might have to send keys is the typical you know type text into the text field and all that.
And test like this can be flaky because or they're very long and messy because you have to do the whole driver dot find element with specify the buy specify the selector then tell it to do a click.
So that's what regular Selenium provides for you and out of the box this is what you'd have to do unless you were to define methods that do these advanced things.
So as you can see here the script is quite a bit longer than if you use something such as a Selenium base which does simple methods all that for you.
So that test does the exact same thing as this but not totally exact but the same thing but it takes a lot longer to do the same thing with Rossellinium.
And of course the script can be flaky because if any of these elements aren't loaded right away you'll get like a stack trace and a failure for that.
So that's the first step of Rossellinium usage basic things but let's say you want to improve on the flakiness level of that.
Well there are additional things such as there's the Selenium dot web driver dot support dot UI which includes web driver weight.
So this is basically the next evolution of Rossellinium.
A lot of people start using web driver weight in order to wait for an element to be available before interacting with it.
So as you can see here if we go into the test itself you now have to say like to look for an element you're doing element equals say web driver weight self dot driver and how many seconds to wait for until the element say is clickable or the element is you know visible.
And then you stop to specify the buy dot you know CSS etc and maybe this selector with that and that takes up a lot of code significantly more than just like a simple assertion.
So web driver weight is one evolution of that but it's still a lot more code to do so you still end up with a really long script if you have to use a web driver weight EC dot element to be clickable after every single action.
So it's like the first evolution of evolving and then let's say you want to extract those out into methods themselves well you can do that and then inside your test you'd call say wait for element visible and that would just be defined as a huge web driver weight command but instead of calling all this in multiple lines of code you now just do it in one line of code.
So where it starts to simplify the method and all of a sudden it looks a little cleaner than throwing web driver weights everywhere and it's not as flaky as just trying to do a click directly because then if the element doesn't load you get a stack trace and a failure there.
So that's the next evolution.
After that we have the refined raw which basically really builds out advanced methods such as a click method so you'll see that we'll first wait for the element to be clickable or visible and then you get the selector the bike was by etc so we're building out those original methods and now all of a sudden we have a click method.
So by the end of all these methods that we built out we've got a script that looks pretty much just like the selenium based version but it's now using only raw selenium so as you can see here it's just from selenium import web driver and a few of the existing APIs that selenium already provides using this example here you've actually refined your tests to basically be a simple version of what you want.
So that gives you something like this as the full test and all of a sudden it's a lot more readable and easy to follow understand and make changes to it so that's how you evolved something such as a raw selenium building block into something that actually becomes easier to use.
So now that we've basically taken the API from really raw to a more refined thing selenium based tries to simplify all that and if we go to the repo you'll see that there's a lot of advanced features such as dashboards and reports etc.
So let's say we run a different test let's do pi test test suite dot py and then let's do dash dash dash board and then dash dash HTML equals report dot HTML.
So this is going to run a quick series of four tests and two of them will pass and two of them will fail on purpose so that you can generate the report at the end.
So now if we want to take a look at the report open report dot HTML you get a dashboard a pie chart and inside here you have stack traces with screenshots so you can see your click in screenshot of that particular failure that one was failing because the fake text was not visible after 0.4 seconds.
So there are default time outs built in that are probably like seven or 10 seconds but you can change that within your test.
Here the fake element was not present again so the test failed on purpose and you see the screenshot that gets generated and so you have stack traces screenshots and of course pie charts.
There's also a regular dashboard view so if we go open dashboard dot HTML I should take that file and open it in here.
You'll see that there's a logs and a data folder but it's kind of small so let's see if I can make it a little bigger.
So inside the data folder for like a failing test you'll see a basic test info dot TXT file I'll expand it so you can see a bit of what you get from one of these reports.
So you'll have the test that it ran the last page that was on that the test was on when it failed how long it ran for the browser that you had the driver that you were using with it.
And hopefully the version of Chrome driver matches your version of Chrome. You'll also have the Unix timestamp which is great for helping you debug the issue and that converts into a regular date and time so you can see exactly when the test ran and my clock is still on Eastern standard time.
It might be actually ahead of it's actually 528 here in Chicago so it is it's based on your computer on the computer's clock.
So if your computer's clock is wrong it's going to match that but you can always sync it up with UTC etc so that you know where exactly you are.
You have a nice trace back in here where it says okay fake element does not exist was not present after 0.4 seconds.
So that is cool so that is basically the dashboard and the HTML reports functionality you also get a screenshot in that particular log and you have the whole HTML file which you can then take a look to see if there are any failures that occur you can look at that easily works great with like build systems such as Jenkins etc.
So the next part let's take a look at some of the cool command line options that you have actually first of you just type space on the command line you'll see a whole lot of different things that you get out of it such as the methods common options the gooey recorder the ability to print tests right from the command line etc.
So I do say space print basic test.py it's just going to print it which is good so that you can see exactly what is inside your script you can do dash and the print it with line numbers cool so if you do you type space methods you'll see a lot of common methods such as clicking clicking links you can click check boxes easily with check if unchecked so that if the check boxes unchecked
will automatically check it you can grab the page source easily you can do drag and drop hover and click select option by text switching into an iframe easily lots of different assertions that you can use such as asserting that there are no 404 errors there no JS errors etc.
If you type space options you'll see lots of various command line options that you can use such as changing the user agent changing the browser using demo mode maximizing the window using the dashboard using a pi test collect only run incognito mode
So if we run back the test suite that we ran a moment ago you saw that it opened up a new browser each time there's a dash dash RS which stands for dash dash reuse session which means it will run all those tests in the same browser window without having to spin up a new browser window each time and that will save a ton of time
also there is the ability to multi-thread those tests so if we ran the same thing and we did dash n 4 you'll see that it's going to spin up 4 different browser windows instead so you can easily do multi-threading and all that there's also a very powerful tool called the recorder
so let's open that you see a little tool that comes up so let's do sauce demo.com and then do a record so I can basically record actions let's do standard user and then so right now I'm typing this in so that the recorder records a script I'm going to add two items to the cart
and then I'm going to click on the cart and then I'm going to click checkout and I'll put in like fake name 1 2 3 4 5 continue and then finish and then I'll do shift 7 switch into assertion mode I can assert that the text is there when I'm done I get to go back to the command line which was here here we go so you see it created a break point
so if I do see to continue from the break point you'll see that it generated a full test out of just the actions that I did so instead of actually having to manually create all your tests
you can use a slanting based recorder to instantly generate the entire test for you so now if I run that I can do playback and it's going to playback the exact same thing I just did if I do playback in demo mode it's going to slow it down so you can see what exactly you created
so here now it's adding those exact same items to the cart and now it's verifying the cart typing in the fields it'll automatically generate a full Python test for you just like that with a few clicks you don't have to even know all the APIs you can do all that for you which makes it a lot faster and easier to do
so that's the slanting based recorder really fast way of just generating tests on the fly there's also plenty of other advanced features such as the presentation generator and if you hadn't noticed the presentation that I ran earlier this was all built in Python
so if I open the thing the presentation that I ran earlier I use slanting based to generate the Python or to generate the JavaScript from the Python so I did a pi test fundamentals.py it's running a Python script and that generated this entire presentation that you see here today
so some of the advanced tools that you'll have here is the ability to not just do testing but you can generate presentations you can even generate advanced charts I'll quickly show you that so if we go to the chart maker which is from the slanting based examples folder and you
can generate a pi test chart presentation you'll see that you can generate a pi chart with regular Python bar chart column chart and you fancy animations like that there's even a website tour maker I'll quickly go for that
test maps intro GS tour where it uses a pi test to run some Python code that automatically hacks into Google maps will not not really hack it in it goes it changes the browser that sees it and you now added a website tour
so as you can see here you can use the slanting based to not only do tests but create a whole website tour and then you can export that into the JavaScript file and then load that directly into your website as you can see here
tours exported maps intro GS tour dot JS so the Python generates like a whole website tour for you so that's just some of the cool advanced things that you'll have here and there's a ton of stuff on the GitHub read me
page and if you haven't started the GitHub repo already please do there has all the instructions that didn't get to cover today such as various formats and there's multiple syntax formats such as the regular
base case inheritance I'll just make that a little bigger so they can see that's like a standard way of doing it but it also can handle things such as
pi test fixtures where if you load SB and you're familiar with pi test you can run everything as the SB fixture and another common one you can do is the context manager
or even the behave BDD gyrkin syntax format for people who are familiar with that so you can also use the slanting based recorder to record this exact same BDD style gyrkin test as seen here and you'll have to do that on your own because I am running out of time but to end off I'm going to play a video that basically use selenium base to generate a
automation that modified several different websites the same slanting based going in and hacking say Apple
Google and all the various websites you'll see here with automation because Selenium has the ability to execute JavaScript in the web browser which means you can easily modify any text on any
website page and even create like a music video like this so this is actual slanting based going in with the demo mode as you saw and changing the various text that you see that was like github
it's going to go through and here is like dev.2 it just goes through and just changes all the text so as this plays basically want to say that
slanting based can do the test automation instantly generate your test but generate presentations cards website tours and hack websites but it's really it's only hacking your browser not so much your website and as you can see it's just going through and this is actually one of my most fun videos that I created
where this okay can I just go on to like every single major website and just change the text and actually I think a few of them thought they were actually hacked
is like they saw the video I'm like wait a minute no that's good it's just someone messing around with their browser doesn't actually hack their website but with JavaScript you can do anything
and slanting based basically utilizes best to Python generate a lot of JavaScript to do advanced things such as demo mode and all that so yeah this is the last part of my presentation at the
two-minute video where you go in and you probably recognize a lot of these websites is like Slack and if you want to see what the script looks like I'll quickly show you what that looks like at the end
take a few seconds once is over but yeah here's a slanting website as you can see here slanting automates browsers but what you do with that power is entirely up to you which means if you want to use that power to make a music video
where you hack a bunch of websites then that is power to you and all the other things that you want to do all right that should be less than 20 seconds away from completing
that's the pipa.org website where you download Python packages such as slanting or slanting based probably recognize it last year there's one for I boss and three house and then it is end game
and very last thing I'm going to show you is the script that I did for that so I'm going to open up that script so you can see exactly what that looked like open hack the planet.py
and here is the cool method that you pretty much used everywhere set text content so that is you to change the text on any website.
All right cool well if you have any more questions about slanting based check out the GitHub page and also because this is the only real Python session at the conference and you want more Python and more cool awesomeness come see me
even tomorrow I might do like a small find a room somewhere and then show more advanced features such as more dashboards reports and all the other api methods and command line options I didn't get to cover today such as how to change your proxy server or other additional settings that you can do from the command line when you run a test.
All right that's let's open the floor to questions they're going to pass around the microphone to anyone who has a question and yeah please ask and raise your hand if you have questions the microphone guy will come to you.
Great presentation thank you.
We generally when we use the selenium as an UI test framework now one of the main except.
Stay exception what we see so from the selenium base is there any weight automatically detects the state except yes so with the selenium base api it's automatically going to avoid that because it's always going to refine the element when it does it's automatic waiting so if I were to go into the code right now so this is just
the big selenium base with all the different things inside the api which is located at selenium base fixtures base case.py if you go into that selenium base that's where like all the real major code lives base case that's what you inherit.
You'll see that whenever you're finding the element it basically does let's see find elements it calls a method and it loops through actually there's a lot of code in here so I'm not going to search through all that now but essentially you're not going to run into the stale element reference exception because if the element if you try to do a click action and the element isn't immediately there.
It will automatically search for it so run a more advanced thing quickly as I answer more questions by test coffee cart test p y dash dash r s so it's going to basically wait for the elements to appear so here I am ordering some fake coffee from a fake website it's going through and it doesn't run to any issues even though things don't load up right away because it has a default time out of say 10 seconds and if your element is going to generate like.
The stale element or that it's just going to refine it so you don't have to worry about that it's one of the things that's wrapped within the framework.
Thank you.
Next question.
We're pretty much out of time we got time for one more question.
Thank you very much.
Having built some frameworks and also very impressive to see your stuff.
One thing that I haven't seen in your demo is kind of the page object model that testers tend to use.
Yours is very scripty and so just curious what your thoughts on page object modeling in.
There is a format where you can actually structure your test using the page object models.
If you go to syntax formats you go to page object model with base case you can basically set define something such as a login page and then call the login page methods like this.
It's actually one of the 23 different formats that you can use for structuring.
So if you want to basically break out your test into page objects I assume something like this like a login page and then you want to call a method from that.
You do something like that in this way and just has examples of using all the zoom in if you can see so page object model would look like that.
There are a few other examples so that if you want to break out all your selectors into a page objects as well.
There is an instant page object model generator so for instance if I open basic test.py you see it has the selectors in there.
If I do a slinium s base object if I basic test.py so it's going to create a page objects file for it and then it's going to update basic test if I open that.
You'll see that it broke out all the CSS selectors into page objects and you can like change the naming of that so that if later you decide I'm going to reuse reusing the selector a lot.
Why not just break everything out.
You can use some of the really advanced command line tools such as the objectify command and you will immediately break out all your CSS selectors into an object file and then the script will run as is.
You can even translate similar to how we swapped your selectors with that. You can translate the api into multiple languages so let's say if you want to have a slinium base in a different language.
There's like for instance Chinese translation so it's using Chinese characters because there's a one-to-one mapping from all the slinium base methods to every other language.
So if you want to actually run your test there's a translator function. You just do s base translate and immediately translate your test into that language.
So if I do s base translate let's see coffee cart test.py and then I do dash dash zh which is the Chinese code and then do dash p to print it out.
You'll see that it translated a regular test into a different language.
So if you don't speak English at school there are 10 different languages supported. You just do s base translate the language that you want like there's like French, Spanish, Portuguese, Italian, Japanese, Chinese, Korean, all that.
You can instantly translate a test so that your team back in nano japan who maybe doesn't speak perfect English they can see or in this case Chinese they'll be able to see all the api methods with the one-to-one mapping and instantly translate and it will run just like any other test because it does the replacement on the fly.
Any other questions? All right well then come see me afterward if you have any more and I'll show you more advanced things that we did not get to cover today but thank you so much for coming to selenium conference Chicago 2023.

############################################################

[2/44] VIDEO: Undetectable automation with SeleniumBase UC Mode and undetected-chromedriver. (Python)
URL: https://www.youtube.com/watch?v=5dMFI3e85ig
------------------------------
(Source: Original Transcript)
Hello and welcome to the Automation Show.
I'll be your host, Michael Mints,
and today's presentation is a deep dive into
undetectable automation with
Selenium-based UC mode and undetected Chrome driver.
Here are the various steps you can expect,
where you build a bot,
go to a website,
bypass security,
and then you're through undetected.
So by the end of this presentation,
you'll learn how to create bots that appear as humans to websites.
These bots won't get detected or blocked.
Here's a live demo of that.
And as you can see here,
the automation script ran and Selenium wasn't detected.
So there's a lot more to come.
If one bot isn't enough,
how about several?
Here's a demo of multi-threaded bots running in parallel.
And as you can see here,
the script is running,
spinning up several bots,
and they all ran,
and none of them were detected.
So it's not just an army of bots,
but an army of bots that look just like humans using web browsers.
That's how they weren't detected.
So if this is what you came here for,
stick around to learn how to do the things you just saw.
You may find it easier to build a Selenium bot
than to navigate an obstacle course.
But first, you may be wondering who I am,
or maybe you're one of the over one million people
that have already helped on Stack Overflow.
As you can see here by the number of people
I've reached quite a lot.
I'm Michael Mintz.
I created Selenium Base,
the web automation framework for Python,
and you can do various things
like the UC mode that you just saw.
And I also lead the automation team at IBoss.
So there's me in my IBoss hoodie and IBoss booth.
So I've been doing video podcasts since 2012.
That's when I first co-hosted
the marketing update on HubSpot TV.
You can see here various images of me
from that early day podcast.
So I spoke at Selenium conference 2023 this year
as the dedicated Python Selenium speaker.
Here's the we build together Selenium booth.
And here's me giving a talk about Python fundamentals
to frameworks.
So here's me with the creators of Selenium web driver
on this side of me is Simon Stewart.
He created Selenium and over here is Jason Huggins.
He created a web driver and the two of them joined forces
to create Selenium web driver.
So Selenium Base Fun Fact,
the first Selenium Base GitHub issue
was from a Tesla engineer.
If you go all the way back to May 16, 2016,
you'll see that Clive Chan,
who does supercomputing at Tesla,
opened an issue.
So this was like very early days.
I think because of that, you know,
people like Tesla using Selenium Base,
I think it led to rumor has it led to a lot of GitHub stars
as you may find.
My spy network has heard no such news.
Now let me explain how we got here.
No, there is too much.
Let me sum up.
And by here, I mean at time
when lots of companies have been building services
to detect and block bots.
Here's an example of a capture screen
that your bot may encounter
if it got detected and blocked.
So in the early days,
there were few bots,
and those bots didn't look human at all.
Those early bots were mostly innocent
and most websites didn't care if they were around.
It turned and he was grounded.
Oh, yeah.
At some point,
the number of bots grew by a lot.
Many bots were programmed with bad intentions.
And sometimes you couldn't tell apart
the good bots from the bad ones
until it was already too late.
You should listen to a gap in a sense.
Then came Google recapture V1.
Although intended as a defense against bots,
humans on a web browser got hit by it.
So if you zoom in,
you can see the early edition of recapture V1.
And humans were getting hit by that all over the place
even though they weren't bots.
Then Google made improvements.
And here you can see recapture V2 and V3.
Like the I am not a robot.
The reppowered by protected by recapture logo, et cetera.
Things of recapture.
So that annoyed a lot of people
because they were getting hit by captures
even though they were,
he just humans trying to visit a website.
It wasn't good at all.
And just people were very annoyed.
Then came the next iteration of anti-bot security.
Cloudflare turned style capture replacement.
That changed the game in many ways.
Now, in a very real sense,
it's my game.
In a sense that the game revolves around me.
That was then, this is now.
I can't tell you how disappointed that makes me.
For a while, Cloudflare's turn style
did a decent job filtering out bot traffic
from human traffic.
Then undetected Chrome driver arrived.
And it was a GitHub repo
that basically provided a solution
for a Selenium to get past the capture.
On closer inspection,
you can see undetected Chrome driver
with all its GitHub stars
and all its issues
and open pull requests, et cetera.
So undetected Chrome driver
was found to be incredibly effective
at getting past the turn style.
Your station mister,
is this how you present yourself to the public?
See in here,
connection is secure, proceeding.
The maintainer of undetected Chrome driver
is right here in the screenshot here.
And he appears to be very busy with various projects.
As you can see here,
he's got 109 repositories.
So there's a lot of work that he's working on.
And of course, undetected Chrome driver
is just one of his projects.
The biggest challenge for undetected Chrome driver
has been adapting to breaking changes
caused by new versions of Chrome,
new versions of Selenium,
new versions of Cloudflare.
Those can break things
until updates are released.
What does meaning is a test?
And as you can see here
with those 772 issues
and all these open pull requests,
people have been hit by various bugs
and a lot of them.
And through the pull requests,
people have tried to help the maintainer
fix some of those issues.
So yes, because of undetected Chrome driver's supporters
helping out to fix things,
it might be a little less work for him
as you can see here.
Here's an example where there was an issue
about headless mode in Chrome version 110
and I was able to find some information
about the bug to help him out
because starting in Chrome 110,
there are new headless options
that are mandatory for headless mode to work.
And I even got a shout out about it
in version 3, 4, 5,
special thanks here to MDMense.
That's my GitHub account.
So sometimes all that help isn't enough.
That's where a Selenium-based UC mode comes in.
And here's the Selenium-based GitHub page
with all its various features.
So Selenium-based UC mode
is a modified fork of undetected Chrome driver
with multiple changes.
UC mode includes bug fixes
and additional features
such as multi-threading support via pi test X-dist.
And if you look at the screenshot here,
that's a big stack of raspberry pies
that I'm just using to simulate multi-threading support.
But really, that isn't directly related to that screenshot
isn't directly related to what Selenium-based looks like.
You'd see a lot of code.
So UC mode is one of many Selenium-based modes,
as you can see here.
But the other modes include slow mode, demo mode,
proxy mode, the bug mode, mobile mode,
recorder mode, multi-threaded mode.
You saw that.
And more, you can even combine the modes.
We'll do that a little bit later.
So UC mode is not enabled by default.
It must be activated by switching it on.
So you can use dash-dash UC
as a pi test command line option to switch it on.
And it also works with some of the Python formats
that Selenium-based has.
You can also use UC equals true
for the Selenium-based driver manager formats.
So once you have that on UC mode,
then websites can no longer detect Chrome driver.
So then your Selenium bots can do the things
that they wanted to do.
Here's an example script that uses UC mode.
And you should note that Selenium-based has driver methods
that aren't included with standard Selenium,
such as this driver.sleep method here.
Normally, you'd have to import the time library
and then do time.sleep.
Selenium-based has some nice simplifications
so that you don't have to import like 10 different libraries
into your script in order to get things to work.
Most of the time, a single import line does the job.
So in this particular format, you do
from Selenium-based import driver
and then you can initialize your driver
with various options, such as UC equals true,
to activate UC mode.
And then, once you do that,
you might want to have a try-finally block
with a driver.quit at the end,
so that no matter what your script does
if it fails on something,
the driver gets quit afterward
and you open up the resources
so that they can be used by other programs.
So one big issue that people may have
is that something happens, the program ends,
but the driver remains open
and therefore it's an extra running process
that you need to quit manually
unless you do this and have it quit.
So here's the driver.get method,
which will open up a URL,
but with Selenium-based driver.get is special.
What it does is it does a few extra things
such as disconnecting Chrome driver from Chrome
when it opens up a URL so that you don't get detected.
And then we're just gonna have the script sleep
for a little bit and then you'll do more stuff
because obviously just opening a web page
isn't that interesting.
You probably want to do more things
once you get to the web page that you want to be on.
So for reference, here's a script
in a different Selenium-based format with more methods.
So here, it's from Selenium-based importsp
and then with sp, you see equals true as sp,
which uses a Python context manager format.
You now have a driver that spins up automatically
from there and the driver will automatically close
when you leave the width block.
So here, sp.driver.get, go into a page
and then you can type text into a text field like this.
Here, type being more text.
Here, you're clicking on a button
and note that Selenium-based has a special contains selector.
If you look here, a colon contains text
which doesn't appear with standard CSS selectors.
This is unique to Selenium-based,
this particular selector,
because before it takes effect,
it is automatically converted into expath
which does support that type of selector format
with a contain selector.
And then you have other methods
such as assert exact text to make sure that, say,
welcome appears in the H1 tag.
You can do assert element to make sure
that an element's there, the CSS selector
or auto detect expath if you use that.
You can highlight an element.
You can click a link.
So there, you'll find the link text, sign out
and click that.
And then you have assert text to assert
that a text substring appears within an element
which is different from the assert exact text
which where the text has to be exact.
The assert text is just a substring.
Get ready for another live demo.
So we're gonna run that script.
We see here it's doing the highlight thing, logs out.
And of course, that script probably ran very fast.
But as I talked about it before,
there is another option called demo mode.
If you zoom in just by just adding demo equals true,
you can activate demo mode and slow down the script
so that you can actually see what's going on.
Let's run that again.
So here you can see entering the username, password,
clicking sign in.
Then it's gonna verify the welcome appears
and it's gonna verify that the image is there.
And then highlight it, click sign out.
And then verify that text is there.
And while it's verifying things,
you see like a JavaScript pop up appear
at the bottom right of the page
showing you what the test is doing.
So note the differences between undetected Chrome driver
and Selenium-based UC mode.
So Selenium-based UC mode has driver version detection
and management so automatically download a Chrome driver
that matches the version of Chrome
that you already have on your system.
It also allows for mismatched browser driver versions
so that you can have say Chrome 115
while using Chrome driver 117.
And then it works out okay.
One of the common issues in regular undetected Chrome driver
is that you get an error if there is a browser driver
version mismatch.
Of Selenium-based, that's all taken care of
and you won't see those issues.
Selenium-based also changes the user agent
to prevent detection.
And the main thing here is that like for instance,
if you run a headless web browser,
headless Chrome will appear inside your user agent string.
However, with Selenium-based UC mode,
the headless Chrome switches to just being Chrome
so that it looks like a regular Chrome instance
that a human is using and then your bot won't get detected.
It also disconnects Chrome driver from Chrome as needed
so that if a website tries to see if Chrome driver
is connected to Chrome, it won't be able to detect it.
It also allows for multi-threaded test in parallel
which you saw earlier.
And it also adjusts configuration based on your environment.
So if you're running on Linux,
it's automatically going to handle running it in headless mode
if it's like a headless Linux environment.
It'll also like use XVFP for a headless display
if it needs that.
For Windows environment, it has a different configuration
and for a Mac environment.
It'll also have different configuration.
So basically, it adapts to whatever environment
you run Selenium-based tests on.
And there are also options for proxy and proxy with auth
as you saw on an earlier slide
so that you can basically change your proxy settings
and you can even combine that with UC mode.
So here's another UC mode script.
And before I live demo this, you can just see now
it's using the SB context manager
and it's calling a basically trying to get through
but if it fails, because if it's going to check
for the text, oh yeah, you passed in H1.
If that doesn't go through the first time,
it's going to launch Get New Driver
with undetectable equals true,
slightly different from UC equals true from here.
And then it'll try again.
So that has multiple attempts on getting to that website.
Let's run that script.
So here we're going in and you have passed.
So you can see here, oh yeah, you passed
and asserts that the text is there.
So the Selenium bot got through and you saw that
because it had the JavaScript on the page
in the bottom right, which Selenium put there,
basically showing you that Selenium indeed
had control of that web browser and you got through.
So now let's learn about how UC mode works in general.
First, there are several things that need to happen
for browsers to remain undetected from anti-bot services.
So here's a list of requirements for that.
And UC mode covers most of these.
You need to modify Chrome Driver
to rename Chrome Driver Specific Variables
that appear in the Chrome Dev Tools console.
A website would be able to find those variables
and then detect you from that
if you're not modifying your Chrome Driver.
You also need to launch Chrome
before attaching Chrome Driver to it.
So meaning, don't launch Chrome with Chrome Driver.
You need to create a sub-process that launches Chrome
and then after Chrome's already been spun up,
then you can attach Chrome Driver to it
and continue your test from there.
And you don't want to use Selenium specific Chrome options
because that'll easily get you detected.
And if using Headless Chrome,
change Headless Chrome to Chrome in the user agent
that's something you saw before.
UC mode does that automatically for you.
If using a custom user data der,
don't let that folder be used with non-UC mode Chrome.
I'll mention that again later in a different slide,
but essentially if you're using user data der
and you're setting like a custom one,
make sure that that user data der
isn't used with like your regular Chrome
or a non-UC mode Selenium based test
because it's gonna be configured differently
and as long as only UC mode uses that user data der
that you set, then everything should be fine.
And disconnect Chrome Driver briefly from Chrome
before loading websites with detection services.
That's done automatically from UC mode.
It'll open a website, first it'll detect
if something, if it needs to disconnect
and then it'll disconnect and continue from there.
So the good news, as I mentioned before,
most of these things are already done automatically
when using UC mode with default settings.
The part that's your responsibility
if setting in custom user data der
is making sure that the user data der
is only used by UC mode Chrome instances.
If you cross the streams,
UC mode can be detected.
There's something very important I forgot to tell you.
What?
Don't cross the streams, stopping instantaneously
and every molecule in your body exploding
at the speed of light.
Total proctonic reversal, right?
That's bad.
Okay, all right, important safety tip.
Thanks, you good.
And UC mode takes care of all the other requirements.
So with those things done,
your bot can appear human.
But if anyone looks too closely at what your bot does,
it may raise suspicion even if already marked not a bot.
Here's to the in-star plate.
Zooming in here to some other example websites
that's letting base UC mode traveled to,
they'll say no automation framework detected
on a pixel scan or you are not a bot automation tool,
not detected from a fingerprint.
So it's not just cloud flare captures,
but like pixel scan, fingerprint, et cetera.
It basically, none of the sites will be able to detect it
if you're using UC mode correctly.
So there are additional methods that you can use
to have a better experience when using UC mode.
So note that driver.get URL has been modified
from the original to reconnect automatically
if a web page is using bot detection software.
So since driver.get has been modified,
there has been a new method added driver.default.get URL,
which exists to do a regular get.
And this is useful if you're revisiting say the same website
that you've already been granted access to.
Like they already said, oh, this is not a bot.
Let them through because once you're in,
there is a cookie that is saved in your cookies
saying that you're not a bot.
And then you can just refresh the page
and it probably won't check to see if you're a bot again.
So this is useful to avoid the two or three second disconnect
that may happen if you need to revisit a website
that you're not worried that they're gonna check you
as a bot again.
So there's also a UC open method,
which will open a URL in the same tab with a disconnect.
Now this is slightly different than the get method,
which opens a new URL in a new tab
if it needs to disconnect.
So this might not be enough to bypass detection
because if you're in the same tab
opening a new URL, there might have been some data corruption
or whatever where they'll be able to detect
that Selenium Rana command on that page.
So already there might be not just like maybe a cookie
that was saved, but session storage items in there
that would alert a website that you're a bot.
And because you don't want any like session storage
or anything like that getting in the way,
there's the UC Open Whip tab method,
which basically is the same as the driver.get modified method,
but without the precheck so that you can immediately
open a URL in a new tab and have the disconnect right away.
So as a reminder, the driver.get URL precheck checks to see
if a URL has bot detection software on it
before opening the URL in a new tab with a disconnect.
This precheck is done using Python's request.get URL method
before opening a URL in a UC mode web browser.
If the response code is a 403 from the request.get call,
which is another code for forbidden,
then the URL is opened with a disconnect.
So you can also customize the default disconnect reconnect time
and here's a method for that driver.use open with reconnect
where you put in the URL and the reconnect time
so that you can change the default disconnect reconnect time,
which is two seconds.
So here's an example driver.use open with reconnect
where you have the URL and then you have the reconnect time
seen here.
There's also the short form example where,
because there's only two args,
you can just put in a six there instead of reconnect time
equals six, just to make it slightly shorter.
So you can also click with a disconnect reconnect.
There's a method for that driver.use click.
So if your bot needs to click on a button on a website
that has anti-bot services,
you might be able to do it with this special method,
which forces a short disconnect,
unlike a regular click,
which then may make Selenium revealed to the website
and then they can block you after that.
So there are some defaults such as
bike will CSS selector and the timeout is seven
and that timeout is for waiting,
for how long to wait for an element to appear
to try to click on it before failing that, you know,
the element that you're trying to click on doesn't exist.
So here are some examples of that driver.use click button
and driver.use click say button pound ID
and then change the timeout, so say timeout equals 10.
So here's some links to UC mode code
and then you can just go through each of these,
for instance, verify undetected.
It'll open a link to GitHub
and you can see like the code here.
There's a lot of advanced stuff in here
so that if it fails the first time
when trying to go to a website,
it will try to do, you know, get new driver again
and click as you saw that before, self.get new driver
undetectable equals true to try to do that again
and then it will do driver.get, the URL
and then I'll try to verify success again
and you saw a little bit about that in the earlier examples.
You want to assert that the text is there, oh yeah, you passed
and then you can post like a JavaScript message,
slenium wasn't detected in like the bottom right corner
of the screen, et cetera.
You didn't print that output to the console.
There are other examples too, like UC CDP events here
at similar, but this allows you to save the CDP calls,
you know, Chrome DevTools protocol calls
and you can do stuff with that.
There's also a simple raw UC mode example.
We're just using the SP context manager
from slenium based import SP
and you saw that in an earlier example.
So plenty of examples right from the slenium based GitHub page.
So if there's anything you need, you can just go there
and find it.
So these are a bunch of links that are useful.
So there are a bunch of things to keep in mind.
You may need to adjust default settings
for your bot to remain undetected.
Add from college lacrosse, how are you?
Step back from the door.
I got, look at you, you're a guard now, huh?
How long have you been guarding?
Step back.
Now, what kind of talk is that?
Give me a hug, you big joker.
That is good to see you.
Once your bot enters a website,
it should continue to act accordingly.
Tom Holland, is it?
We don't mean your family any harm.
Well, we did your shoot as that.
Aside from shooting your dad, we don't mean
your family any harm.
He's only stunned.
Are you real?
Improvise if your bot makes any mistakes.
On behalf of all of us, Mr. President,
I've been authorized to plead not guilty.
On the other hand, they have also authorized
me to plead guilty.
Now, I am confused.
That's good, keep rolling, keep rolling.
Ask him a question again, I like that.
That was a good answer, Bill.
Ask me a question again, that's good stuff.
This is a good email, we try.
Go.
Hang on a sec, let me get you.
Recapture my mood.
No, no, no.
That was great, dude, again.
Let's say, all right, grim it up.
Grim it up, I'm trying.
Your bot should look human to avoid detection.
Leave log and prosper.
You guys look very realistic.
Number one to enterprise.
Ethical concerns.
Don't use bots for evil purposes.
You're punching out early today.
It says who, who to help?
I don't tolerate insubordination, mister.
Not now, not if you're five.
Thank you, sir.
Do use bots with honorable intentions.
Need you to know something.
I'm Sharon, but I'm a different Sharon.
I know who I am.
I don't have hidden protocols or programs
allowing you to wait to be activated.
I make my own choices and make my own decisions
and you just know this is my choice.
Do use bots for automating tedious manual tasks.
Do take the time to train and configure your bots.
I fold.
Allow your data.
It makes very little sense to bet when you cannot win.
But I did win.
I was better than you would call.
Final remarks.
Not all bots are created equal.
But I have been programmed to adapt
to whatever functions you may require.
I am a high-grade model of a multi-purpose service
road.
I have information on each planet.
Now be my master road.
I don't deal with things at first.
Anything mechanical.
I'm friendly with all life and school
and I can both have school.
Slending base UC mode lets bots appear human.
I will not forget it.
A jet surf.
But with your help, I am learning.
Visit slending base on GitHub for more info.
GitHub.com slash slending base slash slending base.
Questions?
Just go to the GitHub page and then
go to the discussion section, as seen here.
Also if you found a bug, you can go to the GitHub page
under Issues and open a ticket there
if there's anything that you've found.
So perfection takes practice.
Keep iterating.
Resist the Borg.
You will be assimilated.
10%.
79.
No, no, no.
I can do better than that.
3%.
I can do better.
4%.
Do it again.
We got your signal.
How are you able to fly 4% again?
Slending base gives you the tools that you need to succeed.
So thank you for watching this tutorial.
If you have any questions, just go to the slending base page
on GitHub GitHub.com, slending base slending base.
And then there's going to be tons of links to read me
files that basically give you all the information
for how to use any of the modes, various command line options.
You can see the various formats that you can use.
There's even a recorder that can be used
to generate your tests automatically for you.
So lots of cool stuff.
And there are plenty of other videos
that you can find to see all these demos
for whatever tool you're interested in.
So remember, slending base gives you
the tools that you need to succeed in automation.
Thank you for watching and see you on the automation
world places.

############################################################

[3/44] VIDEO: Undetectable Automation 2 - with SeleniumBase UC Mode (Python)
URL: https://www.youtube.com/watch?v=2pTpBtaE7SQ
------------------------------
(Source: Original Transcript)
Hello, and welcome to the Automation Show. I'm Michael Mintz, and this is
undetectable Automation 2 with Selenium-based UC mode.
So this is, of course, the follow-up to my previous video, Undetectable Automation,
which you can find on YouTube if you haven't seen it already.
So there you learn the basics of bypassing captures, sort of like in the screenshot.
So here's what to expect from this presentation.
You'll be learning how to bypass most anti-bought systems.
You'll be using UC mode on more than just Chrome.
You'll be overriding your browser's geolocation, using cookies to bypass login screens,
and live demos of all of the above.
So on the topic of live demos, I'll run some of them now.
Get ready for a live demo of bypassing CloudFlare to reach GitLab.
Alright, so we're going in. You see the Capture. Capture gets bypassed,
and you can see that Selenium-based wasn't detected.
So GitLab, common site that has a CloudFlare Capture to get in.
So let's get ready for a live demo of bypassing Bing's turn style.
And this is on Bing.com, Turing Capture Challenge.
I'm not sure they use it for, but there's a Capture and Selenium-based UC mode
was able to get by it without a problem.
Now let's get ready for a live demo of bypassing a Capture.
We're clicking the Capture checkbox is required.
Alright, we're going in to the Selenium-based turn style test.
Click the Capture, and you can see Selenium-based wasn't detected.
Now, let's do a live demo of bypassing a Capture,
where you must fill out a form and click the Capture checkbox.
So you can see here giant form.
We're going to fill it out with Selenium-based,
and then click the Capture at the bottom so that we can submit successfully.
There you have that.
So let's get ready for a live demo of bypassing a Capture that only appears
after submitting a form.
So we're going into autrefs.com, which is a website authority checker.
You see that the CloudFlare Challenge there was bypassed,
and now it's loading the data.
And as you can see there, Selenium-based with all the backlinks,
linking websites for GitHub.
So now let's do a live demo of bypassing a Capture that only appears
after clicking to sign in.
Alright, so we're going into steamdb.info,
and we click the sign in.
You see the CloudFlare Capture that got bypassed again,
and now we're in, we can do whatever we want.
So yeah, Selenium-based wasn't detected again.
Alright, so let's now do a live demo on a more advanced site
where you're bypassing multiple bot detection systems at the same time
via the Pixel Scan website.
So we're going in pixelscan.net,
and as you can see here there's going to be tons of different checks
that you're going to have to pass in order to prove you're not a bot.
So here you can see that your browser fingerprints are consistent,
that you are not masking your fingerprint,
and that no automation framework is detected.
So Selenium-based was able to get past all those anti-bot checks
with UC mode.
So isn't that exciting?
Yes!
Selenium-based UC mode helps you build bots that bypass Captures.
A robot, not just a robot,
is one that can cross the uncanny valley
and come out the other side, pass for human.
And improvements are made regularly.
I can't believe she's a robot. She's so lifelike.
Thank you. I'm learning.
For those of you who do not know who I am,
I am Michael Ments.
I am the creator of the Selenium-based test automation framework
that you can find on GitHub,
and during this presentation you'll expand your knowledge of making bots
to bypass Captures.
I'll also be using a similar format as last time,
which means including video clips with the learning.
And don't worry,
clips will be less than 24% of total time again.
So the audience really loved the previous video,
as you can see here,
a 97.5% like ratio,
hundreds of likes here,
over 400,
and only 12 dislikes for 12,000 views.
So that means that for every 1000 people who watched the video,
only one person didn't like it.
So that's pretty good.
So let's hope to continue that today.
And I also had tons of amazing comments from the last video
because people were really excited about the work that was done.
So some of them were like,
oh, this was fun, extremely useful.
Selenium-based is amazing.
Save me a lot of time with Selenium-based.
I used to only use undetected Chrome driver itself.
Thank you.
You continue to amaze me with your additional great ideas.
I've been following you on the net.
Keep up the great work.
So tons of positive comments.
So people really like that.
And we want to continue that momentum and energy here.
So there were a small number of people who didn't like that first video,
mainly due to the video clips.
And for that, I can only show this video clip.
So a few people said that they didn't like the humor.
You think you're funny?
I'm not saying I'm funny, but I didn't open my night one.
You're not funny.
Of course, there were people who did like the humor.
You're funny, rookie fellow.
Yes.
Yes.
Now, if you don't want the added entertainment,
if you go to the UCMode docs on GitHub,
we can read everything without all these video clips
that some of you don't like or a few of you don't like.
And we'll of course visit there later in this presentation.
So if anything is confusing,
review the first video.
Like, if it sounds like I'm speaking in a different language,
then maybe you need to
review the first video so that you can understand
the UCMode concepts in terms that I'll be talking about in this video.
And that first video covered like tons of things,
such as differences between undetected Chrome driver
and SunnyBase UCMode.
There are some live demos there.
Things that you need to do to remain undetected,
which we'll also cover here today.
The new driver methods included with UCMode,
links to UCMode code on GitHub, et cetera.
So there are three types of Cloudflare captures
as seen in this screenshot here.
So one, two, three.
Just going in.
So there's the turnstile when entering a website.
There's the turnstile that everyone must click.
And there's the turnstile triggered by other actions,
such as clicking to log in, et cetera.
So here as you saw in the earlier live demo,
going to gitlab.com.
There's a capture that sort of automatically appears
and then you automatically go through it
if they don't detect your slenium bot.
Then on another website,
there might be a capture that you have to click.
And those type of captures are actually being phased out
in favor of Cloudflare's like newer system,
which basically triggers a capture after you perform
another action, such as submitting a form, et cetera.
So you might see the second version
not as frequently as the third going forward,
but we're going to basically show you
how to bypass all three.
So note that each type of capture must be handled differently,
and that's very important.
So when you have the turnstile when entering a website,
we're going to show you how to solve that
with the SP format of slenium base.
So from slenium base, import SP
and then we have with SP,
UC equals true as SP,
and the UC equals true part is important
because UC mode is just one of the many modes
of slenium base.
So you really need to specify that,
otherwise you get a regular slenium web browser
that will get detected.
Then you'll set the URL and do sp.driver.use open
with reconnect, set the URL,
and that second value there is the reconnect time,
which is essentially the time that Chrome driver disconnects
from Chrome waits that many seconds
and then reconnects.
So there's also the turnstile when entering a site
with the driver format.
So it's a little different from slenium base,
import driver, and then driver equals driver,
UC equals true, set the URL,
run the same UC open with reconnect method, et cetera,
and then make sure you quit the driver at the end
to prevent memory leaks.
Now, there's also a safer driver format,
where essentially instead of having just the driver.quit
at the end where it may not get reached,
if, say, the script fails before then,
you can have a tri-finally block
where if anything goes wrong in the tri-block,
the finally block will get executed.
And this is just like a standard Python syntax.
If you're not familiar with it, try finally.
You can guarantee that the code written
in the finally block will get executed at the end.
So there's also the base case format of slenium base,
which is the format used if you're running tests with pi test,
unit test runner that's included with slenium base.
So with that, you do from slenium base, import base case,
and then there's a special line, basecase.main,
name, file, dash, dash, UC,
which basically, if you forget to call your
pi test script with pi test and use regular Python instead,
this will trigger pi test automatically
so that you don't have to worry about that.
So then you create your class, class undetected test,
for instance, and then make sure you import basecase
into that class.
And then when you name your test function,
make sure it starts with test underscore,
so that pi test will pick it up during pi test collection.
With this line here, if not self-doubt undetectable,
self-doubt getting your driver undetectable equals true,
that's basically there in case you forget to add dash, dash,
UC option, when you run something with pi test,
because otherwise you won't get the UC mode activated.
This guarantees that that script will add in the UC mode browser
or launch that if you didn't launch it with it the first time
when you're in the script.
And then you saw this before, set the URL,
and then driver dot UC open with reconnect URL reconnect time.
So there are 23 different syntax formats
for structuring tests with Selenium base,
and we covered a few already, such as the SB format,
the driver format, basecase format, et cetera.
And the good news is that 20 of those 23 syntax formats
work with UC mode.
So the only ones that don't work with UC mode
are overriding the driver.
There's two of those.
And then there's a GERKIN syntax with behavior BDD.
You can't use those with UC mode,
but you get 20 out of 23 syntax formats,
which is pretty good.
So there's also the turn style that everyone must click.
So in the example here, from Selenium base and port SB,
with SB, UC equals true as SB, set the URL.
You saw that before.
The new part is switching to an iframe.
So SB dot driver dot switch to frame.
And then you can say iframe.
But if there's more than one iframe on that web page,
then be sure to use a better CSS selector.
And then you can do sb.driver.useclickspand.mark,
which clicks the checkbox in the iframe in a stealthy way.
So there's also the turn style triggered by other actions.
And with the SB format, that's, you know,
again, from Selenium base and port SB,
with SB, UC equals true as SB, you set the URL.
And then again, esp.driver.use open with reconnect.
And then, of course, when you call your UC click method,
then just make sure you have the selector of the button
that you want to click.
And then you'll be clicking that button in a stealthy way.
So note that if the capture type is number one or number three,
then using solution number two won't work
if they've already detected your bot.
So at that point, the checkbox is just for show.
And you'll fail to bypass the capture
even if a human takes over and clicks the checkbox manually.
So very important, if it's one of those captures
that it doesn't expect you'd ever go through,
like you're loading GitLab and automatically
you should take you through if it thinks you're a human
or one of the others, then once you get that capture checkbox there,
you're already caught.
So no matter how you click it, it won't help.
So there's lots of UC mode methods that you should be aware of.
And also note that driver.get has been modified
from its original version to reconnect automatically
if a web page is using bot detection software.
It figures that out by using a requests.get call to the URL
in advance before loading the URL,
so that knows whether or not to use UC mode open
or just a regular open of the URL.
So because of that, there's also a new driver.defaultget URL method
which will open a URL in the standard way without using UC mode,
which means you will get detected if you try to open a URL
that has bot detection software on it.
There's also UC Open URL which is basically opening a URL
in the same tab as UC mode.
UC Open with tab URL which basically opens a URL
in a different tab in UC mode.
Then there's UC Open with reconnect,
which is pretty much the same as UC Open with tab,
except now you can specify a reconnect time
so that you can customize how long the driver is disconnected
from Chrome during the method call,
so that if it's like a slow loading web page, et cetera,
or you have a slow internet connection,
you can modify the reconnect time as needed.
There's also just a simple driver.reconnect
with a timeout which will disconnect Chrome driver
from Chrome for that timeout,
or you can just disconnect without reconnecting,
so just driver.disconnect.
There's also driver.connect to reconnect again after you've disconnected,
and of course you're already seeing driver.use click,
you know, selector method to do stealthy clicks.
So also note that choosing the reconnect time
is not an exact science.
It depends on the website and the speed of your internet connection.
The default value may be too low.
Some sites like pixelscan.net require a longer reconnect time.
So make an educated guess, and try to get lucky.
In case you need help with pixelscan.net,
some working code has been provided below.
And also note that some sites like pixelscan.net require
adding incognito equals true in order to get through all the anti-bot checks.
So sometimes use equals true is enough,
you may need the incognito equals true,
as you can see below,
from slinning-based import SP,
with SP use equals true,
incognito equals true,
then you load your URL,
and the UC open with reconnect as before.
So there are three things UC mode does to make bots appear human.
Modifies Chrome driver to rename Chrome DevTools console variables,
it launches Chrome browsers before attaching Chrome driver to them,
and it disconnects Chrome driver from Chrome during stealthy actions.
For example, if the Chrome DevTools console variables aren't renamed,
you can expect to find them easily when using slinning for browser automation,
as in the screenshot where if you're typing CDC in the console,
you see all these Chrome DevTools console variables appear.
So if you can find them,
so can websites that block bots,
and if those websites find them,
then they know your bot, they'll block you.
So UC mode common mistakes.
Thinking that modifying Chrome driver
is enough by itself to avoid getting detected.
If we can't override the Auto Nav,
we're just going to have to lean into it.
We're redefine with the shuttle things of this home.
The sphere's here to slow it down.
Yup, it's not enough.
So where are some things that make UC mode work?
Well, if you launch Chrome using Chrome driver,
then there are settings that make your browser look like a bot.
So instead, UC mode connects Chrome driver to Chrome
after the browser is launched,
which makes Chrome look like a normal human controlled web browser.
So during this presentation,
I mentioned that Chrome driver disconnects from Chrome in UC mode to avoid detection.
But what does that really mean?
It means that UC mode calls this method,
which is already included with regular Selenium,
driver.service.stop.
So with the driver service stopped,
websites can't detect Selenium.
So that also means that Selenium can't perform actions
until the driver service has been brought back up.
Force engineering, take the warp engines offline until further notice
is a new on way of building up and finding a lithium chamber.
Captain, we gave that order.
That was command of Jordy LaFour, Jensen.
Please follow his instructions.
I serve.
Well, it looks like a great party to might have a join you.
You can do that using driver.service.start.
So note that the following UC mode methods automatically handle stopping
and starting the service as needed with the delay specified.
driver.use open with reconnect, driver.use click, driver.reconnect.
That basically lets you customize the reconnect time there.
There's also a special option for reconnect time
so that you can add in manual actions while disconnected.
Breakpoint.
That's where you can type C and press enter to continue
because it uses a Python breakpoint for that.
So you can see below we have driver.use open with reconnect
and you can set reconnect time equals breakpoint
or it's the second variable there so you can just do that.
And also the driver.reconnect method also has that too.
So adding in that breakpoint lets you take manual control
and still be undetected using manual actions.
So disconnecting Chrome driver from Chrome is only needed.
If Chrome driver has already touched the browser tab intended for visiting
a website that has bot detection services,
that means you can avoid detection by using a simple JS method
that opens a URL in a new tab.
window.open URL.
So window.open URL is automatically used by UC mode methods
that open a URL.
After the reconnect time has passed,
Chrome driver connects to that new browser tab
where hopefully enough time has passed to avoid bot detection services.
So that's one of the key things of UC mode.
There's also one other important JS method
that's used by sending base UC mode to avoid detection
when performing actions such as clicking.
And that is the window.setTimeout method.
So window.setTimeout
basically lets UC mode perform actions in the future.
Next Saturday nights, we're sending you back to the future.
With enough time to disconnect Chrome driver from Chrome
before websites have a chance to notice anything unusual.
This makes it impossible for websites to detect
Selenium actions in real time.
It's used by driver.ucClickSelector.
So once you learn Selenium bases UC mode API,
getting past Cloudflare defenses becomes easy.
If your bot gets reckless or if too much traffic
comes from your bot's IP address,
then your bot will probably get flagged and then blocked.
So let's talk about multi-threaded UC mode without pi test.
So in that first YouTube video I had,
you basically saw how pi test multi-threading via pi test
X-dist allows you to spin up multiple browsers at the same time
in UC mode.
Well if you're not using pi test and you just want to use regular
Python, there's another way to do that using thread pool
executor as seen here.
And that comes from the concurrent.futures library.
So essentially you do that.
Also very important, you need the sys.argv.append-n
because that activates the Selenium base thread locking
so that you can spin up multiple browsers at the same time
without them having port conflicts in UC mode.
So if we jumped to the bottom part here,
we set a list of URLs right here.
It's just like an identical list.
And then we do with thread pool executor max workers
equals Lennie URLs as executor.
For URL in URLs, executor.submit launch driver.
Then we call the launch driver method up here
and we spin up the browser in UC mode
and do whatever we need to do and quit the driver.
So that is essentially how you do multi-threaded UC mode
without pi test.
So as mentioned earlier, running multi-thread scripts
on one site from the same IP address
can lead to problems unless you do things very carefully.
So what is Rosetta 2?
And why might Mac users care?
So Rosetta 2 lets you run an Intel-based Chrome driver
on an ARM system.
The script that patches Chrome driver into UC driver
currently requires an Intel-based Chrome driver.
So Mac users may already have it.
If not, run software, update, dash, dash, install, dash,
Rosetta.
And that takes care of your problem.
So is UC mode only for Chrome?
Surprise announcement, 90 more.
UC mode networks on other Chromium browsers.
For example, Brave Today, maybe others in the future.
Time for a live demo.
All right, so we're spinning up a Brave browser
and I'm going to GitLab and we got in successfully.
So SlendingBase wasn't detected.
So this shows that Chrome isn't the only browser anymore
that works with UC mode.
So in order to use a Chromium browser other than Chrome,
you need to set the binary location.
So if you look at the code here,
I'm setting like the binary location,
which this is specific for Mac users.
If you're using Windows or Linux,
it's going to look different for the default location
of a Brave browser there, for instance.
So here you do with SB.
UC equals true.
Incognito equals true.
Binary location equals your binary location as SB.
And then you do everything as before.
This allows you to use UC mode with other Chromium browsers.
So it takes a lot of time to figure out how to support
more Chromium browsers.
For instance, I still haven't figured out how to make it work with Edge.
It's quite a bit different from Chrome.
But as for the people who keep asking me about Firefox
support for UC mode, that's on you.
One of you must do this.
So Sunnybase lets you set your browser's geolocation
using the Chrome DevTools protocol.
And we're going to have a live demo with a trip to Paris.
Let's get into the Paris mood by getting ready
for a web browser geolocation change that takes us to Paris.
So we're going to a website called OpenStreetMap.
And we just click the Show My Location button,
as you can see here.
And that also makes the geolocation appear in the URL.
And now we've teleported right outside the Louis Vuitton Foundation.
And if you don't know who Louis Vuitton is,
I think he was in like a popular song that was on the radio a lot recently.
I could have my Gucci on.
I go in my Louis Vuitton.
Anyway, here we are in Paris outside Louis Vuitton,
right outside of Gandhi Street.
And it's not India even though Gandhi Street is right there.
Yes, let's talk about how to change the geolocation.
So lots of different steps involved here.
So pay close attention.
You need to use open like a blank page,
and then use sp.executecdpcmd with emulation.setgeolocation override,
as shown there.
And then you'll do that with browser.reset permissions.
And then you'll call browser.grant permissions with origin with the open streetmap.org.
Set your permissions with geolocation.
And then you'll specify latitude longitude.
And then you'll execute another CDP cmd emulation.setgeolocation override,
latitude, longitude, accuracy, set that to 100.
And then open the website that you want to go to.
And then with open streetmap, you click the span.geolocation button,
which takes you right to your current location.
And then I use one of the slanting base assert URL contains to verify
that the geolocation appears in the URL.
So yeah, that's all it is to it to changing your browser's geolocation.
So let's talk about using existing cookies to bypass login.
So slanting base lets you load previously saved cookies into the browser.
So that you can avoid having to log in again.
Let's do a live demo.
So we're going to go to sostemo.com, log in, save the cookies,
and then do that again without logging in.
It went very fast, so I'll quickly just show you the steps involved.
First, we did a regular log in to the website.
And then we call the method sb.savecookies.
And then we opened a brand new web browser again.
And then we loaded the cookies that we'd saved previously,
which includes the log in cookie.
And then we went straight to a URL that requires that you've already
been logged into that website.
And this just the highlight shows you that you're actually logged in,
because that inventory list only appears after you've logged in the website.
So that's using existing cookies to bypass login.
So this is a reminder that all the examples from this presentation
are taken from the SlendingBase examples folder on GitHub.
So be sure to visit the GitHub page if you haven't already.
Everything's already there, and it's probably going to be easier to copy
from there than like copy from a YouTube video where it's like a screen shot
and not like actual text you can work with.
So for those you don't know, this is the SlendingBase GitHub page,
or like part of it, where there's like tons of different things
to check out, it's like a giant candy store.
There are so many different pages, examples, modes.
There's like a recorder so that you can record different actions.
There's also the UC mode docs here right below the recorder.
And then you see the presenter there.
That's essentially what I'm using to create this presentation you see here.
SlendingBase gives you a chance to give you the ability to create presentations
just like this, and I've been using SlendingBase presenter
as a replacement for other presentation tools such as PowerPoint.
So it's pretty powerful as you can see here,
and definitely be sure to check out the GitHub page for everything.
So speaking of visitors, they found me.
They found me, I don't know how, but they found me.
It was Cloudflare actually.
They found me, as you can see here on the LinkedIn Analytics search appearances page.
Yeah, they're the top companies, the searchers work at.
So yeah, they found me, and that was an interesting day.
Yeah, they got weirder.
And yeah, they're watching me on GitHub too, as you can see here.
So it wasn't long before Cloudflare pushed an update that broke UC mode temporarily.
That was SlendingBase issue number 2626.
UC mode stopped handling Cloudflare checkboxes.
So that basically took the fuel out of the UC mode plane causing a scary situation.
Naturally, I got to work on a solution right away.
We are currently at work on a solution.
Within five hours, add a workaround for people.
And that workaround basically used a thing called piato gooey.
So import piato gooey, and then piato gooey dot press with a space.
Basically, let you click the capture with like internal, like spacebar pressing,
which lets you get past the capture.
And yeah, it was a very fun day, and I added a lot of gifts and stuff.
So basically, keep people entertained as I was working on a solution.
As Kyberton would say about the newest version of CF's capture checkbox,
it's powerful, but not invincible.
Game of Thrones quote, if you guys haven't seen it.
So now, if you'll kindly pull that lever after a pip install piato gooey with the latest version of SlendingBase,
and then the code shows you how to get around to that.
However, within 24 hours, I shipped a new release that fixed everything,
and you no longer needed piato gooey.
Just regular SlendingBase was working again just as before.
And as Doc Brown says,
So predictably, Cloudflare has been keeping a close watch on SlendingBase ever since then.
All updates pushed by Cloudflare so far have been countered successfully by SlendingBase UC mode.
I found it.
Told you to be in here.
So are all capture services created equal?
As it turns out, nope.
There's one major capture service that even SlendingBase UC mode can't bypass consistently.
Google Recapture.
As you can see here, I'm not a robot from the Google Recapture thing,
and yeah, if you don't pass it successfully,
you get to find a lot of crosswalks and bicycles and other fun things, you know.
So this is one of those captures that SlendingBase can't really get through consistently.
So yeah, Google knows how to do bot detection well.
Throughout resistant crops are now sold over a hundred countries.
Other advancements in the liter of meat have transformed the synth food industry.
Speaker, committee to feed.
Recapture can catch bots very effectively.
Next.
Next.
So even though Google Recapture looks similar to Cloudflare Turnstile,
they are not the same.
Any sense?
Where is that word?
Unfortunately, I think that's something else.
What is your opinion too?
The reasons that may explain why Google Recapture is better.
Well, since Google makes Chrome, Google's own Recapture service has access to more data
than other capture services, like, you know, each capture, a Cloudflare, a data dome, etc.
And therefore, use that data to make better decisions about whether or not web activity
is coming from real humans or automated bots.
So if sledding based can't do something, I won't make up stories that I can't.
Can he make rain?
Rain?
Should have seen the rain.
I mean buckets of rain coming down day after day.
I didn't know what the hell we were going to do with all this stuff.
And if you want to talk about snow.
Don't talk about snow.
But if something changes along the way, I'll be sure to update people about it.
It gives us compassion when all that we feel is hatred.
If Google Recaptions more effective than Cloudflare Turnstile,
why are companies still using Cloudflare?
Well, the power of marketing can make anything look good on a silver platter.
It's a great choice, but nothing beats to achieve the burger with a sequel fall.
The great is 45% of the fee.
A classic bearing.
Imagine just twinkies in the 1937 shot to a cabin for pudding.
I like it.
And companies might not realize that bots are able to get through.
I mean, maybe they don't know about slanting-based UC mode.
Perhaps now they do know about it.
So let's do some trivia.
While on the topic of services that detect bots,
let's see if you can detect what's unusual about the following video clip.
Thank you, but I know one young man that does.
Him.
So my name is Chenzhen.
Chenzhen from Qingwu?
Yes.
And who was your master there?
All right. Did you figure it out?
If you determine that the video is not filmed in English, you are correct.
That scene was dubbed over with voice actors.
Actually, it's from the movie Fist of Legend from a Hong Kong film company,
which means it would have been created in Cantonese,
although Jettley's main language is Mandarin.
And that scene in that video takes place in Japan
because Jettley's character is studying with his Japanese girlfriend there.
And so, yeah, whatever language there were really speaking there,
it definitely was not going to be English.
That's for sure.
So that ties into good bot detection software,
because it can see the little things that reveal bots to not be human.
Just like maybe some people noticed that the voice actors were used
to dub over the real voices.
There's little things like that that good bot detection software
knows how to do properly.
So let's talk about the legal implications of web scraping.
So based on the following article,
it outlines a court case where social network and company meta
lost the legal battle to data scraping company bright data.
It was determined that web scraping is 100% legal
in the eyes of the courts as long as the scraping is only done with public data,
not private data,
and the scraping isn't done while logged into the site being scraped.
Unless maybe you have already had permission to log into that site and scraped data.
So if the above criteria are met, then scrape away according to the article.
And I'll just quickly copy paste that into a browser tab.
So you can just see what's there.
A legal battle of web scraping.
You can see like this why meta lost the scraping legal battle the bright data.
Talks about a lot of things, but anyway in summary,
yeah, you can scrape away for public data and also note that I'm not a lawyer.
So I can't officially offer legal advice,
but yeah, read the article yourself and make your own judgments.
So it takes a lot of work to be a GitHub repo maintainer.
There are lots of things required of us, such as writing lots of code to improve the repo.
Addressing lots of notifications, working a full-time day job, spending time with family.
I don't know if they'll let me Jean-Luc, but I will ask.
Thanks, number one.
He's my number one dad.
Creating YouTube videos.
And so much more.
I mean, maybe we want to go play like Majon or something on weekends with our friends or something.
Pretty complicated game. We have to like spot matching patterns.
Very interesting and stuff like that.
But anyway, yeah, we have busy lives and yeah, we gotta, you know, keep busy.
So here's just an example of like all the notifications I receive,
just from the GitHub page.
And this doesn't count all the notifications I received from like other social networks
where people try to reach out with slaining-based questions.
As you can see here, like look, like 16 hours ago and all that.
Like I might wake up one morning and they're like 10 different notifications.
I'm like that to deal with.
And like these take a lot of time.
There's no way I can get through all these notifications if so many come in on once on like a regular day.
So when there are too many notifications, I have to be selective.
In those situations, my strategy basically involves prioritizing tickets based on
who has already given my repo a GitHub star.
If no star, then no service.
No ticket.
Remember, starring a GitHub repo shows respect.
So if submitting a bug report, make sure to include all the necessary details.
Four. Sign phone. Four.
Oh, be five, ten minutes.
I may be slow to respond due to other priorities.
Be patient, and your turn will come up.
Otherwise, you'll miss an opportunity.
I guess I'll just go to my uncles.
Should we tell them we're leaving?
What for? Let's just get out of here.
We'll make people do. Amazing things.
So keep things orderly for repo maintainers.
Medium turkey chili.
Don't be rude to maintainers.
What is that right there? Is that lima bean?
Yes.
Never been a big fan.
Listen to the advice given by maintainers.
What is this?
It has to command 0450. I don't sell that one.
What about this?
That's what we want. It's a command 0450.
Don't believe me. It's only using the circus.
It's for elephants.
Remember, maintainers have busy lives.
And we need to make time to do marketing for our repos.
Start weight, get your star bleed. Prepare yourself for work 10 excitement.
Discover the undiscovered country.
If you like a repo, help spread the word by telling some of your friends about it.
This is Jon Snow. He's King of the North.
So important UC mode reminders.
UC mode is not enabled by default.
It must be activated by switching it on.
So that means dash dash UC.
When you're running with pi test, or UC equals true for like the SB and driver manager formats.
Otherwise, it's not the default mode, and you'll get detected.
And UC mode is one of many different slanting based modes.
So other than UC mode, there's slow mode, demo mode, incognito mode, proxy mode, debug mode, mobile mode, multi-threaded mode,
and more. You can combine modes too.
And this is not the full list. So yeah, go check those out on the get up page.
So back to the slanting based get up page.
Here's where you can go to find out all the details of things that I didn't get to cover here today.
So there are many different tools to choose from.
Don't underestimate their abilities.
After visiting a site in UC mode, remember to maintain your bots cover by using other UC mode methods such as UC click selector when needed.
Maintaining your cover is important.
So training bots is a lot like training dolphins. It requires performing lots of repetitive work.
Once the training is complete, you can expect amazing results.
So don't forget to celebrate small victories along the way.
Remember, building bots is a marathon. Not a sprint.
It's a chaotic world out there, so stay safe and stay focused on automation.
Take your time and do it right.
Sometimes the best way to prevent distractions is by tuning out negative news.
Remember, be respectful to GitHub repo maintainers.
We'll show people the door if anyone causes trouble.
Questions, just go to the GitHub page discussion section.
If you found a bug, there's an issue section where you can open a ticket.
And remember, Selenium Base gives you the tools you need to succeed.
That's what I'm talking about.
Thank you for watching this presentation.
And be sure to give Selenium Base a star on GitHub if you haven't already.
And check out some of the other YouTube videos. There's a bunch now.
So anything you want to learn about such as the recorder, there's a video for.
And there'll be a lot more videos to come.
So thank you and happy automating.

############################################################

[4/44] VIDEO: Undetectable Automation 3: "Revenge of the CAPTCHAs" (with SeleniumBase UC Mode / Python)
URL: https://www.youtube.com/watch?v=-EpZlhGWo9k
------------------------------
(Source: Original Transcript)
Hello and welcome to Undetectable Automation Episode 3 Revenge of the Captures.
And this is going to be using Selenium-based UC mode, which is a special tool within a Test Automation Framework that lets you bypass Captures and in particular Cloudflare Captures.
So this, of course, is the follow-up to my previous video Undetectable Automation 2, as you can see here.
And that was quite popular. It only came out three months ago, over 4,000 views, over 200 likes.
And that was the follow-up to an even more popular video Undetectable Automation, where we showed you all the basics of bypassing Captures.
And that, of course, had over 800 likes and over 24,000 views in the last nine months.
So we're going to expand on that today with some more advanced Capture bypassing techniques.
So here's a live demo of bypassing a Capture.
As you can see here, we're going to getlab.com, and the Capture was bypassed with the Selenium-based Automation using UC mode.
Selenium-based wasn't detected.
And the code for that is right here, from Selenium-based import SB,
and then with SB, UC equals true as SB, which is using a Python Context Manager format.
You'll set the URL like this, getlab.com, user sign in, and then you'll call a method UC Open with Reconnect URL.
And then there's a little bit more code after that because we have all of the Selenium-based methods available to you.
So you could call a method such as assert text where you'll write the text you want to assert followed by the CSS selector or selector of where you expect that text to be.
And then you can also modify the default timeout value as shown.
And there are other methods such as assert element, which we'll look for that CSS selector in the default timeout.
And then other methods like highlight and post a message, like you see here, Selenium-based wasn't detected.
So even if using UC mode, you may still need to click the capture checkbox in order to bypass it.
And that's not a problem because there are special UC mode methods for handling that exact situation.
So here are some of those methods.
There is UC GUI handle capture, which basically uses a tool called piato GUI.
And that tool will press the tab key a certain number of times until it hits the capture and then hit space bar to click the capture.
So that's the UC GUI handle capture method.
There's also the UC GUI click capture method and piato GUI is used again here and it's going to click the capture with the mouse.
Now note that you'll need to use this one if you're using Linux because the other method won't work on Linux for some reason.
I think maybe because they're more strict and you have to really click the capture with the mouse.
So when is clicking the capture checkbox required?
Well, if they've seen your IP address too many times, then they'll make you click it.
Also, if they don't accept your user agent's string, they'll make you click the capture and don't worry, UC mode gives you a good one by default,
although sometimes depending on if you're using Linux, for example, even a good user agent won't help you because they'll think you're using a server if you're on Linux,
and then they'll force you to click the capture.
And they'll also make probably make you click the checkbox of the capture if you're using a VPN if they detect it.
So for testing purposes, I'll be using a bad user agent for some of my live demos.
And this is going to force me to click the capture to bypass it so that we can simulate a more real world example where you might be running a script on Linux where you have to click the capture,
whereas on Mac and Windows, you might not necessarily have to click it if they like the data they see in your web browser.
So on the topic of live demos, I'll run some of them right now.
Get ready for a live demo of bypassing CloudFlare with tab and spacebar.
So as you can see here, we're going back to getlab.com and it's going to tab through and then hit the spacebar automatically with Pyotogui,
and then you can see that slinning base wasn't detected.
So here's the code for the previous live demo.
It should look exactly the same as before, but we've added the UC GUI handle capture method right right after calling the UC open with reconnect method.
And of course, there is the other slinning base methods that you may want to add your script because once you bypass the capture,
you probably want to do some web scraping or something else.
So let's continue the live demos with another one where we're going to bypass CloudFlare with a mouse click.
So here we're going to getlab.com again.
It's going to make you click the capture.
Pyotogui detects the location of the checkbox and then automatically goes to click it and you can see that slinning base wasn't detected.
So here's the code for the previous live demo.
It's going to look very similar as before except this time after calling UC open with reconnect.
We're going to call UC GUI click capture and that's going to make Pyotogui click the capture checkbox.
And then your additional methods that you want to add after that.
Alright, so here's a quick recap of what you just learned.
You can activate UC mode with UC equals true and here it's SBUC equals true because we're using that syntax format.
We'll talk more about that later.
To navigate with stealth, just call UC open with reconnect and the URL.
And you can also specify an optional reconnect time if the default time isn't long enough.
And you just want to make sure that your reconnect time is longer than the time it takes for your page to load.
So you can use UC GUI handle capture or UC GUI click capture to bypass captures as needed.
It's that easy.
So things can get a bit more complicated than that.
So previous tutorials on YouTube that you saw mentioned the method UC click selector.
Now, although this method can no longer click a capture directly,
it should be used when clicking on something else that causes a capture to appear after that.
And here's a lab demo of that.
So we're going to go to ahrefs.com and after typing in some text and clicking a button,
it's going to make the capture appear and then I'll click it.
And as a bonus, we're going to click it just in case it didn't go through with the automation is.
And now you're able to scrape the web page because you're able to bypass the capture that appeared.
So the code for the previous demo that you just saw can be found on the slanting based GitHub page.
Just go to the examples folder and you'll find over 200 examples of various things that you will be seeing here today.
So continuing with live demos, get ready for another live demo of using the UC click selector method
to bypass a Cloudflare capture on steamdb.info.
So we're going into steam and then we're going to use UC click that then takes you to a cloudflare capture
that gets bypassed right away.
And now that you're on the page, you can log in to whatever you want.
You can see that slanting base wasn't detected.
We ran some fancy JavaScript to have that message pop up.
So the code for the previous live demos right here, we did UC equals true.
And then we also disabled the content security policy on that website so that we can inject JavaScript in there
because some websites don't let you inject JavaScript depending on their content security policy settings.
So we go UC open with reconnect for that URL.
And then we call the UC click and then after that method was called, it took you to a capture.
But just to make sure that the capture was bypassed, we're adding in a UC GUI click capture
just to be safe to be sure that we bypass the capture when going through.
And then you have all the other methods that you need such as assert text, maybe another UC click, highlight, set messenger theme,
and then post the message that slanting base wasn't detected.
So here's some important information.
UC mode now requires pi out of GUI for all features to work.
Now, pi out of GUI may require enabling admin level permissions for controlling the mouse and the keyboard.
Pi out of GUI doesn't support headless mode and that's okay because UC mode now includes a special virtual display on Linux
so that you no longer need to use headless mode in GUIless environments.
So that's very important to know.
Don't try to use headless mode anymore.
Let UC mode give you the special virtual display and that will immediately let you run GUI in a headless environment.
So some general information.
Don't assume that all capture services are secure, even if they say they are.
I think you find it's rather more than just in order.
You're now entering the most secure location in the whole of England.
Looking at you, CloudFlair.
So on the other hand, some capture services are quite good.
Let's take a look here.
The Google Recapture Test.
We're going to try to click it.
Oh, it failed because it's making you select all images with bridges.
So well done, Google Recapture.
You've passed our little test.
I'm from MI7.
This has been a test of your emergency response systems and I have to say you've all done extremely well.
Right.
Well, I'll leave you to it and get well soon.
However, the real reason UC mode is popular, which you saw earlier, is because of the CloudFlair bypass capabilities.
That's where the high reputation comes from.
Yes.
Good.
You have reputation.
Outcome Reynolds gets it done is the top.
I'm glad to hear that.
If this is your first tutorial on UC mode or Selenium Base, then here are some important things to know to understand things better.
So what is Selenium Base?
Selenium Base is a complete framework for web automation and testing with Python and Selenium.
Now, although there are many different features, the most popular one today is UC mode, which enables Selenium browsers to appear as human-controlled browsers to websites.
So let's talk about structuring your scripts and tests.
So there are different ways of structuring Selenium Base scripts and internally this is called the 23 syntax formats.
So most examples use syntax format one from the Selenium Base examples folder, and that uses base case direct class inheritance, which uses the PyTest test runner.
However, the next one popularity is syntax format 21, Selenium Base SB, the Python context manager, which is ideal and recommended for UC mode, and as you saw in the earlier examples today, that was the syntax format that we were using for the example shown.
So here's the base case direct class inheritance.
You can see that from the Selenium Base help docs syntax formats file.
So in this format, which is used by most of the tests in the Selenium Base examples folder, base case is imported at the top of a Python file, as shown here, and followed by a Python class inheriting base case.
So here I create a class, my test class, base case, then any test method defined in that class automatically gains access to Selenium Base methods, including the setup and tear down methods that are automatically called for opening and closing web browsers at the start and end of tests.
So you can see here we created a test demo site, and because it starts with test underscore, this makes PyTest automatically detect it when it starts searching for tests.
And you might have noticed the base case dot main name file line, and that just basically enables Python to run PyTest on your file indirectly, which is basically used if you forget to call your script with PyTest.
If you call it with Python, that line is going to automatically trigger PyTest for you.
So here's Selenium Base SB, which is probably the format you're going to be using, or you'll want to use if you're using Selenium Base UC mode.
And here it's just a simple from Selenium Base Import SB, and then you'll have with SB as SB, that is the Python context manager format.
And remember if you're using UC mode, make sure to add UC equals true in there, otherwise you won't be using the stealth mode, and here's the format you see here.
So now let's talk about the Selenium Base GitHub page, which is just a massive area of knowledge and tools that are quite powerful.
As you can see here, there's just a lot going on, and it's actually quite fancy even if it doesn't look it.
But note that there is tons of excellent documentation for tools such as the recorder, UC mode, et cetera, which has its own readme file.
You may find that some tools are quite powerful.
I didn't mention this earlier, but I'm going to fit it in now.
So I'm Michael Mints, and I created the Selenium Base Framework, and I also lead the automation team at IBOSS.
And as you can see here, I am sitting at a recruitment booth because we went to UMass Amherst where I went to school for my undergraduate degree, and we're recruiting new employees.
Here's just a fun little photo of me at work, or doing stuff for work.
So also, I've reached over two million developers on Stack Overflow, as you can see here, two million people reached.
And I've got quite the reputation there because I basically helped lots of developers solve their Python and automation problems.
So let's talk about the Great Capture Dual.
So throughout the past few years, Cloudflare has pushed a lot of changes to their Turnstile Capture.
And in order to keep UC mode working, I had to push a lot of updates to counter those changes.
It has been an epic dual.
So sometimes Cloudflare pushed multiple changes at the same time.
And that's when I had to make multiple UC mode updates to counter those changes.
Sometimes I received a little assistance from GitHub.
So let's talk about the timeline of major Cloudflare updates.
So on March 20th, 2024, Cloudflare pushed a major update where they could detect UC mode Selenium clicks.
And the outcome of that is that UC mode's UC click selector method was updated to click on Captures via JavaScript using window.setTimeout,
which basically lets you call a JavaScript method in the future.
So then on May 10th, 2024, Cloudflare pushed a major update where CSS selectors of Captures were updated.
And the outcome of that is that to update all the UC mode examples to change span.mark to just span.
And no regular sunny base changes were needed.
Only changes to the example tests, because all the tests were using span.mark.
So I basically updated all the tests and then told people, yeah, just update your selectors.
And then on June 7th, 2024, Cloudflare pushed an update where Captures could detect JavaScript clicks.
This was a major setback.
So the outcome of that is that I had to add new UC mode methods for clicking on Captures with Payato GUI.
And you saw those methods earlier in the examples I ran.
So then on July 8th, 2024, Cloudflare made an update where Captures were hidden behind Shadow DOM.
They really went in for the killing blow there.
So the outcome of that is that I updated existing UC mode methods so that they could determine the Capture coordinates for Payato GUI.
And it was same day delivery, thanks to an advanced warning on Discord a few days earlier where an apparent Cloudflare employee mentioned that Shadow DOM was coming to their Captures, which was great because that allowed me time to prepare things before they released their Shadow DOM Capture update.
On July 25th, Cloudflare made updates to the CSS selectors that come before Shadow DOM.
And the outcome of that is that I updated existing UC mode methods and you can use UC GUI handle Capture or UC GUI click Capture for any Capture now.
And on Linux, only UC GUI click Capture works just a reminder for that.
I saw that earlier, but it's important that you keep that in mind.
So next, only minor changes from Cloudflare have been shipped since then so far, but it's basically been quite the skirmish back and forth here and there.
They make a change, I make an update back and forth so that I can keep UC mode working with all the latest Cloudflare updates.
So remember, give me space to work on UC mode updates as needed.
Because you never know when they'll strike next.
So let's talk about some theories on how Cloudflare detects JavaScript.
So a month before Cloudflare added JS detection, a GitHub repo named Protector was released.
Now, Protector is capable of detecting both Selenium and JavaScript.
Based on experiments, Protector's detection mechanisms appear to get the same results as Cloudflare's detection mechanisms.
It appears that Cloudflare learned from them.
So here's the Protector GitHub page and it's maybe a little popular now, but essentially this repo here had the JavaScript code that could detect Selenium and other JavaScript actions.
And of course, the creator of this repo borrowed a lot of JavaScript from other repos, such as Selenium detector and J detects.
So basically it was a combined effort to build a Selenium detector and JavaScript detector that was open source.
Not so much a JavaScript detector, but detecting JavaScript click actions on a website.
It's an important difference because pretty much all websites or all JavaScript pretty much.
So I was able to use Protector to make UC mode better.
So in order to make UC mode better, I decided to build my own open source capture using Protector, and I called it the Protector Capture.
Unlike Cloudflare's detection system, which only scans for bots on page loads and capture clicks, the Protector Capture continuously scans for bots.
This makes it a more powerful anti-bot system.
So here you can see the Protector Capture that I designed.
And you can find that on Seleniumbase.io, slash apps, slash Protector.
And you have to go click that I am not a robot.
And if you're not a robot, I'll let you through.
And if it detects at your robot, it'll fail.
And here's what it looks like when they detect you.
This is basically more of a demo website so it can show you how it detected you.
So it might detect navigator dot web driver.
And here it shows the time and milliseconds after the page load completed.
You'll also see that it detected window dot CDC, which basically shows the Chrome Deptools console variables that appeared there when you loaded the page.
And UC mode would hide that so that those variables wouldn't appear.
And then you also have the runtime stack access, which detects the web driver there.
So you can see that it's quite an advanced anti-bot system.
So here's a live demo of the Protector Capture on a website.
So access denied Gandalf blocked you because you went to Seleniumbase.io slash Hobbit login.
And of course, if you're using UC mode correctly, you can bypass the Protector Capture.
Here's a demo of that.
So the Hobbit anti-bot test page verifying that.
And then if you've gotten through, we'll get to a screen here.
Welcome to Middle Earth where Seleniumbase wasn't detected.
And it'll play a nice fun animation where you zoom in on Middle Earth there.
So what happens when Cloudflare adds real-time bot detection like Protector already has?
So currently, UC mode uses Selenium to locate the capture checkbox before the pi auto GUI click.
And this is fine for now because Cloudflare only scans during page loads and capture clicks, but not in the time between that.
So there's already a plan in place for the day Cloudflare adds real-time bot scanning.
Here's the plan to handle that.
Basically, you already have the existing method UC GUI click capture,
and there's a third argument called blind.
And if you basically set that blind to true, it'll force a retry if the first click failed
by clicking at the last known coordinates of the capture checkbox without confirming first with Selenium
that a capture is still on the page.
The page will need to reload first.
So let's take a field trip to the UC mode help docs.
And as you can see here, we're just going to jump on this fancy button here, which will open a tab.
And now we have the UC mode docs, as you can see here.
And at the very top, you'll see a link to the first UC mode video followed by a link
to the second UC mode video tutorial.
And you can see that there's going to be lots of examples and descriptions about how it all works.
So you can see here a simple example with the driver format, which is not one of the formats we covered earlier,
because it doesn't have all the features as the SB format.
But it's basically from Selenium based import driver, and then you can do driver equals driver,
use equals true, and then make sure to use the existing methods like UC Open Reconnect,
and then quit the driver at the end.
So this will basically allow you to bypass GitLab.
However, if for the more advanced functionality, for instance, if you're using Linux,
then you're definitely going to need the SB format, because that contains the special virtual display
that allows you to run Pyotogui in a GUI-less environment.
And you can probably see all these examples as we saw earlier.
Be sure to try these out on your own if you want to.
This one you saw earlier too. The Atrefs were basically we went through,
and we did a UC click in order to click the capture checkbox.
So actually to basically bypass the capture checkbox without clicking on it.
However, if it didn't pass the click, you've got the UC GUI-click capture method after that,
just to make sure you got through that capture.
So here's some other examples.
And you can see here I've been testing it on Linux with a script like this,
and it's working quite well.
As you can see, Zoom in is running successfully in GitHub Actions on Ubuntu.
And the first just a moment line was happening here.
The print, when you first get to the page, and then we called the UC GUI-click capture,
and then we called that print line again, and then we saw that it says virtual manager this time,
meaning that it bypassed the capture within GitHub Actions on a Linux machine.
So note that there's just going to be a ton of examples and other useful things
that you may want to read on your own time, because there is a lot to cover.
And there's also other driver-specific methods that you may be interested in,
such as driver.disconnect, driver.connect, other methods that weren't covered earlier,
such as UC GUI-press-key or UC GUI-press-keys,
so that you can basically use Pyro GUI to press keys on a keyboard and UC mode.
And you even have a method UC GUI-click-xy, which allows you to click on any point in the screen with Pyro GUI,
which maybe you'll want to use if, say, Cloudflare makes a change,
and I haven't yet updated UC GUI-click capture to handle the new coordinates of where the capture checkbox is going to be.
So this is like a method you could use as an alternative.
And as again, you can see UC GUI-click capture, which basically auto detects the capture,
and then calls UC GUI-click-cf for clicking Cloudflare or UC GUI-click-RC for recapture.
And although the recapture bypassing isn't working at the moment,
so essentially UC GUI-click capture just calls UC GUI-click-cf,
which I might have mentioned in earlier videos.
So then you also have the UC GUI-handle capture, which uses the tab key in the space bar to click the capture.
So note that the reconnect time is used to specify how long the driver should be disconnected from Chrome
to prevent detection before reconnecting again,
and it's important that you set the reconnect time to longer than it takes for that initial page load to happen
because Cloudflare checks for Selenium on the initial page load.
And if your reconnect time is less than the time it takes for the page to load,
then they'll probably detect that you're using Selenium and then block you.
So lots of other cool stuff here, such as basically setting the reconnect time to breakpoint
so that you can manually put in actions on the page for that being detected, etc.
And also note that even though the arg is frame equals iframe,
since Cloudflare changed their captures around to hide everything behind ShadowDum,
instead of breaking backwards compatibility and changing the name frame to selector,
it's actually that you should put the selector of something above the iframe
in that particular scenario not putting iframe there
because the iframe is no longer visible in its magic ShadowDum world where things are hidden.
So to find out if you see modal work on a specific site,
just throw in your reconnect time equals breakpoint, play around,
and if it works, then you'll know that you can use the existing methods to bypass captures.
And of course there's a multi-threaded system so that you can use, say,
this multi-threading in order to run multiple scripts at the same time,
or if you're using concurrent.futures,
just make sure you add the sista argv.append-n,
which basically tells a slinning base to do threadlocking as needed
so that it can basically make sure that it's not trying to call like Pydogui
from different scripts at the same time which would overlap and cause problems.
So the things that make UC mode work is that, you know,
it modifies Chrome driver to rename Chrome DevTools console variables,
it launches Chrome browsers before attaching Chrome driver to them,
and it disconnects Chrome driver from Chrome during stealthy actions.
And with all those things done, you've got UC mode and your bypassing captures
as long as you're using all the special methods that are described there.
So yeah, definitely be sure to read the full readme so that you're fully aware
of how everything works. So yeah, that is the UC mode health docs
and hopefully that answers a lot of questions there.
So be sure to study, study, study.
There's a lot of important information in the UC mode docs,
so study well to avoid falling into traps.
And sometimes you might still be able to get out of a trap you fell into.
Once you bypass the capture, be ready for anything.
So there's more to come, as usual, expect more UC mode updates
and note that, you know, clapler will make changes and then UC mode
sometimes has to make changes immediately after that to keep things running smoothly
and also note that new projects are classified until released.
Well, I never heard of you and you're not on my roster.
That's just the way we like to keep it, Captain.
It's double double top secret intelligence.
So I think I could tell you would be a lie, Captain.
So questions, check out the GitHub page.
GitHub.com slash Selenium base, slash Selenium base, slash discussions.
And then you can open a discussion there.
Or maybe first check to see that there isn't already an existing discussion that answered your question.
And if you found a bug, GitHub.com slash Selenium base Selenium base issues.
So you can open a bug there.
So final remarks.
Selenium base gives you the tools you need to succeed.
And tools to build lots of bots.
So we've reached the end of this presentation.
I hope you've learned a lot about Selenium base and UC mode
and do be sure to check out the Selenium base GitHub page
so that you can learn all about everything you want to know,
such as UC mode specifics, Selenium base specifics, etc.
There's so much there and just yeah.
Check it out and have a great time automating.
I'll see you next time.

############################################################

[5/44] VIDEO: Undetectable Automation 4: "Chrome Devtools Protocol" (with SeleniumBase CDP Mode / Python)
URL: https://www.youtube.com/watch?v=Mr90iQmNsKM
------------------------------
(Source: Original Transcript)
Hello, I'm Michael Mints, and welcome to Undetectable Automation 4, the Chrome DevTools Protocol.
And this, of course, is the follow-up to my Undetectable Automation Series, which you can find on YouTube,
where the first video had over 30,000 views already, and over 900 likes.
So this presentation was originally presented a few days ago at Boston Code Camp 37
at the Microsoft Sales and Technology Center in Burlington, Massachusetts.
So there are a few slides that are specific to that.
But let's get on to the main presentation here, which is Captures and Antibot Services.
Do they really work? Find out.
Last time, I talked about Cloudflare Turnstiles and Google Recapture,
and that was in Undetectable Automation Episode 3, Revenge of the Captures.
And this time, we're going to cover way more than that.
So there are all these different physical captures to click, like the Recapture,
H Capture, and Cloudflare Turnstile.
And, of course, there are lots of Invisible Antibot Services out there, such as in Capsula,
Akamai, Datadome, Primder X, Cassada, and Shape Security.
And there are also different types of Recapture, like there is the Invisible Recapture,
which isn't necessarily as strong as the physical recapture that you have to click.
So just note that not all Captures, even by the same company like Google here, are created equal.
This is what happens when you fail a recapture.
You basically have to find crosswalks and images and different types of things.
Regular automation, for sure, isn't going to solve this.
So if they catch you the recapture, then they're going to make your bot try to solve this
and it probably won't get through that, unless maybe you try to solve the audio capture or something like that.
And this, of course, is what happens when you fail H Capture.
You get to essentially find lots of cute bunnies in photos.
Automation isn't going to easily solve this, and even AI is going to have some trickiness solving that.
And, of course, if you like puppies, there's also the puppy version of H Capture,
which is equally tough to do for most automation systems.
And, of course, if the invisible anti-bot services block you, you'll probably hit a page like this, such as here.
You'll see you have been blocked, and then it'll say something like, uh, why?
Well, something about the behavior of the browser has caught our attention.
There are various possible explanations for this, such as you are browsing and clicking at a speed much faster than an expected of a human being,
or something is preventing JavaScript from working on your computer, or there is a robot on the same network as you.
So, of course, if they catch you, they'll block you.
And, of course, this is what happens when Gandalf blocks you.
You shall not pause.
But, actually, there is a Hobbit Capture.
So, if you fail that, you're going to get the Gandalf block page.
No joke. That was, uh, I put that up on sunnybase.io slash Hobbit slash login.
If you're interested in trying your bot at it.
So, also an important notice.
You should know the laws and legal implications of, uh, bypassing captions.
So, web scraping is legal if you scrape publicly available data on the internet.
However, if you log into a website and then take that data, then that might not be so legal.
So, by the end of this presentation, you're going to learn which anti-bot systems work and which ones don't.
And, you might already know this, but most don't work.
There's going to be multiple live demos.
You'll learn how to bypass weak defenses.
And, of course, you'll learn powerful web scraping techniques.
So, but first, yeah, a little about me.
So, that's me right there in the image.
I created the sunnybase framework.
And, I lead the automation team at iBoss.
And, in my spare time, I may be found spending time with entrepreneurs.
Like here, uh, some tech people, you know, uh, Brian Halegan, Darmeshav, HubSpot,
because I worked there in the past, you know, got spend time with them.
Why might be spending time with celebrities?
Like, you know, just the other week I was at Comic Con.
Got, you know, selfie with, uh, Jonathan Frakes, you know, so, uh, spending time with celebrities.
And, of course, spending time with politicians.
Like here, uh, that's Tulsi Gabbard.
Uh, I guess he'll be seeing more of her pretty soon in the White House.
But, uh, yeah, so politicians, I might be hanging around them.
And, of course, famous philanthropists and educators like the world famous Jeff Sidel.
And, I'll also be speaking at conferences.
As you can see there, it's, uh, just like me at the Selenium Com.
And, I might also be attending conferences as a guest,
such as here where I attended Microsoft Build.
Or you might find me jet skiing in Key West.
And, of course, working on Selenium Base, uh, that's my main project.
You can see here when the pandemic hit at all this extra time to spend working on it
because I didn't have like the hour commute each way to go into work.
So I could, uh, instead of commuting into the city to work,
I could, uh, spend the extra time, you know, developing out Selenium Base for automation.
And, if you go all, actually, go on the way forward,
you can see it's already like at over 5,000 GitHub stars.
And, it had its humble beginnings back when I opened source it in March at March 5, 2014.
That was back when I was working at HubSpot.
And, they're like, yeah, I could open sources.
I'm like, cool. I'll do it.
And, there you go.
Selenium Base was open sourced, and then I expanded it on my own.
And, now it's quite popular.
So, that's enough about me.
Let's begin the presentation.
So, this here is the symbol for the Chrome DevTools Protocol.
And, this is the key to bypassing, uh, captures, and, uh, other antibody systems.
So, the Chrome DevTools Protocol is a remote debugging protocol that lets developers communicate
with a running Chrome browser.
You can inspect the browser's state, controls behavior, collect the bugging information.
You can also build Chrome extensions with it.
And, of course, lots of different players are using it.
For instance, Selenium WebDriver has CDP components, and also playwright has CDP components.
So, here we go.
A lot of people are using CDP already, but not necessarily stealth CDP, which we'll cover.
So, here's just, you know, example of playwright using CDP.
You have all these different, uh, you know, CDP things in playwright.
And, of course, you also see here Selenium using CDP.
Lots of different uses there within the Selenium repo.
And, of course, people might already know this, but Microsoft still supports Selenium,
even though they have playwright.
You can, if you go to, like, the learn.microsoft.com,
you'll see that they have, like, a whole section on using WebDriver to automate Microsoft Edge,
and they've got examples that use Selenium.
Doesn't feel so awkward anymore, speaking at a Microsoft conference,
presenting something that uses Selenium, even though they're building playwright.
So, also, happy birthday. Selenium, 20 years of it.
Can you believe it? It's like, wow.
Selenium has come a long way.
And, just this year, as for a very nice birthday present,
Selenium got a new sponsor, Bright Data,
and they invested a bunch of money into Selenium,
and then got, you know, a cool notice on the Selenium.dev slash about section that,
hey, Bright Data is a new official sponsor of Selenium.
So, it's cool. We got a lot of funding.
And, of course, that's great news for the Selenium community.
Everyone's super happy to see that, you know, there's a lot of funding coming at Selenium
so that we can keep building the ecosystem up.
So, let's get back to CDP, Chrome Dev Tools Protocol,
which is the key to where we're going very shortly.
So, lots of GitHub repos are using CDP.
You go to, see, Chrome Dev Tools slash awesome Chrome Dev Tools.
You'll see a repo that keeps track of various other repos that are using CDP.
And, the first major Python implementation of CDP was here.
The Python Chrome Dev Tools Protocol,
which, of course, was created by a Mark E. Hass.
And, he, of course, works for MITRE, which means he works for the US government.
So, this Python Chrome Dev Tools Protocol was the first real instance of having a Python implementation of CDP
that could be used for stealth CDP.
So, also, it was nicknamed the Pi CDP.
And, that was the key ingredient to stealthy automation at a repo called no driver.
And, as you can see here, it has all the Pi CDP components in the CDP folder.
So, essentially, Pi CDP is powering no driver,
which is a framework used for stealthy automation.
And, no driver is the successor of undetected Chrome driver,
providing a blazing fast framework for web automation, web scraping,
you know, all that stuff.
So, that was basically the successor of this undetected Chrome driver framework,
which just surpassed 10,000 GitHub stars.
So, it was the first real popular anti-bot system
that a maintainer here sometimes takes long vacations
and it disappears for a while, leaving gaps in the coverage where things might not work.
And, of course, the issues pile up like here, 991.
So, maybe not necessarily the best option if you need the most up-to-date stealth capabilities.
So, also, in addition to using CDP for controlling Chrome in a stealthy way,
you can also achieve stealth by using tools that control the mouse and the keyboard.
And, Pi Auto GUI is one such tool.
So, as you can see here, using a pip deep tree,
you can see there's like a ton of different dependencies.
So, it's like quite a heavy project if you, like, inspect it carefully.
So, yes, I'll swigart.
He is the creator of Pi Auto GUI.
So, that is another key component in addition to CDP that we're going to need for some stealthy automation.
And, Pi Auto GUI requires a headed browser to work.
And since most Linux machines have headless displays that don't support headed browsers,
an external tool called XVFP must be used in order to simulate a headed browser in a headless Linux environment.
This is like a key component to having headed browsers work in headless environments.
So, now, if you compile all those things together,
so to have a completely stealthy framework for clicking captions and bypassing antibody systems,
you'll need a framework that uses a regular browser to hide evidence of automation activity,
CDP capabilities for performing stealthy actions,
Pi Auto GUI for performing tricky actions,
such as, you know, clicking shadow root captions,
JavaScript can't easily access that.
Pi Auto GUI can just click right through that without even looking at it.
And, of course, the XVFP integration for headless Linux systems.
So, note that, Selenium Base has all those packaged up nicely into a thing called CDP mode,
which is essentially the successor to UC mode right next to it,
and that was used for basically the early days of undetectable automation,
and that could easily bypass Cloudflare captions.
But what was limited in UC mode was that it couldn't handle all the real-time anti-bought systems,
but CDP mode can.
So, this is the Selenium Base repo on GitHub.
You can see, you know, over 5,000 GitHub stars,
blazing fast Python framework for web crawling, scraping, testing, and reporting,
supports, pi test, stealth abilities, UC mode, and CDP mode.
So, that is Selenium Base basically doing all the things you're about to find out.
And, of course, we have a Discord channel, and that was just started recently.
We've got over 200 people already, start only a few months ago,
and that is the invite link in case anyone wants to see the Discord.
And, on the topic of Discord, there's actually another cool room called Scraping Enthusiasts.
And, inside this room, there's a special tool that basically,
if you type, say, anti-bought followed by a URL,
it's going to tell you all the anti-bought services that are there on that particular website.
So, here, anti-boughtpokémon.com slash US,
it'll say, test results for Pokemon.com.
You'll see there is the text recapture,
or an invisible recapture, if you go there.
It also detects encapsula.
And, if you scroll up, say the Nike.com, you'll see it had, like, shape security.
So, all of a sudden, with this particular thing, you can detect all the anti-bought services
that are used on Barry's sites, like Pokemon.com.
All right, so moving on, if you want to access the server,
that is the invite link for this, which is useful if you want to scrape various websites
because you want to know what anti-bought services they're using before you go there.
So, if you use that tool to figure out which anti-boughts are protecting with sites,
you can create a full list like this.
So, here you can see, Pokemon's protected by the impervent encapsula.
Walmart's protected by Akamai and Perimeter X.
Albertsons is protected by impervent encapsula.
EasyJet, protected by Akamai.
Hyatt protected by Cassada.
Southwest protected by Shave Security.
Best Western protected by DataDome.
Priceline protected by DataDome.
Nike protected by Shave Security.
And Nordstrom protected by Shave Security.
So, now that you know all the different protections that are on various sites,
let's see if we can use Slending-based CDP mode,
which has all the stealth CDP features and etc.
In order to bypass some physical captures.
So, up first, PlanetMineCraft.com.
The sign-in page.
We're gonna go in.
Let's see if Slending-based can do it.
Up boom.
As you can see here, Slending-based was able to load the site and a bypass that capture.
Let's go directly to CloudFlare.com slash log in and try that site too.
So, we're going in.
It's gonna load CloudFlare.com.
And let's see if boom.
And it clicks it.
So, success.
Yeah, that was like Pioto GUI in combination with CDP mode in order to click the capture
behind the Shadowroot element.
That is quite effective.
Up next, we have GitLab.com slash users slash sign-in.
All right, so we're going through and boom.
We just bypassed their Antibot system.
And now I'm just like playing around the site.
You can see like Slending-based wasn't detected.
So, yeah, it's like writing on their Facebook wall, essentially.
You can just use Slending-based in order to modify a site itself.
So, if you're wondering about the code for the previous Slive demo,
it is right here, something like, you know, from Slending-based import sb.
And then with sb, you see equals true to activate UC mode as sb.
Then you set your URL.
Then you do sb.activate CDP mode with the URL.
And sometimes if you do things too fast, they'll think you're a bot
even if they don't directly detect your bot.
So, you gotta like add liberally a lot of like sleeps in there.
Just to prevent the bot detection from thinking the super fast clicking is normal
or basically to avoid the super fast clicking.
And then you can do something like this.
UC GUI click Capture, which if the capture wasn't bypassed right on the initial page load,
then it will get bypassed through that.
And then you can do like a lot of other things like, you know,
a certain text on a web page, a certain the element, set the messenger theme,
which is used for the next thing sb.post message.
Slending-based wasn't detected.
So you can like inject JavaScript onto the page and like do whatever you want.
Lots of cool things you can do there.
So up next, let's go to Bing.com slash Turing Capture Challenge,
which is Microsoft's anti-bot system.
But I think they're pretty much using CloudFlare for that.
And boom, that was just easy to bypass pretty weak.
I just like use the CloudFlare Capture on that.
Are you having fun yet?
Because there's a lot more to come.
So if you're not yet concerned about the state of online security,
then you probably need to see more live demos.
So it's time for live demos of bypassing some invisible anti-bot services.
So let's go to Pokemon.com slash US,
which is protected by the Impervent Capsule.
Just going to load in here.
We can see, okay, so we're on the Pokemon site.
It's going to click.
And now it's going to click the Poke Decks.
And then it's going to go in.
It's going to find electric Pokemon.
Let's say Pikachu is one.
We're going to find Pikachu and there he is.
And it's going to like scrape some data from the website.
And let's see.
Then we're going to go find all the Pokemon events in your conquered mass USA.
And it gets a list of that.
So if we go to this tab here, you can see some data that it's scraped,
such as data for Pikachu and Pokemon events near conquered mass USA.
So that's just an example of some web scraping on a site that has anti-bot protection.
Up next, Walmart.com, which is protected by Akamai and perimeter X.
So we're going in Walmart.com.
Here we are.
And then the automation is going to start typing things.
Settlers of Catan board game.
Because who doesn't like playing Settlers of Catan?
And if you can see up here, it's like loading all these different Settlers of Catan items with their prices.
So yeah, that's pretty cool.
So up next, Albertsons.com slash recipes protected by Impervent Capsula.
So if you're hungry, let's get some food, right?
All right.
So let's do a search for, let's see, Albertsons.com.
I'm in the mood for some avocado smoked salmon because who doesn't like avocado smoked salmon?
So we're going to go in, go through all the items.
You can see that it's scraping through.
It's like going through the page and it's like loading all these avocado smoked salmon items that you know.
So that was just a simple scraping of Albertsons.
Pretty cool, huh?
All right.
So that's your smoked salmon recipes.
Up next, let's do some flight stuff.
So easyjet.com slash yen protected by Akamai.
We're going in.
Going to get our, you know, flight helmet ready.
Let's see.
Automation is going in.
Going to click through that.
Let's see.
Let's go from London to, let's see what it does.
Venice.
And up next, it's going to do, let's see.
We're going to fly on the 12th of January for one adult.
Let's find these flights.
And here we go.
It's loading and boom.
From London getwicked to Venice.
Here we go.
And you can see in this panel here, all the data it's scraped about the flight data.
Such as departure times, arrival times, the price, how many seats left, etc.
So yeah, pretty cool, huh?
All right.
So that is, yeah, easyjet.
Up next, let's go to hiat.com protected by Cassada.
Going in.
Hiat.com.
Let's get some hotels, right?
Let's see.
So we're going to click on hotels and resorts.
And we're going to search for hotels in Anaheim, California, USA.
And then search for that.
And all of a sudden, we're going to get the availability within the selected dates.
And here we go.
Found a bunch of hotels.
And if we go to this tab pane over here, you can see all the places it found,
like the Hiat House at Anaheim Resort Convention Center.
And all these other places, like Casa Laguna Hotel.
Up next, we have bestwestern.com slash N slash US, protected by Datadome.
All right.
So we're going in.
Let's do a search for bestwestern places.
Let's see.
Palm Springs, California, USA, looks like a nice place to search for.
Going in.
We're going to find a bunch of hotels.
And up here we go.
They're loading.
And if we go to the tab pane here, you can see that it is loading up all these hotels
in Palm Springs, like the Chateau, Big Bear, Botico Hotel, or the in Palm Springs.
The Data Tree Hotel.
All these exciting places.
Up next, we have priceline.com, protected by Datadome.
All right.
Going to priceline.com.
Let's do some data scraping.
Let's see.
Where to?
Let's go to Portland, Oregon, USA this time.
We're going to set the dates.
We're going to go on through.
All right.
Let's see.
Hotels listed.
It's scrolling through because sometimes you have to scroll down in order for all the hotels to load.
And as it scrolls down, we can see that there we go.
It just populated the list.
And as you all know, William Shatner is the priceline price chopper.
So if he is the priceline price chopper, does that make me the capture chopper?
I would ask William Shatner in person.
But I think he still remembers the time that I took his captain's chair on the USS Enterprise.
So maybe he won't talk to me until I give him back his captain's chair.
But hey, up next, Nike.com, protected by shape security.
All right.
Here we go.
Nike.com.
Let's get some shoes.
I'm in the mood for some Air Force One shoes.
And here we go.
We got a full list right here.
Nike Air Force One, 07.
A few various ones there.
And if we go to the tab here, we can see that it found results for Nike Air Force One.
Up next, Nordstrom.com, protected by shape security.
Let's get some clothes for a friend or a wife for something like that.
You know, cocktail dresses for women, teal.
Let's do a search for that.
Here we go.
Green cocktail dresses.
Who doesn't like those?
Going through, going down, we are doing a search.
Boom.
And here's the whole list being populated right here, right now.
Cocktail dresses at various prices.
And there's a lot of options right here.
So isn't that exciting?
So yeah, CDP is powerful, as you can see, especially when used for stealth.
So yeah, CDP is the trick to bypassing all these anti-bought systems.
And of course, Payato GUI can help with that too.
So out of the following nine anti-bought defense systems.
And there's a lot of them.
The seven of these are weak.
And they can't detect stealthy CDP.
So that means the weak ones are the cloud flare,
impervent capsula, octomide, data-dome, perimeter, X,
cosada, shape security.
As you saw before, I just bypassed all these defenses.
So yeah, it's, yeah.
I wouldn't recommend them if you absolutely want to make sure no one can scrape data
from your website with automation because they will not get the job done.
However, these two will get the job done.
They're strong.
The Google recapture and the edge capture.
They are quite powerful.
The CDP is detected when you try to, you know, stealth your way through.
So they'll block you and put up, you know, physical captures
that you'll have to solve fancy puzzles on, which your automation won't do so well.
So what is Microsoft's stance on stealthy CDP?
Well, officially, playwright is an end-to-end testing framework
where we expect you to test on your own environments.
Bypassing any form of bot protection is not something we can act on.
Thanks for understanding.
And this was the answer to someone who went to bypass
cloud flare turn styles with playwright.
However, the unofficial answer is a little bit different from that
because there are external repos using playwright for stealth.
And Microsoft employees are endorsing them via GitHub stars.
So there's this framework here scrapling, which, you know,
offers undetectable lightning fast and adaptive web scraping for Python.
And you can see if you look carefully, it is using playwright.
And if you look also carefully at the people who start the repo
and there are a lot of people who start it, you'll have, you know,
someone from Microsoft and, you know, another person from Microsoft.
So, yes, so even though they're not directly saying,
oh, hey, we're going to let you bypass, you know,
anti-bot systems with playwright,
there are going to be other frameworks that use playwright
with the stealthy CDP capabilities.
And then those anti-bot systems are bypassed.
So also pretty cool thing, stealthy CDP works well with GitHub Actions.
And I was running a simple script where I was scraping some price line
just to see if it would work in GitHub Actions.
And data came in, which means I was able to, yeah,
scrape data right from GitHub Actions, which anyone can use for free
because there's like the free version for open-source frameworks.
And people might be wondering, why does stealthy CDP work in GitHub Actions
but not in other kinds of services like AWS?
Well, here's why.
Answer, GitHub Actions runs in a residential IP address space.
That is a huge deal because, you know, AWS runs in a very known IP range
where people know if you're like running a script from there
then it's coming from AWS, which means it's not human person controlling web browsers.
So it's, which means it's a bot.
And people are going to likely block you for IP ranges
but not if you're running things from GitHub Actions.
So for those of you unfamiliar with residential IP addresses
that is a public IP address assigned to a residential internet user
by their internet service provider.
It's a gateway that allows all devices on a home network to access the internet.
So basically, that's the secret.
People can use residential proxies to get a residential IP address
if their IP address is not residential.
And some legal info behind that that I looked up.
It is legal to use residential proxies to scrape content from a public website
but illegal to scrape content from a private website.
In other words, your web scraper should not log into a website
and then collect data from within that login session.
So yeah, you got residential proxies and you're scraping public data.
Go for it.
According to the data online, it is legal.
So yeah, to summarize that, scraping public data is probably legal.
Think laid site.
Scraping private data is probably not legal.
Think dark side.
And if you break local and or international laws
then bounty hunters may come after you.
So let's get back to the Selenium base, you know,
talking about all the CDP stuff, and other frameworks, etc.
So Selenium base includes a special Chrome extension called the recorder.
You can generate complete scripts with it.
S-based recorder dash dash you see.
It kind of looks like this, you know,
put in the file you want to save it as, the URL you want to record on, etc.
And out will come, you know, a script that you want to generate.
So let's use the Selenium base recorder to say go to Pokemon.com.
And let's record.
And let's see what we got.
Right.
So I am going to accept all cookies and I'm going to play Pokemon events.
I'm going to click find event.
And let's do a search for like kind of like Newton Massachusetts USA.
And click search.
And here we go.
So now we have a bunch of different Pokemon events that came up.
16 events found, etc.
So you can go click in.
And when you're done recording, just type C in the console and press continue.
And outcome is your script looks like this.
So yeah, I recorded all that.
You can see this activate CDP mode.
And it's, you know, performing various actions.
Let's try running that script with the playback demo mode, which slows things down.
See if the recorder worked.
Okay.
So we're going in.
It's going to accept.
It's going to play Pokemon events.
See if it got everything.
It's going to do Newton Mass USA.
It's going to click search.
And there you go.
It works.
It works.
So yeah, as you can see here.
Yeah, it's cool recorder can generate scripts for you.
So yeah, that's the recorder.
Okay.
So how does one make an automation recorder?
So basically need to have knowledge of analytic software, automation and testing and Chrome extensions.
And with all those key ingredients, you have an automation recorder.
And really, there's not much difference between analytic software and test recorders
because they both involve, you know, using event listeners to grab the data.
The only difference with analytic software is that the data will go to like the service provider
and their customers and it'll be a different output format.
But otherwise, the analytic software stuff is very similar to recording things in a web browser for test automation.
So if you're not familiar with what an event listener is, they're basically functions that wait for specific events
to occur on a web page and then execute a specified action in response.
So you could have the add event listener method.
So for instance, element add event listener event function, etc.
And then with all these things, you can basically, if someone types text somewhere, you can record it.
If you click a button, you can record that.
And afterward, you know, you output test automation script.
Here's like a full example, constant button equals document.get element by ID, my button.
Then you add the event listener, you click function, and then you send an alert button clicked.
But instead of like sending the alert, you're like creating, tabulating all this data
and you're going to make a script out of it.
And here we go.
Things you can record, such as click, mouse over, mouse out, key down, up, load, and resize.
So yeah, that's the secrets of building a test recorder.
And also note that there are a lot more other stealth CDP repos out there than the ones I covered
like a Drizion page, that's a popular one, had like, you know, over 8,000 get-up stars.
Then there's Selenium driver list.
It's, you know, a few hundred get-up stars.
And Patrick Python, it's relatively new one, maybe only like 40 stars.
So yeah, there's other frameworks out there, not just, you know, undetected Chrome driver, no driver,
or Selenium-based UC motor, Selenium-based CDP mode, et cetera.
A lot of different frameworks are getting into the game, like a scrapling before I showed you earlier,
where the Microsoft people were starring that repo.
So yeah, there's a lot out there.
It's also take a field trip to the CDP mode help docs, where we'll learn more things.
So going in, you'll see that there's just documentation, shows you like various things you can do.
The key method is activate CDP mode with the URL.
That'll activate CDP mode.
And then there are tons of other methods that are available that you can use that.
So some common SP CDP methods like esp.cdp.click selector, esp.cdp.click a visible type, press keys, select all, get text.
All these are available to people.
So yeah, the docs are really good.
It uses also similarly the UC mode methods, such as esp.reconnect, esp.connect.
You can also disconnect the web driver from the web browser,
and then use CDP mode to basically click things that being detected.
And you can check if you're connected or not at any point.
And there are just tons of different examples on the website, like for instance,
here is the Pokemon example that we ran earlier.
There's like esp.cdp.click etc., different other actions, like scrolling to a view, you can assert elements.
You're going to get the text, and you can grab event and print things.
So as we were scripting the data, that was all appearing there.
Here's the example of the hi-at site that was using Cassada for protection.
And here's a script that bypassed that.
There's also the best Western site here that was using data domain protection,
and we bypassed that pretty easily.
Here's the Walmart example.
And if we scroll down, here's the Nike example.
Yeah, that one was a shorter one.
But yeah, essentially, yeah.
All the examples are there, and we have a full list of methods that you can use.
Like here, there's like just tons of different stuff.
There's so many different things.
We've got like, you know, drag and drop.
We've got different scrolling methods.
You have hover and click.
You can get the cookies from a website.
You can get a whole list of elements, etc.
There's a lot of cool stuff that you can use here.
So note that mouse click uses a simulated mouse click.
Whereas there is another GUI-click section where it's actually going to use piato GUI
to physically move the mouse and click a certain element on a web page.
So there are options here.
Also, once you've found an element, the element itself has some
a few different methods that you can use from within it.
So yeah, so those are the CDP mode docs, and that's all available from the
SlendingBase GitHub page.
You just scroll down, you'll see the whole CDP section here,
and you get to read about and find out how to build all these scripts yourself.
So yeah, that is the CDP mode help docs.
So if you have any questions, you can go to SlendingBase discussions.
I also showed you the Discord link earlier.
Easy to find me.
If you found a bug, SlendingBase issues, you can find that.
Also, final remarks, you know, SlendingBase gives you the tools you need to succeed
and tools to build lots of bots.
So yeah, that is the end of the presentation, and I hope you have a lot of fun.
Just note that there are plenty of other examples that you might be interested in running.
For instance, if I go into the CDP mode directory, which has,
if I do like a PWD, you can see the GitHub SlendingBase example CDP mode,
so find all these other examples that I didn't necessarily get to run.
So for instance, if you want to learn about collecting XHR requests,
you can do Python, Raw, XHR, and then it's going to basically go into,
say, website, learn.microsoft.com.
It will scroll it a bit so that it gives time for various XHR things to load.
And you can see here the request URL and the response body.
So this is essentially like, you could use this as a replacement for SlendingWire,
which is previously used for similar things.
So that's an example of that.
Also, if we do Python, Raw, REC, actually, RawResSB,
that's another example of collecting requests and responses on a website.
So we'll scroll up.
If we scroll up, you'll see that there is a request will be sent,
response received, et cetera.
So it's basically grabbing all the data that would appear in your network tab.
So yeah, there's a lot of cool examples of just going to the SlendingBase examples
folder CDP mode.
All the examples that I showed you here earlier are there.
So give those a try.
Yeah, everything is easy as bypassing captures to all the advanced anti-bots.
That's all there.
So yeah, enjoy having fun with those.
And of course, see me if you have any questions.
And note that I am not the only game in town.
Just want you know that there is lots of other stuff CDP repos out there.
So yeah, take your pick.
You might have favorite ones.
Like if you're a Python developer, that is the most common one.
But if you like JavaScript, there might be like one or two stealth CDP ones for that.
Just take a look.
But anyway, thanks for watching this presentation.
And I will talk to you all later.

############################################################

[6/44] VIDEO: Hacking websites with CDP (Chrome Devtools Protocol) and Python
URL: https://www.youtube.com/watch?v=vt2zsdiNh3U
------------------------------
(Source: Original Transcript)
Coming up on the Hacker Show. Intercepting requests, responses, and XHR with CDP, the Chrome DevTools Protocol.
Modifying requests using a method called CDP.Fetch.ContinueRequest.
Controlling browsers via the remote debugging port, bypassing captions and antibody defenses,
and live demos of all the above with Python.
Get ready for some serious hacking.
Welcome to hacking websites of CDP, the Chrome DevTools Protocol,
and we're going to be using CDP for lots of things, such as in the screenshot example here,
we'll be using fetch.ContinueRequest, which lets you modify requests and change websites,
like you see here. We'll get to that shortly.
So the Chrome DevTools Protocol is the key to communicating with Chrome,
and it can be used for various things, such as debugging, etc. It's very powerful.
And if you're coming from Microsoft Edgeworld, there's a slight name change on that.
It's called the Microsoft Edge DevTools Protocol, but it is the same Chrome DevTools Protocol.
As it says in the documentation, it matches the APIs of the Chrome DevTools Protocol.
So same thing, different name, if you're coming from Edge.
And this, of course, is the follow-up to my previous video,
undetectable automation for the Chrome DevTools Protocol,
where basically I showcased how to bypass various captures and antibody defenses
with CDP, the Chrome DevTools Protocol.
So it's pretty powerful, and it can be used for a lot more than that.
And the examples in that video were using a framework I created called SlendingBase,
specifically the CDP mode inside of there, which, if you go to the SlendingBase GitHub page,
you'll see that there is a CDP mode section.
And that, of course, became SlendingBase's most popular feature,
as it became trending on hacker news shortly after I posted a link to that.
SlendingBase, Python APIs for web automation and bypassing bot detection,
and that received 177 points.
So yeah, the people on hacker news were impressed.
And they were so impressed that actually the GitHub Star history showed a parabolic trend
right in December 2024.
It's still December, by the way, if you're watching this after that.
But essentially, lots of people came and started the repo,
and then it became trending on GitHub becoming the most popular GitHub repo in any programming language
for the month of December, gaining thousands of GitHub stars all in a very short period of time.
So the framework became quite popular.
And the Chrome DevTools Protocol is the key to doing all the fancy things
that I'll be showing you today.
So for instance, there is fetch.continueRequest,
which lets you continue a request made to the web browser,
where you can optionally modify some of its parameters, such as the URL,
the post data, the headers, et cetera, so that you can get different content
appearing inside your web browser than what was actually delivered to the web browser.
In order to access the CDP APIs, we're going to be using one of my Python repos My CDP,
which basically translates Python APIs into the CDP APIs.
You'll see here Python method with the same arguments that the CDP methods would have,
but it's all in Python.
And we're going to be accessing that method from slinning-based CDP mode.
So here's an example here where we import my CDP,
and then from slinning-based import esp, it's pretty much all the imports you'll need.
And then in this async example here, we're going to create a method that basically captures all images that appear,
going into the web browser, and then it's going to make a modification.
So instead of having the URL that it had, we're going to give it a new URL,
and then we're going to do, we're going to call tab.feedcdp with mycdp.fetch.continueRequest using the request ID and the newer URL,
and that's going to basically change the data.
We're going to be using a few terms here that you might not be familiar with already.
For instance, XHR, which stands for XML HTTP request,
which is used for interacting with servers, and basically allows you to change the data on a web page after it has already loaded.
Another important term that we'll be talking about today is the remote debugging port.
Now, this is a special option feature of Chrome,
where basically you can use the remote debugging port in order to take control of an existing Chrome browser that's already open.
By take control, I mean like totally hijack the Chrome browser if you know the IP address and the remote debugging port,
and you have the permissions to access it.
It's quite a powerful feature, and it already exists in Chrome.
Let's get to the fun part where we're going to be showing off some live demos.
And of course, if you're a fan of the movie hackers, there's going to be a lot of awesome hacking involved,
and all this code is available open source on GitHub so that you can try out these examples for yourself after you've seen me run through them right now.
So let's get to that.
For the first example that I'll be demonstrating here, we're going to be using a website called Getty Images,
which basically lets you purchase high quality printouts of images from various events and conferences.
So here, we've got a simple Getty Images search, and we can easily perform that with the slanting-based framework.
So if we do Python, raw, Getty Images, we're going to go to that exact URL by doing the full search for it.
ComicCon 2024 sci-fi panel.
You're going to see the images, and now we're just going to paint a green dot on all the images just for fun.
If you're wondering what that script looks like, we can just go open rawgettyimages.py,
and you can see that we're going to activate CDP mode with that URL.
Also, this line here, if you're not familiar with it, we're going to set UC mode to true.
We're going to make it a test. We're going to set the low calcode to EN in case different countries see different things.
We're going to set the page load strategy to nuns so that there's no extra delays.
And that's, of course, after importing SB from slanting-based.
Then, once we've activated CDP mode, we're going to click the editorial button,
and then press keys. We're basically types text at a slow rate.
ComicCon 2024 sci-fi panel, and then the backslash end is just to hit return.
Then we're going to find all the elements on the page, which are the images, and then loop through them,
and then flash the element basically, meaning that you're going to paint a green dot,
and then we're going to sleep for a short amount of time so that we can see it all happen.
That's the test we just ran.
For the next one, we're going to be using this search here, Jonathan Freak's Cast 2022,
which shows Jonathan Freak's and a lot of Star Trek actors,
but we're going to be using the CDP methods in order to modify those requests that come in so that the images change to something else.
So, if we call Python rawrecmod.py, and then just run that,
we're going to do that same search, but now you see all the images have been replaced by a photo of me at ComicCon with my wife, and Jonathan Freak's.
So, if you want to see what that one looked like, we can do open rawrecmod.py,
and we're just going to go through all the code there.
So, after importing my CDP so that we can perform advanced CDP calls,
we're going to call from Sunnybase and port SP,
and then we're creating an Async method, request paused handler, which takes the event and the tab,
and then we're going to get a few things from there,
and then see all the images that are appearing by going to capture all the images,
and then modify them.
So, we can use, after setting the new URL, so for here, that's the photo of me at ComicCon,
we're then going to call tab.feedcdp with mycdp.fetch.continueRequest with the request ID in the new URL,
and that's going to make all the images change to that URL.
And here's the Sunnybase code that called it.
We're going to call the SunnybaseContextManager.
We're going to activate CDP mode.
We're going to add the handler.
So, sp.cdp.add handler with mycdp.fetch.request paused with the request paused handler that we defined above here,
and we're going to open the URL.
And then after it automatically goes through with the Async call and it modifies the images,
we're then going to change the size of the images that they're all the same size.
That is the code that you saw there.
I'll run it one more time.
PythonRawRecommod.py.
Here we go.
The Jonathan Frakes Cast 2032 photo, and all these images have been modified as you can see there.
That's pretty cool.
You can see that is not what appeared on the original site, but we did modify all the images so that instead of what you should get,
you get that image seen right here.
So, pretty cool.
So, that is just a simple example of modifying requests.
All right.
So, for the next tutorial, we're going to be taking control of existing Chrome browsers using the remote debugging port.
So, for that, we're going to call, say Python, testno.py with UC mode,
and then we're going to add dash, dash trace so that it sets up the Python debugger right there.
So, it doesn't close the browser window.
And then in a separate browser window, we're going to call, say Python, control.py,
so that it basically takes over that existing Chrome browser using the remote debugging port,
and changes the website, and prints out the new page title that appears there.
So, you can see there, CDP mode, slanting based docs.
You want to see what that code looks like.
Let's go there and take a look.
So, if we go open control.py, you can see that we call the async method where we set the host and the remote debugging port.
And 9222 is the default remote debugging port for UC mode if you're not setting one.
So, we just go in, we change the URL that you're on, you print out the document title there.
So, that is using an async method.
We can also do the same thing using a less async approach.
So, if we do Python, control.py, we're going to go in and modify the page again and do the same thing.
If you want to see what that looks like, open control.py.
You can see here, it's no longer using an async method, but we're still using the async.io library.
We're still setting the host and the remote debugging port in a different way, but we're setting things up so that you can still take control of the existing browser.
So, you can do fun things there.
If you're wondering where that code comes from, you should go to the slanting based GitHub page and do a search for issue 3354,
where basically someone was wondering how to take control of an existing Chrome browser with the remote debugging address.
And I showed multiple examples here, which I just ran here.
Here's the one that uses an async method.
Here's the way that basically changes it a bit, so that we're using looped out run until complete in order to basically call async stuff from a non async context.
And then here's the simplified SP CDP sync format, which still uses async.io, but it basically simplifies what you need to do in order to take control of the existing Chrome browser, assuming you know the remote debugging port.
So, that's that example there.
And of course, if you're wondering about the format for that, you can click in here and you can see all the syntax formats in the, there's a slanting based page right here.
There's 25 syntax formats basically design patterns where you can structure your tests a different way.
And here's an example of calling the CDP driver with the non-celenium browser.
Many of the examples will just use the simple SP context manager that you can find syntax format number 21, slanting based SP, the Python context manager, and you can call CDP methods from there by activating CDP mode first.
Let's move on to another example where we're going to do some simple web scraping.
So, let's go to the CDP mode area and let's call Python raw theaters so that we can go to a website that has a little bit of antibody detection there.
And essentially, we're going to scrape the data from all the ancient Roman theaters that are all around the world.
And then, you know, basically just show that scraping a website.
So, here we go. Top 30 ancient Roman theaters.
You'll see that they're just all over the Mediterranean area, you know, Spain, France, Turkey, you've got like Athens, Greece, you've got Ksaria, Israel, you've got other places in Italy, etc.
There's just so many places where the Romans took over during those ancient times, but that's scraping data.
If you want to see the script for that, let's go open raw theaters. Let's see that.
And here we go. From slanting based import SP with SP, you see equals true, test equals true, locale code equals EN.
And then we're going to set ad blocking to true so that we can get rid of like the ad content that appears there.
Then we're going to set the URL, activate CDP mode, we're going to click a pop-up that appears.
And then we're going to loop through all the elements that are there and essentially go through and basically paint a green dot on the text on the page.
And we're also going to print that text out so that you can see it right here.
So that's just a quick example of simple web scraping.
For the next live demo tutorial, let's jump into XHR land where we're going to be capturing XHR requests that appear from server requests.
Let's do Python raw XHR sp.py.
We're going to go into the Microsoft learn website.
And there's a lot of XHR that's going to be appearing there.
And you can see if you scroll up, here's the XHR request URL and then the XHR response body.
So there's just tons of data that isn't normally seen on a website.
But you can easily pick it up just by capturing the XHR requests and then making the call.
And then all of a sudden you got all that data.
So for instance, here you'll see there is browser dot events dot data dot Microsoft dot com slash one collector.
That's basically their analytic software where they're collecting certain data from the visitor.
If you're wondering what that looks like, we can open it.
We can go Python raw XHR sp.py.
And you can see here we've got a bunch of different imports that we're using this time.
But we're going to basically create the async handler method so that we can capture all those requests.
And another one where we can receive the XHR.
And we're going to basically go through after we've captured things and print out the data that you see here.
So that's just a very fancy example of printing out the XHR requests that come into the browser.
And there's also an async way of doing the same thing.
It's mostly the same, but there's going to be more async calls involved but slightly different amount.
So here we add the non async version.
And then when we call it here, we're creating the event loop.
So we're using a little more async.io, but essentially there's a difference here.
And let's do, let's call that method.
Yeah, raw rec async. Let's call that test.
So let's do Python raw rec async.
Oh, I think it went to a totally different example than I thought I was going to do, but let's run it anyway because we just looked at it.
Oh, here we go.
Here's an example where we're blocking the requests that are coming in instead of changing the images.
Okay, I mixed up the examples I had. I have a lot of tabs open, but we'll still get to the example I was going to show.
But essentially in this example here, we're actually going through and we're going to block all the images that appear.
So unlike the earlier example where we modify the images, we're just going to call mycdp.fetch.failrequest with a timeout and then block every single image that appears on that website.
So you can see here it blocked this euro, it blocked that one, et cetera, and it showed how long the test ran for.
So if we go to the actual website itself, you will be able to see that it's actually these are the images you would normally see.
A lot of Nathan Phylian, you know, star of Firefly, Castle, the rookie, other shows like that.
And when we run that example here, you can see that we're going to block all the images just like that.
So CDP is quite powerful in letting you take control and modify various things.
I think the example I was going to show you earlier was this one Python, let's see raw, XHR async.
Oh, here we go.
So here's another async capture of XHR requests.
That's a different example.
That also is similar to the raw XHR SB.
But instead of the non async call we do here, we are going to call it from an async death crawl method coming from the main.
And here we go, we're going to do the event loop for crawl.
Let's run that there.
It's going to be the Microsoft learn site again.
So let's do Python raw XHR async.py.
And here we go.
It's going to go through.
It's going to scroll through it again.
And after it finishes scrolling, it's going to print out those XHR request URLs with the response body.
So, yeah, that is capturing XHR requests.
And since we're already going through the examples in the CDP mode folder, there are some other good ones that you might be interested in seeing, such as, let's see, Python raw social blade.
Which basically is an example of bypassing a Cloudflare Capture and then scraping a lot of YouTube data from my YouTube channel.
And, oh wow, we've got a lot of views already.
99,000 views already for my videos getting close to the big 100k.
And here we go.
We've got my social blade rank, subscriber rank.
Yeah, hopefully these numbers go up after I publish a few more videos like the one I'm doing right now.
So, let's do a few more fun things.
Let's go do an example where we do a, let's do a Walmart search.
That should be fun.
Here we go.
We're going to do a search for, let's see, Settlers of Catan board game.
I think we actually did this same example from my last YouTube video, but it's a fun one.
We did some simple scrap, web scraping by going to the website and getting all the items.
If you want to see what that looks like, open rawwallmarts.com.
And here's the code there.
You can like look through it at your own time, because it'll be on the slanting base GitHub page.
But I think one of my newer examples was calls.
I don't think I demoed that last time.
So, let's do Python raw.coals.py.
And let's see, let's do a search for Mickey Mouse 100 Friends TL pillow.
Okay, here we go.
A bunch of Mickey Mouse pillows.
As you can see there, we're going to scroll through and loop through.
So, there's a bunch of stuff.
And after we've gotten through all that, we're going to print all those out.
Just a demo that web scraping happened.
As you can see here, in the output, all these various Mickey Mouse pillows.
So, yeah, that is web scraping.
And of course, you'll be able to find all these examples from the slanting base GitHub page.
Just go to the examples folder once you've gotten there.
And then click on CDP mode.
And from there you'll just find all these examples so that you can practice hacking
on your own time and learn how all of it works.
There's a lot there.
Definitely check it out.
It's pretty cool.
That is slanting base.
And of course, don't forget, slanting base CDP mode has a lot of instructions.
There's the first video that came out.
And I'm sure the next one will appear there soon.
And it'll have all these code examples that you can learn from so that you can figure out
how to automate and web scrape and bypass captures and use CDP for modifying requests
and capturing XHR, et cetera.
It's very powerful.
And have fun with that.
And that pretty much concludes this tutorial.
I hope you have a great 2025 because today is December 31st.
And New Year's Eve is tonight here.
So yeah, have a happy New Year.
But by the time you watch this, it will probably most certainly be 2025.
Check out the tutorials on the slanting base GitHub page.
And I'll see you all later.

############################################################

[7/44] VIDEO: Unlimited Free Web-Scraping with GitHub Actions
URL: https://www.youtube.com/watch?v=gEZhTfaIxHQ
------------------------------
(Source: Original Transcript)
Coming up on the hacker show, unlimited free web scraping with GitHub actions,
using GitHub secrets to hide within open source,
launching your own free local proxy server using IP tables to make a proxy server public
and multiple live demos after the previews. Get ready for some serious hacking.
So this is unlimited free web scraping with GitHub actions. And yes, that means bypassing bot
detection, such as with the anti-bot services you see below in the screenshot. But first a little
about me, I'm Michael Mints and I created the SlendingBase Automation Framework and I also
leave the Automation team at iBoss. And here's a fun fact. I once showed SlendingBase to Sam
Altman at MIT. And for those of you who don't know who Sam Altman is, he's the CEO of OpenAI. And he
also co-founded OpenAI with Elon Musk. But don't worry, you don't need to be one of the OpenAI
founders in order to get a SlendingBase live demo from me because you might see me at a local
Boston meetup, such as Boston Code and Coffee. So it's a popular new meetup where I recently gave a
actually this presentation that I'll be giving right now. So that was a presentation I gave a few
days ago. And if you're not a Boston Code and Coffee member, you might also see me at one of the
Boston Python meetups. For details on that, you can just go to the Boston Python web page. And they
also do regular coffee meetups called Python over Coffee. And here's an example of one of the
meetups that happened recently for that. So if you like Python and you're in the Boston area,
there's lots of Python places for you to go. Recently, SlendingBase was trending on GitHub and it got
over 3,000 stars within a month period. And it became the top trending repo for any programming
language for the month. With spoken language English, it became really popular due to some of
its advanced features, such as CDP mode. CDP mode provides an advanced stealth capability while
you're automating a web browser so that you can bypass bot detection. And that's where lots of
recent SlendingBase popularity came from. That stealth is enough to bypass bot detection while
web scraping from GitHub actions. If we go over to the GitHub actions tab I have here, I'm using a repo
MDMense undetected testing where I basically demode this ability where I can scrape data from a
website that has cloud flare protection. You can see here, I'm grabbing my YouTube stats.
And this example below here, I am web scraping the prices of Nike shoes from the Nike website.
And in this example here, I am web scraping prices of hotels directly from the price line website.
So if you want to know what these examples look like when run directly from a web browser,
I can run a fee right now. So let's do Python my socialblade.py and we're going to go through
and we're going to bypass the cloud flare capture and then we're going to go in and scrape
the data. And I'm just scrolling the web page here for fun because you don't really need to scroll
this particular one to get the data. And you can see the stats here just as you got it in GitHub
actions by passing the capture there as well. Another example that I ran in GitHub actions that I'm
going to run here locally for you is an example where we're web scraping prices from the Nike
website. So here, researching for Nike Air Force One shoes and then it's going to go through and get
the prices of all the shoes that I found. And in the third example I had from GitHub actions,
it was going to price line where essentially we were going to web scrape data right from the
price line website for hotels in Portland, Oregon, USA. So it's going in selecting the input that
it needs. And then it's going to get a list of the hotels and then it's going to display that
data after it just goes through and scrolls for funds. You can see some of the hotels that it's
collecting data from. And here in the output you can see the hotels with the prices.
So there you go, that's just exactly what was going on in GitHub actions for the web scraping.
These sites all use advanced anti-bought protection. And with GitHub actions and Selenium based
together, you can web scrape any data that you want. GitHub actions is free for public repositories.
That's great news if you're on a budget. You can scrape all the data you want.
There's lots of power behind GitHub actions. It's got hosted runners so that you can run your code
on GitHub action servers hosted on Azure. And don't worry, if you need to hide sensitive
information while using GitHub actions for your open source projects, there's a cool feature called
GitHub secrets. And that removes the limitation of being 100% open source while still being 100%
free. Using secrets in GitHub actions lets you store anything you want inside a string that no one
else can see. And you could have over a thousand different secrets, basically a thousand organization
secrets with 100 repository secrets and 100 environmental secrets. And don't worry, the secrets can
be very big because they are limited to 48 kilobytes in size, which is pretty big. And in order to create
secrets for repository, you just go into the settings section and then you can go into the secrets tab
and then you can view that data, create a secret, and then essentially be able to store all the data
that you want. In order to use secrets in a workflow, you can follow the model scene here in this
YAML file where you'll have steps that you set right here and you can define something such as
super secret as an environmental variable. And I'll grab it from the secret that you set within
GitHub actions. And then when you want to use that secret, so after you've set it in your YAML file,
you can create a Python file and you can do import OS and then do my secret equals OS.inviron
with the token that you specified above from your GitHub actions YAML file. And this will allow you
to pass the secret that you created in GitHub right to your YAML file of GitHub actions and then set it
to use it inside your Python file. So that is the secret to GitHub secrets. And up next, we're going to
talk about how to create an instant proxy server which is faster to launch than making instant coffee.
There's a command called s-based proxy and that's all you have to do and that basically launches
a proxy server using the Selenium based dependency proxy.py which uses that. And also if you want to
modify the fault port you can, the fault port is 8899, but you can change it by setting dash-port equals
port. And then as I mentioned before, that proxy server is being initialized via proxy.py.
And you can easily configure a proxy with Selenium based by basically setting an argument either with
a PyTest command line option as seen here with the PyTest dash-proxy equals host-poline port
or you could also set it with the Selenium based SP manager, SP proxy equals host-poline port there.
That's the secret to proxy servers and how to use them with Selenium based.
How about opening up a proxy server to the rest of the world? Well, there's a cool Linux tool
called IP tables which is a very powerful utility and it comes pre-installed on most Linux distributions
and it basically lets you control and manage the incoming and outgoing traffic that's going into
your Linux servers. And if you're wondering how IP tables works, here's a quick step-by-step guide
covering all the major details that you may want to know. For instance, if you want to connect to
your server, you do that and then you do sudo su dash in order to gain the root access that you need.
And then if you want to list current IP tables rules, you could do IP tables dash L and that'll
list all the rules currently visible inside your IP tables on that Linux machine. And then to open
a port for incoming TCP traffic, you'd use a command such as IP tables dash A input dash P TCP dash dash
8899 dash J except and then you're going to set that incoming port and you'd do the same for
outgoing TCP traffic. If you need it, IP tables dash A output dash P TCP dash dash D port 8899 dash J
except and all of a sudden you've set up your Linux server so that your proxy server can
accept incoming connections and essentially be used for anyone else trying to use that proxy server.
But if you're already using GitHub actions, then you might not need to use the proxy server at all.
And that is of course the secret to making a server public. If you have a nice stack of Raspberry
Pies like in the screenshot here, it's quite easy to connect to them, launch an instant proxy server
and then use IP tables to open it up to the rest of the world assuming your stack of Raspberry Pies
is associated with an IP address. Let's move on to some of the live demos because that's going
to be one of the highlights of this presentation. You saw a few earlier where we're doing simple
web scraping, but there's of course a lot more examples with capture bypass that you might be
interested in. And of course, let's get on to the first one where we're going to be using
space proxy in order to start the proxy server. And then if we want to see data appearing in
that proxy server, we can do something such as, let's see, let's exit that out. Let's go into the
actually the examples folder is good enough. Pytest, my first test up UI, dash dash proxy equals
127.0.0.1 colon 8899. And we're going to launch the test. And you can see that as the test ran,
data came into the proxy server so that you can see the requests that were made. So let's run that
one more time so you can see it. It's running a simple test like that, but if we run it and then
switch to this window here, you can see that it's filling the data on here. There are lots of other
examples. So for instance, if we go LS, because right now we're in the slunny mace examples folder,
there's a lot of different examples here. There's also a CDP mode folder, which is specific for the
CDP mode tests, because this is the super stealth ability in order to bypass captures in the most
effective way. So let's do an example Python raw Albertsons.py. And this is an example where we're
going to basically go to a shopping site, and it's going to go in and do a search for avocado
smoke salmon. And then after it does the search, it's going to go through and get the results. So
here you have 87 results for avocado smoke salmon. Now let's say we want to run this exact same
test using a proxy server. So let's open up the file open raw Albertsons.py. And let's say we
want to set the proxy info here proxy equals 127 dot 0 dot 0 dot 1 colon 88899, which is basically
the proxy server info that we set before. And now we're going to go ahead and run that script
Python raw Albertsons.py. And while it's running, we're going to basically take a look at the data
coming into the proxy server. So here we have all this data coming in. You can see it's going to
collect all that data here. And that data is basically coming in. So for instance,
it's got TikTok analytics and cookie law analytics, etc. Basically showing you that you can collect
all the data using your proxy server from whatever example that you just ran. Let's do some more
proxy automation. So we're going to open raw tiktok dot py. And we're going to change proxy settings.
So we're going to go proxy equals 127 dot 0 dot 0 dot 1 for the local host and then port 88899.
And then once we've set that, we're going to run it. So Python raw tiktok dot py. And in this panel
here, we're going to see the data coming in. And this shows that the proxy server is handling
requests because you can see all this data is loading. And now it's going to go through and just
go through the Star Trek tiktok channel. And it's just scrolling now, but it looks like it's already
collected the data that we're interested in. So this shows that the proxy server is working with CDP
mode. So that's that example. Let's move on to another example where we're going to do the same
with the Walmart test. So we're going to go open raw Walmart dot py. And we're also going to change
the proxy settings there. So proxy equals 127 dot 0 dot 0 dot 1 colon 88899, end quote comma.
And then Python raw Walmart dot py. And then while that's running, you can see the data going in.
So we're going to do a search for settlers of the 10 board game. And you can see all this data coming
in to the proxy server. So you can see here, it went through. So that's just another example of
collecting data via your proxy server. Let's run another example. Let's do Python raw cf dot py. And
here's an interesting one because we're going to bypass Cloudflare protection on Cloudflare's very
own website. So let's see if we can do it. Oh, there we go. Success. So this just shows you that
we can bypass Cloudflare's best anti-bought defenses right on their own site. We're going to run it
again and boom. Py out of gooey move the mouse, click the button. And we bypass the capture showing
that it is quite possible and quite easy to bypass your captures with the sending base CDP
mode automation. And as we've demoed earlier, you can run all this in GitHub actions and bypass all
the captures that you need to bypass in order to scrape the data that you want to collect.
Let's talk about the outline of a GitHub actions YAML file. If you have a GitHub actions job that
ran, you can click on workflow file from the run detail section on the GitHub actions tab.
And then you can see the specifics about what the script is made of. So here we're setting the name,
CI build three. And then you can have the script run on a certain cron schedule. So here on schedule
cron 38 star star star star, which basically means that this script will run on the 38th minute of
every hour. And then you can also run on a push to a branch or a pull request or a workflow dispatch.
So here we're going to set the jobs, the build. We can set an ENV. We can set the strategy,
such as the matrix where we set which OS to run on, such as in this case Ubuntu latest. And we
can set the Python version here. And then with the matrix, we can basically set the steps where it uses
actions check out before. And then actions set up Python V5. And then you can set your Python
version to use with the matrix with Python version. And then you can give a name, a run command,
where basically we're setting up various environmental variables in order to maximize the stealth.
And then we can install slanting based dependencies as seen here. And then when we finally get to
running the script, here we are. We can do Python, rawsocialblade.py with dash dash to bug.
And then there's also the Nike example and the price line example, basically showing you how to
quickly run your Python slanting based CDP mode script from GitHub actions with unlimited
capture bypass. That's the example taken directly from MD men's slash undetected testing, a repo
where I'm basically testing all the CDP mode examples that I have to show that the stealth
ability works. Be sure to check out the slanting based GitHub page for all the other information
that you might not have caught here today, but there will be more tutorials to come. And we can't
wait to show you more. Have a great night everybody and enjoy your automation.

############################################################

[8/44] VIDEO: SeleniumBase Recorder Mode 🔴 / Web Test Generator
URL: https://www.youtube.com/watch?v=eKN5nq7YbdM
------------------------------
(Source: Original Transcript)
Hi, I'm Michael Mints, and today's slenium-based tutorial is going to be on Recorder Mode,
which lets you record and export browser actions into test automation scripts.
The fastest way to use Recorder Mode is through the Desktop app which you can launch by calling S-Base Recorder on the command line.
So, if we open up the slenium-based console scripts which you see here,
you'll see that Recorder is one of the commands,
and you'll also need at least slenium-based 2.3.0 to activate it.
However, a newer version also works.
So, let's go ahead and type S-Base Recorder on the command line.
You'll see that it spins up this Desktop app that allows you to choose a file name for your recording
as well as a starting URL, and then you have a few other controls such as regular playback or playback in demo mode.
So, let's start by doing a recording on an advanced e-commerce website.
So, let's do www.saucedemo.com and click record.
That's going to start the recorder or a slenium-based in Recorder Mode,
and now you can start recording your actions that you want recorded or performing the actions that you want recorded.
So, I'm going to log in as the standard user and I'm going to put in the password here.
I'm going to click log in, then I'm going to add something to the cart,
and then I'm going to click the cart.
I'm going to click checkout.
I'm going to type in a fake first name and fake last name, and then fake zip code.
Then I'm going to click continue.
It shrinks the screen so that my face isn't covering it.
Then I'm going to click finish, and then I'm going to switch into assert text mode by clicking shift 7,
and you'll see that the red border has turned into teal.
So, I'm going to click on this text here, which is the thank you for your order,
and then I'm going to do shift 6.
You'll see a pink background appear.
That switches the recorder into assert element mode.
Now, I'm going to click on this image here, the pony express image,
and let's say we're done recording.
So, I'm going to go back to the console here and type c to continue,
because technically, we were in a pi test debug mode.
And now, you'll see that it recorded a script.
So, it has me opening up the URL that I typed in,
followed by typing in the text and the password for this website,
clicking the login button, clicking to add an item to the cart,
and then all the actions that I perform, such as checkout,
building in my first name, last name, or fake names,
and if I exit code, clicking continue, and then finish,
and then, as you can see here, I did a special assert text mode with the shift 7,
which allowed me to create this line here.
Thank you for your order, which it verifies in this selector on the page.
And then also, the shift 6 mode for asserting an element gave you this line here,
self-doubt assert element, image, alt equals pony express.
So now, it's verified that the script was recorded properly.
I'm going to click the green playback button.
So as you can see there, it played back the script.
So now, let's also try playing back the same script, but also in demo mode,
which lets you see what actions are being performed by the web browser.
So I'm going to click on playback demo mode.
Let's shrink the screen a bit so that my face doesn't cover up the screen too much.
So you can see it's now doing everything in demo mode,
which is highlighting the actions that the browser is performing.
It's going to click finish, and there it's going to do thank you for your order,
where you can see what's being asserted, and also asserting the image there.
So the first was a text assertion, and then was an element assertion.
So as you can see from that, the recorder was able to both record,
and playback the recording that you made to make sure that everything was working.
And as you can see, the recorder gives you very simplified selectors,
basically giving you the optimal selector for the job,
and keeping the script as tight and as clean as possible,
as seen here in the console output that it printed.
So now let's go back into the recorder mode documentation,
where we can explain a little bit of what's going on here, what you just saw.
So this recorder app that we launched basically is a nice shortcut for commands like this,
where S-base, MK-REC, the name of your file, and then dash dash URL equals the URL you want,
which basically opens up a web browser with the recorder mode extension,
and then drops you into a break point so that you can enter actions into the test that you're creating,
and then leave that by typing C, and then pressing Enter,
which allows you to continue from the break point which you created.
So that is the standard way of running the recorder from the command line.
So let's say we want to just copy paste this just so that you can see that working.
I'm going to close the recorder app, and I'm going to run this particular script directly from the command line,
S-base, MK-REC, newtest.py, dash dash URL equals Wikipedia.org,
so spin up the browser, and it'll also launch recorder mode.
And now let's try clicking on English, and then I'm going to search for food,
and then I'm going to click on one of the food things, such as food preservation,
just a random thing, and let's say I want to assert that that text is there in the test.
I'll do shift 7, the border changes, I click on food preservation,
and then let's say I'm done, I can go back into here, and type C to continue,
and then as you can see here it created the recording,
and this is the slenium-base file that was generated.
I opened Wikipedia.org, I clicked on English, and then let's see,
there's an extra line here because technically when you click on a button that sends you to a different URL,
that's two different actions that were recorded, clicking the button that redirected you to a URL,
and you've also opened up a new page.
Now in order to simplify things or prevent an extra action from happening,
the recorder might create a line self.open if not URL,
which will open that page only if the previous line did not already take you there.
So when customizing your script, you may decide that you don't need that line in there,
and you can remove it, otherwise basically modify the recorded script as needed,
so you can optimize the final test that was recorded.
So now that I have that, and it says here that my recording was copied to NewTest.py,
I'm going to do PyTest, NewTest.py, and I'm going to run that,
and it's going to perform the actions that I did, do food,
and then I'm on the food preservation page,
and that basically had the recording played back to verify that everything was working.
So that's pretty much the basics of recorder mode.
There are a few other things that may be useful to know,
such as the documentation will have everything you need to know about the assert element mode,
which is basically the shift plus six keys together, or the carrot key,
that lets you start clicking on things and asserting the elements that are there,
or you can use the M% key, which is shift plus seven,
which switches you into a assert text mode,
which lets you assert text on the web page instead of elements.
And in order to switch back to regular recorder mode,
just press the escape key once,
if you're already in assert element mode or assert text mode,
and you'll go back to the regular recorder mode with the red border,
or if you want to leave recorder mode entirely, press escape again,
and to get back into recorder mode if you've escaped it,
you can press the tilde back tick key,
which is located directly underneath the escape key on most keyboards.
So for extra flexibility, the S-Base MK-R-E-C command,
or MK-REC, however you want to call it,
that's basically combines four different actions.
The S-Base MK-File testname.py dash-R-E-C,
which creates a new empty test with a breakpoint in it,
and then it runs pi test with that in recorder mode,
in order to let you add in your actions.
At the end of that, then that gets saved into the recordings folder
with test underscore name, or whatever you call it,
underscore REC.py, and it prints that so that you can see exactly
what the test was when it was printed out.
As you can see here, it printed out the test after it was done recording,
as well as here.
So if we go back into here, so that's S-Base print command,
another console script, which basically prints the output of a file
right to the console,
and then finally, it copies the recording back
from the recordings folder to the folder where you initiated
your pi test run command.
So that is pretty much the basics of recorder mode,
and you may want to familiarize yourself with breakpoints,
such as import IPDB, IPDB.settrace,
which lets you create a breakpoint in your code to pause the test
so that you can then perform actions that get recorded,
and of course, to leave the breakpoint,
you can press C and hit enter,
and then it will resume from where you left off.
And for any more important information that you may want to know about
how recorder mode works,
and the chromium extension that it runs off of,
the help docs will have all that information for you.
So that is pretty much S-Base recorder mode,
and I hope you enjoyed this tutorial.
Thank you very much, and there'll be more exciting tutorials coming up.
Thank you, and have a good night.

############################################################

[9/44] VIDEO: The SeleniumBase Dashboard tutorial
URL: https://www.youtube.com/watch?v=XpuJCjJhJwQ
------------------------------
(Source: Original Transcript)
Hello, I'm Michael Mints, the creator of Selenium Base, and today we're going to talk about the Selenium Base Dashboard.
The Selenium Base Dashboard lets you, in real time, see the test results as they come in.
So, if you're already familiar with Selenium Base and you run a test with the Dashboard,
you can just use a command like this, pi test test markers, dash dash dash board,
and then any other arguments that you want to include, and then you get a Dashboard URL right here
that you can just copy paste into a web browser. I'm pretty sure I already have this one open.
So, if I paste that in, you'll see that it ran four tests, and they all passed,
and you get a Dashboard display with all the test results.
Now, let's say that you want to host this HTML file that's generated as a regular web page.
Well, Python 3 has this really cool feature called the simple HTTP server,
and if you just run a command such as python-m-http.server and then a port number,
such as, in this example, 1948, it's going to create an HTTP server that will, with that website.
So, that would be displayed under, say, here, localhost pullin1948-dashboard.html.
So, it'll be an exact copy of what you saw.
So, if we run the test again, testmarkers.py, and then with the dashboard,
you'll see that the dashboard is going to update in real time.
So, first there are no tests, and then tests will pass as they run,
and then you get all four passing tests. Pretty cool, huh?
Well, let's do something a little more interesting.
Let's run the dashboard on a test suite where there are failing tests so that you can see what happens.
So, for that, let's use PyTestTestSuite.py from the examples folder,
and then we're going to run it with dash-dashboard, and then a few other things,
such as report, headless mode, etc.
It's going to run these tests, and you're going to see that now,
there'll be some two passing tests, but there'll also be two failing tests in this particular example.
So, as you can see here, the failing tests are arriving,
and you have a link to the latest logs from here.
So, if you click on that from the dashboard, you can see that you can now click,
and you can get more info about what went wrong.
So, in the basic test info file that is generated for failing tests,
you'll have the test that was run, followed by the last page that the test was on,
the browser that you were using, the timestamp, the date conversion,
the time, followed by the trace back stack trace,
which gives you all the details on why this particular test failed.
And in addition to that, you'll also have a screenshot.png file that shows you the exact page
and what it looked like when it failed. So, pretty cool, huh?
So, that is the dashboard, and in addition to this, you can also combine
Pytest HTML reports with the dashboard report to basically create a super dashboard report.
To do that, on your run command, you can switch dash dash html equals dashboard.html,
and if you run this now, when this report completes,
instead of a regular dashboard screen like this, the dashboard is also going to include
the screenshots right on it from the failing test.
So, you don't have to go to the latest logs folder.
So, once that completes, you'll see boom, it automatically combines the Pytest HTML report with the dashboard,
and you have the full stack trace and screenshots right here on this page,
which basically gives you a super report so that you can see, okay, clearly,
okay, there are two tests that passed here. There are two that failed.
Here are all the environmental variables that were set, the test summary, the results,
the test, the stack traces, hey, this fake exception, this test fails on purpose.
Here's a screenshot that was saved along with that particular test, et cetera.
Here's the other tests, slenheim.com and .exceptions, no such element exception.
We're at a fake element that does not exist, and it was not present after 0.5 seconds.
And here's the screenshot for that particular one.
So, this really shows you all the different things that you can do with the dashboard,
such as taking an HTML file and hosting it right on a website by using the Python simple HTTP server.
So, with all these things put together, you have just some powerful test analytics that you can easily, you know, see what's going on.
And if you're curious, if I, what the tests look like, if I'm not running it in headless mode,
I'm just going to remove the dash dash, headless parameter, which basically prevented you from seeing what was going on.
And now we're going to just run the test for fun.
Let's spin up the browser. It's going to click some buttons, go to a website, run another test.
And if something fails, it'll automatically take the screenshot.
And then all that is added into the dashboard report.
As you can see here, as it all combines and gives you the super dashboard test report.
So, that's pretty much all the logistics of Slending Based Dashboards.
And the Slending Based.io webpage has a lot of documentation.
So, if you're not familiar with all the features, it'll tell you in step-by-step details
how all the logging, the dashboards, and the reports all work together,
such as the basic test info file, the page source, the screenshot.png,
all that appearing in the latest logs folder that's generated for your latest test run.
And you have the Slending Based Dashboard.
And we show you that you just add dash dash dashboard to your run command.
And all of a sudden, you'll get the dashboard.
And you can even host this dashboard using Python's simple HTTP server on a port of your choice.
And that gives you pretty much a dashboard on your own webpage, which is pretty cool.
So, yeah.
That pretty much covers the dashboard and super dashboard reports, et cetera.
This is mostly for high test use.
There's also the ability to create test reports with nose tests,
but no one's really using that anymore.
It's kind of obsolete.
Everyone's pretty much on the pi test now.
So, just focus on that.
That pretty much covers everything that I will be covering today.
So, if you, for more details on Slending Based and everything that you did not see covered in this presentation,
you can go to slendingbased.io.
Additionally, you can go to the GitHub page, which you can get a link to from the slending based.io page.
And here you have the GitHub page with all the source code,
and all the examples that you can run.
And if you're ever looking for more examples to run, just go click on the examples folder in Slending Based.
And you've got probably 100 examples that you can run with all the command line options
that are available to you.
Well, thank you for tuning in to Slending Based Dashboards, Reports, and Logging and all that.
Next time, there'll be another exciting tutorial, so stay tuned for more to come.
Thanks for tuning in.
All right, bye-bye.

############################################################

[10/44] VIDEO: SeleniumBase Common API Methods
URL: https://www.youtube.com/watch?v=_yNJlHnp2JA
------------------------------
(Source: Original Transcript)
[No content found]

############################################################

[11/44] VIDEO: SeleniumBase: Have fun with test automation!
URL: https://www.youtube.com/watch?v=yEQeAU_mrg0
------------------------------
(Source: Original Transcript)
[No content found]

############################################################

[12/44] VIDEO: "All Your Base Are Belong To Us" 2021 Edition (created using SeleniumBase)
URL: https://www.youtube.com/watch?v=1s-Tj65AKZA
------------------------------
(Source: Original Transcript)
[No content found]

############################################################

[13/44] VIDEO: Solve Wordle Game using SeleniumBase with Python Algorithms
URL: https://www.youtube.com/watch?v=wSvehy4u_xw
------------------------------
(Source: Original Transcript)
Hi, I'm Michael Mintz, and today's Selenium Base tutorial is going to be on using Selenium Base in order to solve a popular app called Wordal, which looks something like this.
For this, I'll be running some Python code that you see here, and without further ado, let's kick off the test which should launch the Wordal Solver app.
As you can see here, Selenium Base is going to guess a random word at first, and then start trying to deduce what the correct word is based on the hints that are provided.
A yellow square means that a letter is in the wrong place, whereas a green square means that the letter is in the exact place it should be.
As you can see here, Selenium Base solved this particular wordal in five tries. Since it's random each time, let's try it again with another run.
Here, Selenium Base is starting off with a new random word, and from that it's going to try to deduce the correct wordal word for today's puzzle.
And that time, I got pretty lucky, and I got it in three tries, but let's do it again just to show you that. Maybe it's not always so lucky.
I'm going to run it again, pi test wordaltest.py from the Selenium Base examples folder.
Alright, so Selenium Base has entered a new random word, and it's going to keep on entering words until it figures out what the correct word is based on the hints it gets with the yellow and green squares.
It was able to figure out the final word point on its fourth try, which is pretty cool.
So if you're wondering how exactly that works, let's go over the Python code that makes it possible.
So right here is test wordal, and first I make sure that you're not running in headless mode, and that your version of Selenium Base is 240 or newer, otherwise it won't work.
Then we open up URL for the wordal game, and then we click the close icon for a menu box that appears right when you first open it.
Then we set up the selectors using the shadow selectors for interacting with shadow DOM, and then we're going to create a loop because we get six tries to guess the correct word.
We're going to select a word at random from the initialized list of words here.
So that method here essentially grabs the dictionary list of five letter words that were already provided by the website.
So that's going to throw everything into a list, and that will be inside self dot word list.
Next, once we've picked out the random word to start off, we're going to type it in to the first row, and then we're going to click the enter button in order to see what the results are for that particular word.
And from there we're going to use self dot get attribute in order to get the letter evaluation that provides where green is a letter in the exact location that it should be yellow is a letter in the wrong spot, but it's still in the word somewhere.
And the great out spot means that the letter isn't there at all in the word.
Of course, if we have five correct letters, it means that we've successfully guessed the correct word.
So once we've had some hints, we're going to throw the word and the letter status into modify word list.
And if we go over to that method, we'll see that we're going to have a few loops where first, based on the letters that are correct,
words that won't match the criteria and do something similar for present letters and absent letters.
And after all these loops have taken place, we finally have a new word list, which we set self dot word list to, and then we repeat the loop again, basically starting off with a random word from the list of words that are still available after weeding out bad words.
And this loop pretty much continues until you've guessed the correct word and hopefully six tries or less.
So that is pretty much the entire script.
It's less than a hundred lines of code.
And let's just run it one more time for fun because it's after midnight here, which means that we should get a completely new word that I've never tested on before.
So we're going to run and pi test word old test dot py again and see how this next round goes.
And here we go. I have no idea what the next word is going to be.
Robot. Oh wow, guess that in three tries.
Not bad.
All right, let's run it again because three tries is pretty good, but the hints that it provides can make it easy to get it in a few tries if it gets a few lucky guesses in the beginning.
So here we go one more time, pi test word old test dot py and let's see what happens this time.
Here we go, starting off with shine, memo letters are there.
So it's going to try something else.
And it got robot on the fourth try.
So as you can see here, the algorithm that is used in order to try to figure out the correct word is pretty good.
And a simple Python script makes it all possible right here.
So if you're wondering how to see the script for yourself, you can just go over to the slenium base examples folder and that script will be right there.
So let's go over to slenium base word old test and that code has already been checked in and you can check it out here.
So that is the examples folder of slenium base.
And if you scroll down, you'll also see that there is a gift that I recorded previously from the last word that was there.
So this is pretty exciting to have web automation play games for people.
Soon all your lives will be automated just kidding.
Anyway, thank you for enjoying this exciting slenium base tutorial and there will be more to come.
Thank you and have a good night.

############################################################

[14/44] VIDEO: SeleniumBase Test Automation Framework Tutorial
URL: https://www.youtube.com/watch?v=Sjzq9kU5kOw
------------------------------
(Source: Original Transcript)
Hi, I'm Michael Menz, the creator of the Selenium Base Test Automation Framework, and today
I'm going to show you how to get started.
Selenium Base is a combination of the Selenium Library with the PyTest Framework, which allows
you to do really powerful stuff with a lot of additional features baked in.
To get started, go check out the Selenium Base page on GitHub, where you will find a
nice readme with instructions on getting started.
So first you'll need Python installed, if it's not already, and you want to make
sure Python's on your system path.
And if it's not already installed with Python pip, which allows you to install Python
packages, and you'll also want to create a virtual environment, which will allow you
to partition Python installations from each other in case there are different dependencies
required between them.
Once you've got your virtual environment set up and you've cloned Selenium Base, you
can install with just a pip install Selenium Base, or you can do pip install dash our requirements
dot text, and that will install the requirements.
And then Python setup dot py develop to install Selenium Base.
Once you've done that, now you'll need a web driver to run the tests on a web browser.
So let's say to do that, Selenium Base install Chrome driver, and if you have the latest
version of Chrome driver installed, or latest version of Chrome installed, you want the latest
Chrome driver.
So add latest to that command, and it will automatically find the Chrome driver you need and install
it.
And if you want to run tests on Firefox, you'll need Gecko driver.
So just do Selenium Base install Gecko driver.
And that will install the Gecko driver that you'll need to run tests on Firefox.
So once you've done that, you can see the into the examples folder from your get clone
of Selenium Base, and then you can run the first test.
High test, myfirsttest.py.
And by default, if you don't specify a web browser, it's going to run it on Chrome.
You'll see you'll spin things up, the browser, click some buttons, type in some text.
And if you're on the run, the same test in Firefox, just do dash dash browser equals Firefox.
And now it's going to run the same test right there.
So let's see how that goes.
Now it spins up a Firefox browser, as you can see, and goes to xkcv.com, a web comic,
and then performs some actions.
If you're wondering what exactly it's doing, we're going to go into the test, you can take
a look.
So let's open my first test.py, and you'll see you'll have at the top, from Selenium Base
Import Base case, which is the key import, so you can use all the Selenium Base methods,
and have automatic spin-up of the web browser and the spin-down of the web browser during
the test.
And there you'll see like open to open a web page, you can assert almonds or the title.
By using the CSS selector, you can click an element on the page, assert text, and you can
update text, which means typing text into a field.
So and if you add backslash n onto whatever you're typing in, it'll automatically hit the
ender return key at the end of that.
So that's what my first test.py looks like.
Let's do pi test HTML reports.
So let's say we run a pi test test fail.py, test that will fail on purpose.
We do dash dash HTML equals report.html.
You'll see that once it spins up the browser and runs the test, and it fails, you're going
to get a nice HTML report with the screenshots and stack traces involved there.
So open report.html, that a pi test HTML report with the stack trace and the screenshot.
Pretty powerful stuff.
So by default, when running on Linux, it's going to run it in headless mode because
there's not necessarily a GUI screen there, but you can also run test and headless mode
by just adding dash dash headless on a regular screen.
So if we do pi test, my first test.py dash dash headless, it's going to run my first test,
but it'll use the headless version of Chrome or the headless version of Firefox if that's
what you're using.
And at the end of the test, you'll see one past and in the number of seconds that it took.
All right, so let's do something even more advanced demo mode.
So if we type dash dash demo underscore mode when running a test, you're going to visually see
what the test is doing as it performs all its actions.
So for instance, on that test, we're going to assert the title.
Then it's going to assert the CSS selector for the IMG.
Then it's going to click more details and you can actually see all this happening in real
time so that you know exactly what the test is testing.
It's a really powerful feature of the Selenium base and it'll allow you to really know what's
going on.
Literally, the JavaScript is injected onto the page with WebDriver as the test is running.
So there you go.
You have an ability to easily write and run reliable tests that automatically wait for
all the page elements to load in the ready state of the page to be complete because that's
how it's going to prevent flaky tests.
All right, let's go into an example of creating a code list Selenium base script in case you're
new to automation.
You just want to click some buttons on a web page and immediately have a script for that.
We're going to use a tool called Catalon Recorder, which essentially it's a Chrome extension
that you can install.
It's also a same company does Catalon Studio, which does the Catalon Recorder.
So as you just click on something on a page and record all those actions so you can play
it back and export it into your tests.
So let's try doing a record of CL, load the page, Catalon.com.
And now I'm going to go to click on web testing and you'll see at the top right they'll have
the commands that I'm clicking, click on blog, you'll see the command got recorded.
And now I'm on blog and let's click on CICD, there we go.
And that's like enough things to click on.
At the end you'll see all the steps, so now you can do stuff.
And now you can click back the steps that you just recorded just to see that it all recorded
properly.
All right, so pretty straightforward.
Now comes the fun part.
Now we've recorded all these steps.
We can now export this as a Python to web driver plus unit test file.
And then we can convert that into slenium base code.
So to start, let's click on save as file from this giant file.
And let's, we're going to save it into the slenium base examples folder, we're going
to call it test K for Catalon, going to click save.
And now that, now that that test is in the examples folder, let's take a look.
Then test K dot P Y. And you'll notice that it's about 51 lines of code.
And it's got all this extra stuff that I didn't really need because all I really did was
these actions where I opened up a website, and I clicked on elements.
So let's now run the slenium base convert command.
And if you want to know what all the slenium base commands are from the console scripts, you
can just type a slenium base in the window.
And you'll see the commands.
So now let's do slenium base convert test K dot P Y, and it's going to create a test
K underscore S B dot P Y. So let's open that test K underscore S B dot P Y.
And you'll see that the slenium base AI took all these lines of code and simplified it
right down to this.
You open catalog.com, which is what you saw in the test here.
And it used some smart selectors to convert this messy expath into just a partial link
click.
And then you're clicking on the blog and then find element by d dot click.
It literally simplifies all that into really concise short reliable test scripts that
is way more efficient than what you'd get by using regular web driver and unit test.
So let's try running this to make sure that everything's good.
So we're going to do high test test K underscore S B dot P Y. And it's going to spin up that
browser.
And literally you've taken this messy 51 lines of code that catalog and you've slept in
the slenium base convert method is taking all that and just simplified it down to literally
all you really need because the slenium base reliable libraries take care of handling all
the other stuff.
Cool.
So now that we've gotten that we ran it and it's successful.
So we just really quickly took code lists, like automation, clicking and all that.
We record the actions.
We exported it.
We convert it to slenium base and now you've got a really simple script.
So now that we have that we can improve on this even more by using the slenium base objectify
command.
So we do slenium base objectify, let's see test K underscore S B dot P Y. And you'll see
from the output here, page objects dot P Y was created and test K was updated.
And if you go into here, it replaced all the CSS selectors that were there with page
objects that you can now find if you go open the page objects dot P Y file that a simple
command like that took all the CSS selectors and gave you the page object model.
Now now it's going to be slightly confusing to see what happens.
So we're going to show you some of the other things that you can do with the slenium base
page objects commands.
Let's do slenium base revert objects test K underscore S B dot actually forgot the S
revert objects test K underscore S B dot P Y and you'll see we're back to the beginning.
Now let's say you want to be a little more specific as to naming your page objects.
So what you can do is slenium base extract objects test K underscore S B dot P Y and
you literally will discreet the page objects file without modifying test K and now you can
change what you want to name these.
So let's say we call that API testing, we call it the blog link, we call this the category
filter.
All right.
So now that we've renamed these, now we can do slenium base inject objects test K underscore
S B dot P Y and it's going to take the page objects file with all the page objects there
and it's going to map out to back to your test file what you renamed those page objects
to.
You can see, hey, instant page object model, instant converting of a messy long web drivers unit
test script into concise slenium base code.
It's got lots of methods to help simplify things.
All right, so let's go on to the next step, which is more cool fancy examples.
All right.
Let's go into towards examples.
So as you've noticed from demo mode, slenium base has a JavaScript injector that allows
you to do really powerful things with JavaScript on top of the tests.
So I thought, hey, I could use this JavaScript injector to create more types of JavaScript
injections for assisting things.
So let's let me show you an example.
Write test, the Google tour dot P Y and if you run that, it's going to go to Google
dot com and it's going to create a website tour literally injected right into Google in
this example.
Let's see, welcome to Google next, type in your query here, then click here to search
or press enter after that.
But literally, I just created a website tour on Google dot com just like that.
Let's see.
In the tour, I can also use the keys to like scroll through.
And there are also different types of tours that you can use.
So this particular one coming up is going to use a different style than the previous
one.
Welcome to Google Maps and click next search box, click here to show it on the map.
So right now I'm pressing on the keys to take this tour through.
And this is pretty cool because I just like literally took JavaScript and create a
website tour with just few lines of Python code, which you're about to see right now.
And we've got a tour.
Thanks for using Slurney and based tours.
So if you want to see what that code looked like, I'm going to open the Google tour dot
P Y and you'll see I open Google dot com, wait for the element and then I create the tour
and I can add a tour step text that you see there.
I can add an optional title.
When I add a tour step, I can also attach it to an element by using a CSS selector.
It's very powerful.
It's very cool.
And that is Slurney and based tours.
And you can also export your tour as a JavaScript file.
All right.
So I'm going to move on to the next exciting feature, which is master QA.
All right.
So master QA combines Slurney and based automation with human manual verification to create
the ultimate QA experience.
In case you have QA teams, we still want to have a manual component, but you also want
automation to help things go a lot faster.
So here you saw I ran this test and automation performed several actions.
And now you have a manual verification.
This is another JavaScript injection that Slurney and based provides.
Manual check one does the page look good.
I'll say yes.
Automation does its thing.
Can you find the moon?
Nope, no moon fail.
Takes a screenshot if there's a failure.
I can move this around.
It's cool.
I could say that.
Yes, no.
If I do know, get the screenshot.
Do a search for a book.
Do you see books in the search results?
Yes, I do.
I'll say yes, pass.
There's one more for this particular test.
Manual check number five is the page say add normal expressions.
Now it says regular expressions.
I'll say no fail.
And at the end, you get this nice report that you'll see screenshots where things failed.
Additionally, you're going to get a results table dot CSV, which basically takes all those
results and puts it into a nice CSV file that you can then view to see how your test
suite did.
So your manual tester, the automation goes does helps you out.
And then you get this report.
It's like, oh, hey, success for here failed here.
This was the URL.
You're on the screenshot that it took the web browser that you were using the epic time
when the test ran and the verification instructions so that you know what it was being tested.
And you can add additional info in that isn't covered right there.
So that is master QA, a powerful way of combining automated QA with manual QA for the ultimate
experience.
All right.
So that is master QA.
All right.
So let's see.
What else do we have?
Well, there are a lot more tests that you can try out on your own.
You can basically run your tests on a proxy server.
You can do tons of things in order to show you the types of things that I can do.
You go back to GitHub, you'll be able to find a thing called the health docs folder where
you'll find all the help docs that you'll need to help you get started, like the full method
summary, which will show you like all the different methods that you'll be able to use.
And it's quite advanced.
For instance, you can you'll have methods such as like a certain no 404 errors, a certain
no JavaScript errors on the page.
You can do ad blocking, inject JavaScript onto the page, download a file, upload a file.
That's all really powerful stuff.
Let's see.
For it's the customizing test runs, you'll be able to not only choose the web browser,
the user agent, the automation speed, whether to retry failing tests, whether you use a Chrome
data directory or a load of Chrome extension when you run the tests, you can even tell
your test to connect to a Selenium grid server, such as browser stacks, oslabs, testing
bot, or cross browser testing.
So in order to do that, here's an example of running your test against a proxy server.
You could have an IP address call in port or username call in password, IP address port
with dash dash proxy, so that you can maybe say, oh hey, geolocation this test, change
the user agent, change settings, such as default timeouts and all that.
Connecting to sauce labs and browser stack is pretty straightforward.
You can just use a command such as on your test dash dash server equals username call in
key at say hub.browserstack.com or on demand.saucelabs.com, all that.
Now you can run your tests in pretty much any cloud you want.
Additionally, you can create your own Selenium grid if you know what you're doing, and that's
as easy as Selenium-based grid node start, and see, oh, we already had it running, so
I'm just going to stop it, and I'm going to stop the grid hub.
All right, so start from the beginning, because I already had it running before I started
this tutorial.
If I do a grid hub start, it's going to spin up a grid hub for me, and it'll give you
a URL that you can use.
So now if I plug that into a web browser, you'll see you have the grid console for your
Selenium grid that you just spun up if you want to say partition your test to run on
different server machines, and with the Selenium grid hub, you're going to need to start the
Selenium grid node, so let's do a Selenium grid node start, and now that those tests,
the grid node is started, you'll be able, if you refresh the page, you'll now be able
to see all your Selenium grid nodes right up in there, like here are the Firefox browsers
and Chrome browsers, and since I'm running on a Mac here, I'm not going to have like
IE, but if you've had a PC here, you'd have like all the other browsers that you need.
So that is using the Selenium grid controls of Selenium base, easily spin up a Selenium grid
hub and grid node, and partition all your tests there.
Additionally, since Selenium base uses pi test, pi test has advanced features such as multi-threading
and a whole lot of other stuff, so if I do pi test, let's see, test suite.py and dash
and four, it's going to now spin up four Chrome browsers for me and run a suite of four tests,
because test suite has four tests in it, so now you'll see it's spun up the four browsers
and they're literally like one behind another, so it's powerful, multi-threading proxy servers,
change your user agent, change your browser, use a Selenium grid, convert Selenium IDE
or Catalon IDE recordings into a simplified Selenium base script, use website tours, master
QA mode, it's really powerful, the possibilities are endless, and I don't have time to cover
all the features that Selenium base has, but don't worry, there'll be more tutorials,
so I hope you enjoyed this one and happy automating.

############################################################

[15/44] VIDEO: SeleniumBase Commander: GUI for "pytest" scripts & "behave" BDD mode.
URL: https://www.youtube.com/watch?v=gRf7TF95hl4
------------------------------
(Source: Original Transcript)
Hey everybody, it's Michael Mints, the creator of SlingingBase and today's exciting tutorial will be on the SlingingBase Commander, aka the SlingingBase GUI.
So SlingingBase Commander lets you essentially take what PyTest finds and show to you as a display so that you can more easily see what tests are going to be run and what command line options will be used.
So in order to activate the SlingingBase Commander, all you have to do is type S-Base GUI in your test folder and PyTest will collect all these tests that it has and you'll be able to see it right there.
And essentially, it finds the same exact tests that you would find if you just did a PyTest-CO-Q from the command line.
As you can see here, there are 146 tests right now in the SlingingBase examples folder where I am running the script.
So you can see here all the tests that are collected and if we go into the GUI, S-Base GUI, you can see a lot of different command line options that you can select, such as the browser selection, whether or not to reuse the session and the number of threads to be used.
So let's say we want to run a simple test. Let's do the coffee cart tests and let's reuse the session so that everything is done in the same browser window.
So let's run that.
So you can see here it's going into the coffee cart app and it's performing a lot of various tests.
And if you go to the command line here, you can see all six tests passed in 8.03 seconds.
Now the fastest way to run tests is by reusing the browser session.
And if you don't reuse the session, so let's say we just do that and run the same suite of tests, it's going to spin up a new browser for each test that it runs.
And you can see here it's running, it's doing its coffee cart tests, which is one of the cool new examples that SlingingBase has.
If we go in here, you can see that six tests passed and it took 15 seconds this time instead of 8.03 because we weren't reusing the session.
So if you want to speed up tests and have all of them run in the same browser window, make sure to reuse the browser session.
Additionally, you can also run tests using multiple threads.
So let's say we do 8 threads and since this is a test suite of six tests, let's add in two more tests so that we can get 8 threads total.
And let's click to run them all.
And you can see it's spinning up 8 browsers.
And there are always going to be like one behind another.
You can see they're all like right there.
RAN 8 tests in 9.63 seconds. So that's cool.
So you have different options here already available to you, such as verbose output mode.
You also have the dashboards. You can see the test results through that.
And you have, of course, the HTML report.
So in this other window, I'm going to go into the examples folder and let's do open dashboard.html.
You'll see that these are all 8 tests that we just ran and they're all passing.
So now there's also an addition to the dashboard. There's the HTML report.
So we can do open report dot HTML.
And it looked very similar because the dashboard is based off of the report.
But it might have a few more additional things here, such as which plugins were used.
The platform that you're running on, a pi test packages.
This is all part of the standard pi test HTML.
But it adds on the slinning based dashboard to the top of that HTML report.
And if there are any failures, you'll see screenshots and all that.
So let's just go back into the GUI here.
And let's change things around.
Let's go back to a single thread, but we'll still reuse a session.
And let's find some tests that will fail, such as testfail.py.
That should be in here.
So let's run that script.
A lot of different files here.
Oh, here we go. Testfail.py.
And we're going to run that again.
It's going to have the dashboard and the report.
So it's going to run a test that fails on purpose just so you can see what's going on.
You can now see that the dashboard has all read.
And inside the HTML report, it has your stack trace right here.
If I make this a little bigger so you can actually see what it says,
slinning.com and exceptions, no such element exception.
And the element that it was looking for was not present because I basically made this test fail on purpose
so that you can see what happens.
You get a cool screenshot details.
There are other additional things that you have.
If you go directly to the dashboard, refresh that.
You'll see that there is some different logs and data.
I'm going to open this in a Chrome window so that it's easier to watch everything.
So let's go to the dashboard here.
Click on data.
You'll see that there is a basic test info.txt file which has a lot of really cool,
the bugging output which makes it easy to tell what happened.
So this was the test that ran.
The last page that it was on, the duration, the browser and version that I was using,
the driver that it had.
And in this case, Chrome driver should match the version of Chrome not necessarily exactly,
but the major version like 111, 111 should be the same on both.
You'll have a Unix timestamp which is then converted into a date.
So you see Thursday, March 23, 2023.
And the time was at 801 PM.
And I'll even have the time zone information.
Here's the cool part, the trace back.
You can see what exactly went wrong inside this particular test.
So that is, you can see element div pound army of robots is not present after one second.
And you have a lot of cool info showing you details of your trace back.
So that is that.
So that in addition to that inside your latest logs folder, you'll also get the screenshot.
And you'll even get the page source HTML, which you'll see is a file saved to the computer itself.
So if you want to see what happened, it's more than just a screenshot.
You can actually right click inspect and see what's going on with the, you know, the HTML, etc.
Useful stuff for helping you debug something if something went wrong.
So that is the output there.
And if we go back, that is essentially, yeah, it's letting base commander, which allows you to easily select which test you want to run.
I also show you like the number of files that found and the number of tests within those files.
First, I'll list the files at the top, which could contain multiple tests, such as the coffee cart tests, which had six tests.
And then if you scroll down, it'll also have individual tests seen there, such as all the tests that it finds within the particular files themselves.
Now, if you want to slow down tests, note that there is a feature called demo mode, which lets you easily see the actions that a test does.
So let's go inside the coffee cart tests and let's run two of these.
Let's run test by one cappuccino and let's run the context click add coffee and the remove added coffee.
So we're going to run all those in demo mode and we're going to reuse the browser session again, run it in one thread.
Let's run that so that we can see how it all works.
I still had a few of the other tests still selected from below, but now it's running the coffee cart test you can see here.
It's clicking for that total $19 for your very expensive cappuccino.
This is all like fake data going in, so don't worry about fake coffees being ordered from a fake testing website to help you demonstrate how automation works and how to write good tests.
You can see what demo mode it shows you exactly what it's asserting for inside the assertions that it does.
So here demo mode is highlighting all the browser actions that are seen so that you can know exactly what your test does.
Thanks for your purchase, et cetera, verifying only text, but you know, handling button clicks and all that fun stuff.
So that is essentially demo mode.
One of the checkbox items that you'll see within slanting based commander.
There's also the option to use a mobile emulator that's here.
And let's see, there's the option to use a headless browser, which will run all your tests faster.
And if you are using the headless browser, you won't want to use demo mode because you'll just be slowing down your test because demo mode is just there for you to see what the test is doing.
It's quite helpful and debugging and knowing whether or not the test that you wrote is checking what it should be checking.
And also the save screenshots button will essentially save a screenshot at the end of every test.
Otherwise, the screenshots will only get saved when your tests have an error or a failure in them.
That's when the screenshot will get saved automatically in the tear down.
If something goes wrong, but otherwise, it'll save on your megabytes and disk space of your computer by not saving them by default.
Unless you select it here.
All right, so that is the slanting based commander.
In addition to the slanting based commander, which is essentially a commander for the pi test slanting based tests, there's also a behave BDD commander.
So if we go to CD, behave BDD and CD features, and we do S-base, caps lock, S-base, behave GUI.
You'll see that it has the behave features seen and you can run those.
So there's like a calculator test or a real world feature.
And the options are a little different because the behave BDD mode doesn't have multi-threading.
But you'll see why in a sec because basically it's doing a lot of printing out of output.
And if you're running multiple threads, then the print statements would basically overlap and cause issues.
So let's run these two tests. And actually, this one has nine total.
So we're going to reuse the session for all tests so that it goes a little faster.
So let's run that.
And it goes pretty fast when you reuse a session.
All right, so there we just ran 10 different scenarios.
And you can see here in the behave BDD mode, it has a GERKEN formatted steps.
So this might be useful if you want to more clearly see what a test is doing.
So that's a quick view of the S-base BDD mode which runs with behave.
You can also run things directly from the command line.
So if we go to CD features, then inside here you can go in and take a look.
So you can see here, we have a few of these calculator.feature, real world.feature, the steps, swag lag, et cetera.
So if you want to run one of those, you can do behave and then say swaglabs.feature.
And it runs all that and it runs it pretty quick.
This one had a bunch there and a few passing and failing scenarios just so that you can see what it looks like when a scenario fails.
As you can see here in this particular failure, you can see that the values weren't correct because the actual text here was 59.9800.
When we just wanted 59.98.
So if we wanted to see the dashboard on that, that was already selected, which means that if we open it, open dashboard.
And we can see the logs folder. So if we click on one of those and you'll see the latest logs folder, which is generated.
There'll be a screenshot for this one.
Here we go. Inside the screenshot, you can see below if you zoom in.
The item total had an incorrect rounding error.
So in this particular case, here the test found a bug with calculating the price total.
So if you go into here, you can see that that was caught right here.
And that is behave BDD mode. And those tests there were launched with the SlendingBase commander for the behave BDD style tests.
And if you're wondering what those look like, I'll quickly show you.
So if I open, say the swaglabs.feature, you'll see that tests are written very different from the standard Python format because they're using gyrgans syntax.
In order to basically perform all the same actions that SlendingBase would in the Python version.
So that's basically the behave BDD commander.
If we go back into say the examples, I'll show you if we open the coffee cart tests.
It's using a more familiar Python format with tests that inherit base case, which inherits unit test test case.
And these are run with the pi test.
And basically with the test structure you're seeing here, your test should start with test underscore.
And you want to make sure that your file is named appropriately so that it's picked up by pi test collection, which basically shows you the tests that are seen there when you do pi test dash dash CO dash q.
Oh, got to go back. There we go.
Here we go.
So these are the tests that would be picked up by pi test.
And note that most of these will start with test underscore, but some of them were still picked up and weren't because here it had, say underscore test.py in the name.
That's all controlled by your pi test.ini file.
So if we open pi test.ini, you'll see that you can control which tests get collected.
So here if a test starts with test underscore or ends with underscore test.py, that will all get collected by pi test auto collection.
So that's just a quick, you know, jump through a segue into how pi test collection works.
And how those tests get shown up inside the slenny based commander app when you run that.
So we go back into a space GUI.
That's what shows up here.
And that gives you, as you can see, again, all the fancy options you can choose from when running your tests.
So if you have any more questions about slenny based commander or the slenny based commander for the behave BDD tests, you can find all that from the slenny based GitHub page.
Just scroll down here.
All the major features have a link in this section here.
So the GUI button right here had the link to slenny based commander.
And you can also access that from the slenny based docs at slenny based.io.
It also has all the documentation that you can find on the GitHub page.
But it uses the MK docs website generator in order to convert the GitHub read me pages into a fancy website.
So that is slenny based commander and the slenny based behave BDD GUI commander, which looks very similar.
But the tests are in quite differently because one uses regular Python syntax and the other uses behave BDD gerkens syntax.
So if you have any questions about how that works, just check out the documentation and all your questions will be answered.
Well, thanks again for joining in on this exciting slenny based tutorial.
Let me know if you have any questions.
This video will be posted on YouTube very soon.
So if you are interested in seeing more exciting YouTube videos with slenny based tutorials, just check out the YouTube link.
And videos will be there as well as links from the slenny based GitHub page itself.
All right, well, thank you and have a good night.

############################################################

[16/44] VIDEO: Automated Visual Regression Testing with SeleniumBase
URL: https://www.youtube.com/watch?v=erwkoiDeNzA
------------------------------
(Source: Original Transcript)
and welcome to automated visual testing with Selenium Base,
very powerful web automation framework
that you can find on GitHub.
To get started, just go to the GitHub page
and follow all the instructions that you see there.
Let's run a quick example test to help you get started
called MyFirstTest.py.
So you'll be running that with PyTest.
So PyTest, MyFirstTest.py, from the examples folder.
And if everything is installed and working correctly,
it should spin up a browser, navigate to a web page,
click some buttons, type in some text,
and verify the elements are properly appearing on a web page.
Now, that's the base case of Selenium Base, however,
there are a lot more powerful features within it.
So next, we'll be exploring automated visual testing.
To do that, just go to the examples, visual testing folder,
and you'll find a really powerful readme
with all the instructions that you need
to help you get started.
Now, there are other companies out there
that do automated visual testing.
The difference with Selenium Base
is that we think we can do the exact same thing,
but with free open source tools.
So automated visual testing basically
helps you detect when the layout of a web page has changed.
And rather than comparing screenshots,
you're going to compare layout differences
by comparing the HTML tags and attributes
with a version of a web page relative
to a previous version of a web page.
So here's how automated visual testing
with Selenium Base works.
When you set a baseline, it's going
to create a bunch of files that basically store
all the HTML tags, attributes, and values in them
so that you can use those later to see if something broke.
Now, if a test fails, it could mean
that the website was redesigned,
or there might have been a real failure,
or there is dynamic content on the web page,
such as a page ad, that basically changed,
and therefore the test fails
because it thinks something went wrong
when really just you had something else there.
So to demonstrate how this works,
we're going to run three simple tests
that are all located in the test layout fail file.
So the three tests that we're going to run
is the Apple Tools test where we click a button
that's going to make a hidden element become visible.
We're also going to run a test on the python.org website,
where we remove a button, and then make the layout comparison.
And we're also going to run a test on XKCD
where we've modified the attributes of the logo dimensions
that we've changed the height and the width of it.
So let's get started.
To do that, we'll be running PyTest.
Actually, let's go into the visual testing folder.
Okay, now we'll do PyTest, test the out fail,
and then we're going to do our HTML report with it.
So dash dash HTML equals report.html.
So now we're going to run this, and you're going to see
it will spin up the first website, click a button.
You'll see that the website changed,
because an image appeared.
We're going to do another test where we're
going to go to python.org, and then we're going to remove
this donate button that appears there.
And then take the, again, the visual layout of that
before and after.
And again, we're going to go to xkc.com,
change the logo dimensions, and make sure
that the layout test fails there.
So as you can see here, we have the test results.
So if we go to our first test, Apple Tools,
which is technically a competitor,
because they offer a visual testing tool that costs money,
you'll see that in the exception, you will have a hidden
element, and then that was no longer there when the change
was made.
So that became visible.
And you'll see that in the exception,
the visual diff failure HTML tag attribute values
don't match the baseline.
Also with the python.org page, the donate button
that we removed was no longer there.
And therefore, in the previous version that was removed,
and you can see the minus, meaning that, hey,
we noticed the change.
And the visual layout level three failure was present.
And same with the xkcd website, where we changed the logo
dimensions, and you can see here, the height was different
from the height we changed it to,
and the width was different from the width
that we changed it to.
You can see this more clearly if you open the report.html file,
which basically shows the stack trace followed by the screenshot
that it took, where something was different.
So you can see here, OK, clearly there's
a section that was hidden, and it was no longer hidden.
And here you have in the website, here's the big thumbs up.
But if you go to the original URL where we took the screenshot,
there's no thumbs up, meaning that the layout changed.
In the next example, using the python.org website,
we removed the donation button.
And you can see there's no donate button here.
But if you go back to the original website,
you'll see that there is in fact a donate button right there.
And you'll see in the stack trace there, hey,
it detected that there was a change.
The donate button was there.
It was not there afterward.
Therefore, the level three failure happened.
Same with the xkcd website, where we did a visual layout test.
We changed the sizing of the logo.
And here's the new sizing, where the screenshot was taken.
But the original sizing is basically, OK,
it's nice and horizontal, different.
So you can see all these changes that were made.
And therefore, you have the assertion errors.
Hey, the height width changed here.
The donate button was removed.
And an element appeared that wasn't there on the original.
So whenever you run a baseline for visual layout testing,
let's go into the examples folder visual testing.
And let's go into visual baseline, which
is a folder that's created.
For instance, if we go into the Python Home Test,
you'll see that all the things that are created when
you create your baseline.
So you'll get a page URL that basically verifies
that you're on the right page.
You'll get a screenshot of the original
so that you can basically say how the original looked,
so that when you look at your report screenshot,
you'll see what differences there are.
You'll also get tags level 1, tags level 2, and tags level 3.
So in tags level 1, which is essentially a level 1 comparison,
you have all the HTML tags on a web page.
And that is created when you first create the baseline.
When you run the check window method,
it's going to compare the latest version of the tags
to what was in the baseline.
And if something's different, you'll have a level 1 failure.
With level 2, it is HTML tags and attribute names.
So here you'll see that there's like a class,
and there's an ID.
And even more advanced check is level 3.
We're basically, it'll compare all the HTML tags,
the attributes, and the attribute values
to from the baseline to the latest version of the page.
And with a regular Python list comparison,
if something changes, well, then you'll get the assertion
failure, and you'll see here OK, something
that was hidden was visible in the new edition.
Here, a button was removed, and you got that.
And here, the dimensions of the logo changed,
and all these were found.
So that's automated visual testing with Selenium Base.
Pretty much creating a baseline, comparing the baseline
to the latest version, and then seeing if there are any differences.
And also, if you're not familiar with Selenium Base,
it's just from Selenium Base and Port Base Case.
And now you can quickly open up a URL and run,
like, say, the check window method, which essentially,
the first time you run it, you'll create the baseline.
If you can specify baseline equals true,
or if you don't specify that, you'll
use the version that was created in a previous version of a test.
Also, on the command line, if you run with a test
with, for instance, dash, dash, visual, dash, baseline,
I won't run it now.
But essentially, if you do that, it's
going to recreate the baseline, again, even if it was already there.
So that's how you can reset the baseline,
also by deleting the folder that you saw up here.
If you delete this entire folder in the visual baseline
directory, that'll also reset the baseline
when you rerun the test again, and it'll recreate the baseline
unless you specify baseline equals true.
So there are a few ways, as you see here, resetting the baseline.
And then you can run, say, the check window method
to compare the latest edition or the latest version
of the website with the baseline you created previously.
So that is automated visual testing, open source edition.
We know there are competitors out there that also offer this.
But we think that our version that is totally free and open
source on GitHub is more than enough
to handle all the visual layout differences
for automated visual testing that you can think of.
And if you ever want to get back to this readme,
to hear all these instructions again,
just go to Selenium-based examples, visual testing.
You'll see a folder with a bunch of examples that you can run
followed by this really nice, long readme
that basically goes into everything in detail.
And in case I missed anything just now, just go through,
read it, you can see the examples,
you can see the differences that are created
with automated visual testing.
And automated visual testing is just one really powerful thing.
You can add to your existing automated tests.
And if you're not familiar with Selenium-based,
well, you should check it out, because it's really powerful.
It's Selenium, it's PyTest, it's everything combined.
And it's really powerful for web automation.
And as you can see in this gift from the website here,
you can do any type of website testing, log into a website,
add items to a shopping cart, check out,
verify that all the elements are appearing as they should.
And of course, there's demo mode, as you see here,
where I'll even show you as you run the test,
what the test is verifying.
So really powerful stuff.
And again, if you need help getting started
with Selenium-based, the readme on the GitHub page
basically walks you through all the instructions
you need, such as setting up your web drivers,
like Selenium-based install Chrome driver, running a test,
basically a lot of different methods
that you can use inside your test, run commands,
and a bunch of features, and just a ton of examples
to help you get started.
And of course, the most powerful thing,
the command line options, where you can set the browser,
run in mobile mode, and all that.
So thanks for listening to automated visual testing
with Selenium-based, and have a really great day.
All right, bye-bye.

############################################################

[17/44] VIDEO: SeleniumBase integrations tutorial: Google Cloud, Docker, Jenkins, MySQL, S3, and more
URL: https://www.youtube.com/watch?v=n-sno20R9P0
------------------------------
(Source: Original Transcript)
Welcome to this exciting tutorial on how to become a release engineer with Selenium base an
Automation framework that allows you to jumpstart your browser automation like never before
Let's get started with some of our integrations that we have here
So right now we're going to start with the Google Cloud integration and there are a bunch of instructions for that
So to get started with that we're going to go into our Google Cloud platform console and
Let's go over to cloud launcher
And then let's spin up a Jenkins instance great. So we're going to launch that on compute engine
We're going to give it a name and we're going to set it to a nice zone nearby where we are. Let's say USEC
Create
All right, so while that's being set up. I'm going to show you Selenium base. We're going to run our first test and
We just take it off
And a browser spins up goes to xkcd.com clicks a few buttons types in some text and
then pretty much
Automates things. So beautiful thing about Selenium base is that you can make changes on the command line to how your test runs
For instance, if we want to run this with Chrome
We just type dash dash browser equals Chrome and now we're going to run the same test
But now in Chrome
pretty cool, huh?
All right, see what our status is on our virtual machine
The player still starting up Jenkins. All right, so we have a little more time. Well, that is continuing
I'm going to show you the Selenium base website on GitHub
Right here. So Selenium base has a lot of cool stuff. It gives you examples
So you can get started help docs integrations
And a really powerful read me that shows you how to get set up on a Windows machine a Mac
Docker all those things
Installation is really quick. You just need some web browsers some web drivers
Have pip installed and Python and you're pretty much good to go get clones Selenium base
And go in and then once you install the requirements and do the setup.py install
You can quickly run your first test and here's the test that we ran here
We essentially went on to xkc.com
We wait for an element to appear. We click the button
We grab some text and then we asserted that something true was happening inside the text
We opened up another page click link text. You get the idea
All right, cool. So now that our Jenkins machine has been successfully deployed. Let's go into the SSH
console
Opening a browser window
And we're going to connect into this give it a sec to get ready
Once that is ready
We're going to be following the instructions from our Google Cloud setup
So now once we are inside we're going to
clone the Selenium base repository so we do cd slash
pseudo get clone Selenium base
I'm going to pretty much copy paste the code line by line so that you can see that these instructions are exactly what you want to do
We want to go into the Linux folder
And then we want to give the Jenkins user pseudo permissions because we're going to be using Jenkins as our build machine environment
Which will allow jobs to be run with pseudo power
And let's see
Continuing we're going to become tomcat user, which is what the Jenkins user is
best show
All right, now we're going to install our dependencies
So here we go
It's initializing requirements setup. It's going to go to the Linux file and essentially install everything that you'll need
Web drivers browsers
Internal dependencies anything that you'll need to run automation
While that is going on on the side
We are going to check out some of the other integrations that Selenium base offers
So let's see let's go into our Docker panel
So to show you that we can also run inside a Docker
Docker build dash t Selenium base
Assuming you follow the Docker instructions, which are also on the website
So right now it's building everything in Docker
While simultaneously our Google Cloud machine is building Selenium base
And if you're curious about the Docker instructions those are found inside the Docker folder inside integrations
And there's a nice readme with all the steps you'll need to follow
So if you don't have Docker toolbox installed you just need to get that
Then you can create your machine for Selenium base
And then you can do Docker build dash t Selenium base
Which is what we're doing now now it's set and now that once we're in here
We can do a command such as running a test in Firefox which is what we just did
And it's going to run headless leak
So you want to actually see the browser spin-off because we're using xvfb
Which is a headless browser launcher which allows you to run all your tests
Headlessly inside your virtual machine like we just did there we ran one test
So that's the Docker demo
As you can see here our Google Cloud machine is still getting prepared
So we're going to continue back on to integrations
See I'll get ready for the Google Cloud stuff for once that is set
great
Continuing on
So with Selenium base you can do something such as
Let's see we're going to run a
Test called test fail which is going to spin up a site
And look for an element that isn't actually on the page
And it's going to fail and you'll see here that you'll have some error output
And the best thing is inside a logs folder that was created
You will find actually I'm going to run this test again to show you that that file was not there before
All right, so now we're running this again
It's going to open up that it's going to see that the page is in there the element that it's looking for on the page
And we now have
A logs folder thing so inside the generic logs that appear
You'll have a screenshot of the last page that you are on looks like this
And page source the HTML which you can open and it will render perfectly
And if you see the URL here it's actually a file which means that's actually on my file system
It was able to import all the dependencies that it needed
And on top of that you also have a basic test info document
That shows you say the last page you're on the browser that you're using the trace back
And the final exception element not visible
And in addition to that
The logs folder you can also do something such as dash dash
With dash db underscore reporting
Which if I open up my my sequel workbench
I'm just going to show you that there are no rows in here now
I'm going to run this and it's going to run the test fail again
And as soon as that fails
We'll see that if we refresh our my sequel workbench
Now we have a row that appears that shows you the test case address showing you the test that you ran
The start time
See the runtime
The air state error what browser that you're used in the message div army of robots was not visible in 0.7 seconds
And that was the fake element that we're looking for on the page that wasn't actually there
All right, it looks like that our google cloud setup is now complete
So we're going to resume with that
Scrabbed that over here great
Once we've done that we can do
We can start our headless browser display mechanism
xvfb launcher
Now we can go into the slenium base directory so we see the slenium base
Then we can install the requirements like so and once that is set we're going to install
Slenium base with the python setup.py install
Okay, great once that's it. We're going to run an example test in chrome to verify that everything's working properly
And this is running headlessly because it's running from the google cloud machines
You're not going to see the browser spin up so as you can see here now the test ran successfully
And we can also run that in Firefox too
But now we're going to log into Jenkins so that we can create our first Jenkins job that handles that so to do that
We're going to go into our Jenkins machine like from compute from the google cloud platform page
And we're going to log in with our temporary password which I'll change before this video gets out
Let's see that'll be user. Remember me log in
Cool
So now we're inside Jenkins and we're going to create a new item once we're inside here
We're going to give it a names a like test one and it'll be a freestyle project
Click okay
So that's going to get set once we're inside here
We're going to want to add a build step and execute shell and inside the execute shell
We are going to paste this which will have the job going to the slenium base folder
And run the example test my first test.py in chrome
Cool, so we set that in click save
And then build now
Then it's going to start building
And it'll take a few seconds and there we go
We have a blue dot showing us that the test that we just ran past
And if we go into the console output it looks similar to the output that you saw when we ran from the machine my machine
Uh, nose tests in this case you can run it in either pi test or nose tests so good to know
Uh, ran one test 4.6 seconds success
So great
Back on here now that you've run your first Jenkins job using
Automation
You've now become a release engineer
So what you can get can set up is say a deploy job which kicks off whenever there is a change to say
Your repository on github which has your project
And you can verify that everything of your application is working properly
And then you can if all your tests pass the integration test that you've written you can deploy it
So some of your projects might work inside say
Google cloud app engine launcher so I create a few projects
So if I open say this one I created a simple app that is a button table
And if you click on like let's say c1 there's nothing here
I'm going to you know
Type some random letters and click save
Click off of it click there
Essentially the simple app uses local storage in order to save say a seeding chart or whatever inside your thing so c2
Google
Save I'm going to go back to c1 which has what I put there before c2 that so really simple app
I can now write automated tests that test every aspect of this clicks a bunch of buttons
Types in a name into the seeding chart
Click save and then clicks off of it clicks on and verifies that it's all working
So cool so now that we've covered that integration there's one more integration
That we can cover let's say you
After running a test you want to upload your logs
Into the cloud so let's try
The one of our tests but instead of with db reporting
We're going to do dash dash with dash s3 underscore logging
So now we're going to run the test fail
And with this integration
If you have a failing test your logs are going to be uploaded into s3
So if we go into the mySQL workbench
And we click refresh you'll notice that now that we've turned on s3 logging you'll see a log url
So we're going to copy that paste that into our web browser
And you'll see inside here it will take you to say amazon s3 where you've uploaded all your logs from your failing test
So for instance the screenshot from before it will open up and you will see
The screenshot from the failing test as well as a basic test info
All the stuff you saw before the browser that used what page you were last on when the test failed
This essentially all the tools you need to build a fully like
Automated environment and automation system if you're a company you can like create tests really easily with a slennium-based
platform and then
Save logs mySQL google cloud integration
Amazon s3 there are a lot more integrations coming. I'm trying to write as many as possible
In my spare time so stay tuned for more exciting updates on slennium-based in the meantime the state
updated on the latest updates
slennium-based.com it will take you to here you can then click view on github and you'll see this project with
All the updates as they come in. So cool. Thank you for watching this exciting tutorial and
For more help on google cloud there are lots of books like this
And grab a free sticker while you're at it cool. So have fun signing up

############################################################

[18/44] VIDEO: Python Selenium: Fundamentals to Frameworks (with SeleniumBase) - Michael Mintz, iboss
URL: https://www.youtube.com/watch?v=WjiTdflkGWE
------------------------------
(Source: Original Transcript)
All right, hey everybody, and welcome to Python Selenium,
Fundamentals to Frameworks, and we'll be using the Selenium-based
framework in order to tie everything together on Michael Mintz,
and welcome to Chicago.
All right, so a few shout outs for starting.
I'd like to thank the Selenium org.
They created Selenium, and of course, the conference organizers
are doing an awesome job, maintaining everything.
My wife also supports me in a huge way,
and she even came out today to watch,
and I boss my employer.
They support my work, and I use Selenium-based framework
all over for their cybersecurity automation stuff.
So yeah, I am the creator of Selenium-based,
and I also lead the automation team at I boss.
So I'm going to quickly jump in and talk about what's going on.
So this is the only dedicated Python session at Selenium Comp.
So I'll hopefully be holding the Python ecosystem
on my shoulders, and you're going to see lots of Python,
a lot of live demos, and if the one session is not enough,
come see me afterward, there'll be a lot more to come.
So by the end of this presentation, very important,
you're going to learn a bunch of things.
So Python Selenium Fundamentals, we're
going to start with the basics, so things
that you may not know if you don't use Python at all.
If you're ready to use Python Selenium,
then we're going to evolve that into something more advanced,
and we'll get to that later.
So we're also going to find out how Selenium-based can make
Python web automation easier.
All right, so let's move in.
The format is a lot of slides.
They're going to be GitHub readme files that I'll go through.
And of course, lots of live demos, some videos with automation,
some actual demos, assuming the internet connection does not fail.
We can run some real automation on real websites
and see how things go, so it should be exciting for that.
So let's start.
What does Selenium provide?
It's an automation library, and it says so right on the website.
It automates browsers, but it does not provide a test framework.
That's where all the other people come in.
Developers can write test frameworks on top of Selenium
to wrap it and make Selenium a lot more powerful than it is on its own.
So how do you get Selenium for your Python user?
Well, there's this really cool tool called PIP.
If you've downloaded Python or installed it,
it's going to be available from the command line,
and you can install packages using the PIP installer.
So just do PIP install Selenium, and then all of a sudden,
you've got the latest version, which as of today, was 483.
So what are some of the building blocks of basic Selenium
that you get from installing Selenium?
Well, of course, there's importing the library.
That is the main line that you want in most of your programs.
From Selenium import web driver, you've got that.
You've got access to the Selenium library
and all the Selenium methods that go with it.
After that, you can spin up a web browser.
And for instance, let's say we're using Chrome,
but you can also do automation with any of the other browsers,
such as Firefox, Edge, even Safari.
So that is the main command, a very simplified version of it,
for spinning up a web browser.
After that, you've got the driver.get command,
which allows you just open any URL on the internet.
And in that particular example, your web browser,
after you've opened Chrome, is going to take you to Selenium.dev.
So basic building block will cover the basics
so that you know what they are.
And then we're going to get a little more advanced.
So here's the command for finding an element.
And first, you have to specify what type of selector.
So you could have an expath or CSS selector.
Normally, you'd import the by library and do by.css selector,
but that just translates into that.
And then if you're using a CSS selector,
you can then specify the CSS selector.
And this is going to find the element
and then return a Selenium web element.
Once you have a web element, you can then say element.click
as one of many different APIs available to you
to say click on that element element.
Let's say you also want to find an element
and then type text into it.
Well, there's another method.
It's called send keys.
So once you've found your element using driver.find element,
you can do element.send keys, and then the text
that you want to type into the text field.
And then another basic command driver.quit,
which quits your web driver at the end
so that you can free up resources and not
have like 100 different browsers open
if you keep running the command, but not closing your web browser.
So launching a browser can get a lot more complicated
than just webdriver.chrome.
There's lots of different options that you can specify
and you can use all the same options that
are available from regular Chrome.
So for instance, you can disable notifications.
You can add experimental options such as the exclude switches,
which will let you set something else to enable logging
and enable automation.
There's hundreds of different options
that you can specify.
And you can even change the password manager and not
enable that, et cetera, or the credentials enable service.
All these are built into Chrome.
So if you want to take control of a web browser
and change the settings, this is one way to do that.
And then you do driver equals webdriver.chrome
with the additional options that you want to put in.
So that's a typical example of advanced options
where you want to do more than just spin up a web browser.
You want to set all the configuration
and it uses the browser for that.
So up next, test frameworks can wrap Selenium
in order to improve things and give you
a lot of additional behavior.
So in this particular example, this
is right from the Selenium website.
You have a test framework wrapping web driver.
And then from there, you can add additional methods,
such as driver management.
And there are different tools that can wrap Selenium,
such as web driver manager.
And that basically allows you to automatically download
your web driver into a special folder
so that the tests are ready to go.
Because before you can even start your first test,
you need to make sure that you have the drivers,
such as Chrome driver for Chrome, Gecko driver for Firefox,
MS Edge driver for Edge.
And I think with Safari, all you have to do
is change an option and then you can run your tests on Safari.
So that's where frameworks fit in.
So what are some of the disadvantages
of using raw Selenium without additional libraries
or frameworks?
Well, the default timeout is zero.
And a lot of people have probably
seen this particular error message before, where
if something goes wrong, you get a giant stack trace,
and it's not very pretty.
And you see just a lot of Chrome driver messages
that aren't very legible.
But this is like a typical thing where you try to just
click on an element that isn't fully there yet.
You get big stack trace.
So this can be improved on and simplified.
A test framework might wrap all that.
And instead of just throwing a giant message like that,
it'll just be like this element with this selector
is not visible after 10 seconds of waiting.
So these are just some of the ways
that a test framework can improve
on the standard Selenium library.
So the commands can get quite long with standard Selenium.
For instance, driver.find element.
Then you have to specify the buy and then put the selector
and then dot click if you want to click on a button.
However, their test frameworks, where it's just self.click
and then you put the selector.
And it will auto detect between CSS selectors and x-path
because x-path and CSS are quite distinguishable.
Like for instance, if the selector starts with dot slash
or slash slash, you're going to know it's like, OK,
that's an x-path selector because CSS can't do that.
So because there's a difference between CSS selectors
and x-path selectors, a framework could just auto detect
what the selector is and be like, OK, instead of specifying
what kind of selector it is, just immediately click the thing
because it knows, oh, this is x-path and this is CSS.
So that's just a few ways that frameworks can improve
on some of the fundamentals.
So self.click is better.
So with raw Selenium, you're not going
to get fancy HTML reports, the dashboards,
like a special results display, even automatic screenshots.
These are some of the things that test frameworks can build
on top of Selenium so that when you run your test suite,
all of a sudden you have like a screenshot for every failure
instead of just like an error message.
So there are frameworks that already handle the sort of thing.
So here's an example of an HTML report that
combines pi test HTML reports with the Selenium-based dashboard,
giving you a pie chart of your tests,
stack traces in the logs, and of course,
a screenshot from an XKCD website, essentially saying,
like, OK, this is the failure that was here.
It's nice and red.
And here's the screenshot of the last pager on.
So if you have a failing test, it can immediately say, OK,
there's a problem here.
Here's the report that you got.
You clearly see from all the tests that you ran what went wrong
and it's very clear what you need to fix.
So more things with raw Selenium.
It might take a lot more lines of code
to perform the same thing that a framework could do
with a single line of code.
So for instance, with regular Selenium,
you might have to first find the element
and then clear out the text field,
and then do send keys to type in text.
So for instance, that is the how to log into the SAS Labs
web demo website.
And then you go into element.submit.
And then that will do a whole, that'll
let you log in automatically to the website.
So method, like self.type, where you put in the selector,
and then what you want to type in, and then use a backslash
and which will automatically perform a submit action.
You can do all those four lines of code in one line of code
with test frameworks.
And this particular line is coming
from the Selenium based framework.
Basically, a few lines of code or one line of code
can perform the same amount as maybe four more lines
of code from raw Selenium.
So what else can test frameworks provide?
We've got driver management.
And you've already seen for at Selenium Comp
there was web driver manager.
Selenium based also has its own driver manager,
so it works pretty similarly.
There are also advanced methods such as a certain no-broken
links.
So basically, you could have action.
It checks all the links.
And if any of them return a 404, it will tell you that
and be an error inside your report.
You'll also have test assertions such as self.acert text
so that you can check whether certain text appears in a selector
on a web page.
And if it doesn't, then you have a failed assertion.
So this is an example of an advanced assertion
that you could have.
You also have additional command line options
that you can do.
And this is something really huge from regular Selenium.
Remember, you'd have to modify your test
if you want to change which browser you're using
with a test framework.
It might add a PyTest command line option
so that you can say, OK, instead of the default browser of Chrome,
I want to use Edge and then add a HTML report on top of that.
All of a sudden, you no longer have to modify your tests
every time you want to change a little bit of behavior.
You can change the browser and many other things
right from the command line with a lot of these frameworks.
And you've got advanced tools such as test
recorders that will generate full scripts for you
automatically similar to the old Selenium IDE,
but now a new modern version of that.
Those might also exist within test frameworks.
And you have easy to read error messages
such as element H2 was not visible after 10 seconds.
Instead of going back before we had a giant long list
of Chrome driver stack traces, that was kind of hard to decipher.
And you generally make you have to scroll a lot
in order to see what went wrong.
So up next, what about test runners?
Well, Python is a very powerful programming language,
and it has tons of existing test runners available to it.
One of the most popular test runners for Python
is the PyTest framework.
And it has lots of ways for automatically running tests
from the command line where you can specify folder
to run all the test from or file or even like a regular expression
so that you can only run the tests that contain a certain string
within the name.
So that's one of the cool things that PyTest provides.
So here are all the things that PyTest can do.
Auto-collect tests to run, as you saw,
or you will see soon.
You can use markers for organizing tests.
I'll get into that in a bit.
So you can essentially say, this test is A, this test is B,
run all the B tests, run all the A tests,
and all of a sudden you can organize all your Selenium tests
quite easily.
Generate test reports.
You saw that provide test assertions.
That's also available.
You can multi-thread your tests by just saying dash and eight
on the command line.
And all of a sudden you'll spin up eight browsers.
You'll see that in a bit.
Use the large number.
There's a large number of existing plugins
already available, the PyTest, such as the PyTest HTML,
which generate reports.
And there's a lot of additional ones, too,
such as for multi-threading support.
And a lot more that we'll get into in a bit.
So what about complete frameworks?
Selenium-based combines the best of Selenium, Python,
PyTest, all that into a powerful framework.
And we're going to do some live demos for that in a sec.
So you already saw most of these things.
The features that I was covering before were actually
from Selenium-based, where you have the self-doubt
certain obroken links, assert text, command line options,
where you can just change your browser,
easy to read error messages.
And you can see exactly what went wrong and the reports,
et cetera.
To get that, it's just instead of PyTest all Selenium,
it's PyTest all Selenium-based.
So quite easy to get.
And that is a screen from the GitHub page.
So now that we've covered the first 15 minutes,
just a few slides, we're going to start jumping
into some GitHub readme files and live demos, running
some scripts, et cetera.
I will basically going to talk how we can evolve Ross Selenium
into something more advanced like Selenium-based.
But if you want to see a few examples
of this running a test with Selenium-based,
let's run a quick test, my first test,
from the Selenium-based examples folder.
And that ran pretty fast.
So you might not have seen what it was doing,
but there's a cool mode called demo mode,
which actually highlights the browser action
so that you can see what the test is doing
and what it's asserting at every step of the way.
So you have element assertions, you have text-based assertions,
search the title, et cetera.
The JavaScript will go right onto the page
and show you exactly what it's doing.
But if you don't run with demo mode,
it just runs in like instantly.
Like a few seconds, it does all those things.
We're now slowing it down so you can actually
see all the various things that are going on
in this particular example test,
such as adding a backpack to a cart
and then going through the checkout process
and then making sure that you've got the thinking
for your order at the end.
So let's take a look at what this particular test looks like.
And then we're going to take a few steps back
and take a look at how raw Selenium evolves
into something like this.
So if we open my first test.py,
you'll see it's just a simple command
such as opening a web browser.
Actually, let's see if I can make this a little bigger
to see if you can make it easier for everyone to read.
OK, is that a little better for the audience?
OK, cool.
So the spinning up of the web browser is done automatically
and you can change what type of browser you use.
Like, for instance, if I wanted to run that
with like a Safari browser instead of Chrome,
I would just do pi test my first test.py
and then do dash dash Safari.
And you can see that it's now using a Safari browser.
You look carefully at the top left.
It is doing that.
So that was it running in Safari.
So command line options that you really control
and customize the various tests that you have.
So back to here, here's a simple command
for opening a web URL.
Then you can type text into a text field
and then type in the password and then the backslash
and we'll give you a submit action automatically.
So one line of code handled the four lines of code
that you saw earlier.
You can easily assert that an element is on a page
or assert exact text.
You can click the link easily or click an element
like the button here, click a shopping cart,
assert exact text.
So the difference between assert text and assert exact text
is that assert text lets you know if the text is in the full text
whereas exact text means a full text match
instead of a substring match.
So yeah, lots of simple actions, but it performed a lot of things.
And of course, there's also a JS click available instead
of a regular click when you ever want to click something
that is maybe hidden behind another element.
Otherwise, you might get like an element click
intercepted exception or like another element was over yours.
There's lots of different APIs that you can use for that.
So that's just a basic test and it's a lot more simplified
because it takes care of the browser management.
Now let's take a look at how we evolved
from regular selenium to something more advanced,
like selenium base.
So let's go over to the raw selenium.
And let's take a look at a flaky messy raw example
where you have to specify, so quick step back.
So there is a built-in framework for a Python called unit test.
And unit test.test case is something
that test classes can inherit in order to gain additional assertions
and they'll gain automatic set-up and tear-down methods
like you see here.
Set-up and tear-down, which will be called automatically
at the start and end of tests whenever you run that.
So let's see if I can just make it a little bigger as you can see.
So unit test provides automatic set-up and tear-down
so that you don't have to call it directly from your test.
It's automatic before and after your test starts and ends.
And inside the set-up and tear-down methods,
you can specify how you wanted to launch your browser.
And this particular example, it's using raw selenium, not selenium base.
So we're just using regular from selenium and port web driver.
And all of a sudden, you see that you have to define all those things
like how you want to launch your web browser
because that's not automatic because selenium on its own
doesn't include a test framework that does all that for you.
And of course, in a tear-down step, you'll have a quit process.
So you might then have to define your own methods,
such as is element visible.
And you'll check that if there is an exception returned
after trying to do a self.driver.find element action,
then you'll return false.
Otherwise, you'll return true if, say, the element is displayed.
So when you're not using a test framework,
you have to actually define all these methods on your own.
And it can become a little cumbersome,
but that's why test frameworks exist
in order to simplify things for you.
So here's the test that we're creating here with Roselenium.
Test add item to cart.
You're doing a self.driver.get action.
You're going to, instead of using the buy.css selector,
maybe you'll put that into a variable
so that you don't have to type that in.
And then you have to say element.clear,
but maybe in this particular example,
the text field is already empty when you went to the page.
So you didn't necessarily have to clear it,
but a lot of times you might have to.
So send keys is the typical type text into the text field
and all that.
And test like this can be flaky because,
or they're very long and messy,
because you have to do the whole driver.find element
with specify the buy, specify the selector,
and then tell it to do a click.
So that's what regular Selenium provides for you.
And out of the box, this is what you would have to do
unless you were to define methods that do these advanced things.
So as you can see here, the script is quite a bit longer
than if you used something such as a Selenium base
which does simple methods all that for you.
So that test does the exact same thing as this.
Well, not totally exact, but the same thing,
but it takes a lot longer to do the same thing
with raw Selenium.
And of course, the script can be flaky
because if any of these elements aren't loaded right away,
you'll get a stack trace and a failure for that.
So that's the first step of raw Selenium usage,
basic things, but let's say you want to improve
on the flakiness level of that.
Well, there are additional things such as,
there's the Selenium.webdriver.support.ui,
which includes web driver wait.
So this is basically the next evolution of raw Selenium.
A lot of people start using web driver wait
in order to wait for an element to be available
before interacting with it.
So as you can see here, if we go into the test itself,
you now have to say like to look for an element,
you're doing element equals say web driver wait,
self dot driver, and how many seconds to wait for
until the element say is clickable
or the element is visible.
And then you stop to specify the buy.css, et cetera.
And maybe this selector with that.
And that takes up a lot of code, significantly more
than just like a simple assertion.
So web driver wait is one evolution of that,
but it's still a lot more code to do.
So you still end up with a really long script
if you have to use web driver wait,
ec.elman to be clickable after every single action.
So that was like the first evolution of evolving.
And then let's say you want to extract
those out into methods themselves.
Well, you can do that.
And then inside your test, you'd call say wait for element
visible, and that would just be defined
as a huge web driver wait command.
But instead of calling all this in multiple lines of code,
you now just do it in one line of code.
So this is how it starts to simplify the method.
And all of a sudden, it looks a little cleaner
than throwing web driver waits everywhere.
And it's not as flaky as just trying to do a click directly
because then if the element doesn't load,
you get a stack trace and a failure there.
So that's the next evolution.
After that, we have the refined raw, which basically
really builds out advanced methods such as a click method.
So you'll see that we'll first wait for the element
to be clickable or visible, and then you get the selector,
the bike was by, et cetera.
So we're building out those original methods.
And now all of a sudden, we have a click method.
So by the end of all these methods that we've built out,
we've got a script that looks pretty much just
like the Selenium-based version.
But it's now using only raw Selenium.
So as you can see here, it's just from Selenium-Import Web
Driver.
And a few of the existing APIs that Selenium already provides.
Using this example here, you've actually
refined your tests to basically be a simple version
of what you want.
So that gives you something like this as the full test.
And all of a sudden, it's a lot more readable
and easy to follow, understand, and make changes to it.
So that's how you evolve something such as a raw Selenium
building block into something that actually
becomes easier to use.
So now that we've basically taken the API from really raw
to a more refined thing, Selenium-based tries
to simplify all that.
And if we go to the repo, you'll
see that there's a lot of advanced features such as dash
boards and reports, et cetera.
So let's say we run a different test.
Let's do pi test, test suite.py.
And then let's do dash dash dash board, then dash dash HTML
equals report.html.
So this is going to run a quick series of board tests.
And two of them will pass, and two of them will fail on purpose
so that you can generate the report at the end.
So now, if we want to take a look at the report,
open report.html.
You get a dashboard, a pie chart,
and inside here you have stack traces with screenshots.
So you can see your click-in screenshot of that particular
failure.
That one was failing because the fake text was not visible
after 0.4 seconds.
So there are default time outs built in that are probably
like 7 or 10 seconds, but you can change that within your test.
Here, the fake element was not present again.
So the test failed on purpose, and you see the screenshot
that gets generated.
And so you have stack traces, screenshots,
and of course, pie charts.
There's also a regular dashboard view.
So if we go open dash board.html, I should take that file
and open it in here.
You'll see that there is a logs and a data folder,
but it's kind of small.
So let's see if I can make it a little bigger.
So inside the data folder for like a failing test,
you'll see a basic test info.txt file.
I'll expand it so you can see a bit of what
you get from one of these reports.
So you'll have the test that it ran.
The last page that was on, that the test was on when it failed.
How long it ran for?
The browser that you had, the driver that you were using with it.
And hopefully, the version of Chrome driver
matches your version of Chrome.
You'll also have the Unix timestamp, which
is great for helping you debug the issue.
And that converts into a regular date and time.
So you can see exactly when the test ran.
And my clock is still on Eastern Standard Time.
So it might be actually a head of, it's actually 528 here
in Chicago.
So it's based on your computer on the computer's clock.
So if your computer's clock is wrong,
it's going to match that.
But you can always sync it up with UTC, et cetera,
so that you know where exactly you are.
You have a nice trace back in here where it says, OK, fake
element does not exist, was not present after 0.4 seconds.
So that is cool.
So that is basically the dashboard and the HTML reports
functionality.
You also get a screenshot in that particular log.
And you have the whole HTML file, which you can then take
a look to see if there are any failures that occur.
You can look at that easily.
Works great with build systems, such as Jenkins, et cetera.
So the next part, let's take a look at some of the cool
command line options that you have.
Actually, first of you just type S-base on the command line,
you'll see a whole lot of different things
that you get out of it, such as the methods, common options,
the GUI, recorder, the ability to print tests
right from the command line, et cetera.
So if I do say S-base, print, basic test.py,
it's just going to print it, which is goods
that you can see exactly what is inside your script.
You can do dash n to print it with line numbers.
Cool.
So if you do type S-base methods, you'll
see a lot of common methods, such as clicking, clicking
links.
You can click check boxes easily with check if unchecked.
So if the check box is unchecked, you'll automatically
check it.
You can grab the page source easily.
You can do drag and drop, hover and click,
select option by text, switching into an iframe easily.
Lots of different assertions that you can use,
such as asserting that there are no 404 errors,
there are no JS errors, et cetera.
If you type S-base options, you'll
see lots of various command line options
that you can use, such as changing the user agent,
changing the browser, using demo mode,
maximizing the window, using the dashboard,
using a pi test collect only run, incognito mode.
So if we run back the test suite that we ran a moment ago,
you saw that it opened up a new browser each time.
There is a dash dash RS, which stands for dash dash
reuse session, which means it will run all those tests
in the same browser window without having
to spin up a new browser window each time.
And that will save a ton of time.
Also, there is the ability to multi-thread those tests.
So if we ran the same thing and we did dash n4,
you'll see that it's going to spin up
four different browser windows instead.
So you can easily do multi-threading and all that.
There's also a very powerful tool called the recorder.
So let's open that.
You see a little tool that comes up.
So let's do sasdemo.com and then do a record.
So I can basically record actions.
Let's do standard user.
And then, so right now I'm typing this in
so that the recorder records a script.
I'm going to add two items to the cart.
And then I'm going to click on the cart.
And then I'm going to click checkout.
And I'll put in fake name 1, 2, 3, 4, 5.
Continue.
And then finish.
And then I'll do shift 7 to switch into assertion mode.
And I can assert that the text is there.
When I'm done, I get to go back to the command line,
which was here.
Here we go.
So you see it created a break point.
So if I do see, to continue from the break point,
you'll see that it generated a full test
out of just the actions that I did.
So instead of actually having to manually create all your tests,
you can use a slanting based recorder
to instantly generate the entire test for you.
So now, if I run that, I can do playback.
And it's going to playback the exact same thing I just did.
If I do playback in demo mode, it's going to slow it down.
So you can see what exactly you created.
So here, now it's adding those exact same items to the cart.
And now it's verifying the cart, typing in the fields.
You'll automatically generate a full Python test for you.
Just like that, with a few clicks,
you don't have to even know all the APIs.
You can do all that for you, which makes it a lot faster
and easier to do.
So that's the slanting based recorder.
Really fast way of just generating tests on the fly.
There's also plenty of other advanced features,
such as the presentation generator.
And if you hadn't noticed, the presentation that I ran earlier,
this was all built in Python.
So if I open the thing, the presentation that I ran earlier,
I use slanting based to generate the JavaScript from the Python.
So if I did a Pytest Fundamentals.py,
it's running a Python script.
And that generated this entire presentation
that you see here today.
So some of the advanced tools that you'll have here
is the ability to not just do testing,
but you can generate presentations.
You can even generate advanced charts.
I'll quickly show you that.
So if we go to the chart maker, which
is from the slanting based examples folder,
and you Pytest Chart Presentation, you'll
see that you can generate a pie chart with a regular Python
bar chart, column chart, and do fancy animations like that.
There's even a website tour maker.
I'll quickly go for that.
Pytest Maps Intro Gs Tour, where it uses a Pytest
to run some Python code that automatically
hacks into Google Maps, not really hack it in.
It changes the browser that sees it,
and you've now added a website tour.
So as you can see here, you can use the slanting based
and not only do tests, but create a whole website tour.
And then you can export that into the JavaScript file,
and then load that directly into your website.
As you can see here, tour is exported at Maps Intro Gs Tour.js.
So the Python generates a whole website tour for you.
So that's just some of the cool advanced things
that you'll have here.
And there's a ton of stuff on the GitHub Read Me page.
And if you haven't started the GitHub repo already,
please do.
There has all the instructions that I
didn't get to cover today, such as various formats.
And there's multiple syntax formats,
such as the regular base case inheritance.
I'll just make that a little bigger so they can see.
That's like a standard way of doing it.
But it also can handle things such as Pytest fixtures,
where if you load SB, and you're familiar with Pytest,
you can run everything as the SB fixture.
And another common one you can do is the context manager
or even the behave BDD-Gurkin syntax format
for people who are familiar with that.
So you can also use the slanting base recorder
to record this exact same BDD-style Gurkin test
as seen here.
And you'll have to do that on your own,
because I am running out of time.
But to end off, I'm going to play a video that I basically
use the slanting base to generate a automation that
modified several different websites.
The slanting base going in and hacking, say, Apple,
Google, and all the various websites you see here
with automation because slanting has the ability
to execute JavaScript in the web browser, which means
you can easily modify any text on any website
page and even create a music video like this.
So this is actual slanting base going in with the demo
mode as you saw, and changing the various text that you see.
That was like, get up.
That's going to go through.
And here is dev.2.
It just goes through and just changes all the text.
So as this plays, I basically want to say that slanting base
can do the test automation, instantly generate your test,
but generate presentations, carts, website
tours, and hack websites.
But it's really it's only hacking your browser, not
so much your website.
And as you can see, it's just going through.
And it's actually one of my most fun videos
that I created where this is OK.
Can I just go on to every single major website
and just change the text?
And actually, I think a few of them
thought they were actually hacked.
It was like, they saw the video.
I'm like, wait, wait.
No, that's good.
It's just someone messing around with their browser.
Doesn't actually hack their website.
But with JavaScript, you can do anything.
And slanting base basically utilizes the best
to Python to generate a lot of JavaScript
to do advanced things such as demo mode and all that.
So this is the last part of my presentation
at the two minute video where I'm going
and you probably recognize a lot of these websites.
It's like Slack.
And if you want to see what the script looks like,
I'll quickly show you what that looks like at the end.
Take a few seconds once it's over.
But yeah, here's a slanting website.
As you can see here, slanting automates browsers.
But what you do with that power is entirely up to you,
which means if you want to use that power to make a music video
where you hack a bunch of websites,
then that is power to you and all the other things
that you want to do.
All right, that should be less than 20 seconds away
from completing.
That's the pipi.org website where you download Python packages
such as slanting or slanting base.
Probably recognize it last year.
There's one for Ibot.
And three house and then it is end date.
And very last thing I'm going to show you
is the script that I did for that.
So I'm going to open up that script so you can see exactly
what that looked like.
Open hack the planet.py.
And here is the cool method that I pretty much used everywhere
set text content so that I was going to change the text
on any website.
All right, cool.
Well, if you have any more questions about slanting base,
check out the GitHub page.
And also, because this is the only real Python session
at the conference and you want more Python
and more cool awesomeness, come see me.
Even tomorrow, I might do like a small find a room somewhere
and then show more advanced features such as more dashboards
or ports and all the other API methods and command line
options that I didn't get to cover today,
such as how to change your proxy server
or other additional settings that you
can do from the command line when you run a test.
All right, let's open the floor to questions.
They're going to pass around the microphone
to anyone who has a question.
And yeah, please ask.
And raise your hand if you have questions.
The microphone guy will come to you.
Great presentation.
Thank you.
We generally, when we use the Selenium as an UI test framework,
one of the main state exception, what we see.
So from the Selenium base, is there
any way it automatically detects the state exception?
Yes.
So with the Selenium base API, it's automatically
going to avoid that because it's always
going to refine the element when it does its automatic waiting.
So if I were to go into the code right now,
so this is just the big Selenium base
with all the different things.
Inside the API, which is located
at Selenium base fixtures, basecase.py,
if you go into that Selenium base,
that's where all the real major code lives.
Basecase, that's what you inherit.
You'll see that whenever you're finding the element,
it basically does, let's see, find elements.
It calls a method, and it loops through.
Actually, there's a lot of code in here,
so I'm not going to search through all that now.
But essentially, you're not going to run
into the stale element reference exception
because if you try to do a click action,
and the element isn't immediately there,
it will automatically search for it.
So run a more advanced thing quickly
as I answer more questions, pi test,
coffee cart test.py dash dash rs.
So it's going to basically wait for the elements to appear.
So here, I am ordering some fake coffee from a fake website.
It's going through, and it doesn't run to any issues,
even though things don't load up right away
because it has a default time out of, say, 10 seconds.
And if your element is going to generate like a stale element
or that, it's just going to refine it.
So you don't have to worry about that.
That's one of the things that's wrapped
within the framework.
Thank you.
Next question.
We're pretty much out of time.
We got time for one more question.
Thank you very much.
Having built some frameworks, also very impressive
to see your stuff.
One thing that I haven't seen in your demo
is kind of the page object model that testers tend to use.
Yours is very scripty.
And so just curious what your thoughts on page object modeling in.
Yeah.
So there is a format where you can actually structure
your test using the page object model.
So if you go to syntax formats,
you go to page object model with base case,
you can basically set, define something
such as like a login page and then
call the login page methods like this.
And it's actually one of the 23 different formats
that you can use for structuring.
So if you want to basically break out your test
into page objects, I assume something like this,
like a login page, and then you want to call a method
from that, you do something like that in this way.
And just has examples of using all the zoom in, if you can see.
So page object model would look like that.
There are a few other examples so that if you want
to break out all your selectors into a page object as well,
there's an instant page object model generator.
So for instance, quickly, if I open basictest.py,
you see it has the selectors in there.
If I do a slenium space object, if I basictest.py,
so it's going to create a page objects file for it.
And then it's going to update basictest.
If I open that, you'll see that it broke out all the CSS
selectors into page objects.
And you can like change the naming of that
so that if later you said, oh, I'm going
to reusing the selector a lot.
Why not just break everything out?
You can use some of the really advanced command line tools,
such as the objectify command.
And you will immediately break out all your CSS selectors
into an object's file and then the script will run as is.
And you can even translate, similar
to how we swapped your selectors with that,
you can translate the API into multiple languages.
So let's say if you want to have a slenium base
in a different language, there's like, for instance,
Chinese translation.
So it's using Chinese characters because there's
one-to-one mapping from all the slenium base methods
to every other language.
So if you want to actually run your test,
there's a translator function.
You just do S-Base Translate and immediately translate
your test into that language.
So if I do S-Base Translate, let's see,
coffeecarttest.py.
And then I do dash dash zh, which is the Chinese code
and then do dash p to print it out.
You'll see that it translated a regular test
into a different language.
So if you don't speak English at school,
there are 10 different languages supported.
You just do S-Base Translate, the language
that you want, like there's like French, Spanish, Portuguese,
Italian, Japanese, Chinese, Korean, all that.
You can instantly translate a test
so that your team back in, not out Japan
who maybe doesn't speak perfect English,
they can see, or in this case, Chinese,
they'll be able to see all the API methods
with the one-to-one mapping, and instantly translate,
and it'll run just like any other test
because it does the replacement on the fly.
Any other questions?
All right.
Well, then come see me afterward if you have any more,
and I'll show you more advanced things
that we did not get to cover today.
But thank you so much for coming
to Selenium Conference, Chicago, 2023.

############################################################

[19/44] VIDEO: The 17 SeleniumBase Syntax Formats (Design Patterns)
URL: https://www.youtube.com/watch?v=PYpO9kNBjgM
------------------------------
(Source: Original Transcript)
Hi, I'm Michael Minsk, the creator of the Selenium-Based Test Automation Framework, and today I'm going to talk to you about the 17 Unique Syntax formats for structuring your Selenium-Based tests.
To get started, head over to the Selenium-Based GitHub page and click on Syntax formats from the list of options you have.
That will take you to this page where you will see the list of all those syntax formats.
Now, these 17 syntax formats are really more of design patterns that you can use for structuring your tests in different ways, depending on whether or not you like the page object model, or a simple structure, or other types of formats.
So, I'm now going to go through one by one, so you can see what those are.
The first Syntax format is Base Case Direct Inheritance. Now, this format is used by most of the examples in the Selenium-Based examples folder.
It's a great starting point for anyone learning Selenium-Based, and it follows good object-oriented programming principles.
In this format, Base Case is imported at the top of a Python file, followed by a Python class inheriting Base Case.
Then, any test method defined in that class automatically gains access to Selenium-Based methods, including the set up and tear down methods that are automatically called the spin up and spin down web browsers at the beginning and end of test methods.
So, here's an example of that. So, here, as you can see, from Selenium-Based and Port Base Case, then you define your class, and that class must inherit Base Case, and then you're going to create a test method, and make sure that this test method that you create starts with test under its score, because that is the format for a PyTest auto collection for tests that are run with PyTest.
And then you can use all the available Selenium-Based methods, such as self.open, to open your L, self.type, to type text into a text field, self.click, etc.
So, that's the first of the syntax formats.
The next one is Base Case subclass inheritance. Now, there are situations where you may want to customize the set up and tear down of your tests.
Maybe you want to have all your tests log in to a specific website first, or maybe you want to have your tests report results through an API call depending on whether a test passed or failed.
This can be done by creating a subclass of Base Case, and then carefully creating custom set up and tear down methods that don't overwrite the critical functionality of the default Selenium-Based set up and tear down methods.
Afterwards, your test classes will inherit the subclass of Base Case with the added functionality rather than directly inheriting Base Case itself.
So here's an example of that. So here you still have from Selenium-Based-Import-Based Case, but you'll create a separate test class that inherits Base Case, and then you can overwrite the set up and tear down methods that are included, which are automatically there even if you don't define them.
So if you're overwriting the setup, make sure you call the super method, which basically calls the constructor, and this is where the setup method will spin up the browser automatically.
If you need to do something after the browser is spun up, but before your tests actually start, you can add that custom code here.
There's a similar story with the tear down method. First, you want to make sure you save the tear down screenshot before you do anything, because if you have a tear down that takes you to a different page and your test failed, the screenshot that you would get would not be on the same page where the error occurred.
So make sure you call self.save tear down screenshot first if you're overwriting the tear down method.
And then you can customize it, such as if there is an exception, you can run custom code if your test failed, or with the else statement, run code if the test passed.
And this is a great place to put an API call, for instance, if you're trying to send your test results to a test case management tool, and there's an API for that, you can send a failed test result through here, and a passing test result through here.
And at the very end of that tear down method, you want to call the super base test case self tear down method, and just keep in mind, this base test case here should match the name of your class here.
And now you can also define other methods that you may want to use, such as a login method, that may be all your test will call, or other methods.
And then inside an example test, so for instance, here we've created a class my tests that now inherits base test case instead of base case.
And now there you can have your test method that calls the login method that you defined, and as well as any other methods, and all your slenian base methods as usual.
So that was the second syntax format.
The third syntax format is the SPPITEST fixture with no class.
Now the PITEST framework comes with a unique system called fixtures, which replaces import statements at the top of Python files by importing libraries directly into test definitions.
More than just being an import, a PITEST fixture can also automatically call predefined setup and tear down methods at the beginning and end of test methods.
To work, SP is added as an argument to each test method definition that needs slenian base functionality.
This means you no longer need to import statements in your Python files to use base, to use slenian base.
If using other PITEST fixtures in your tests, you may need to use the slenian base fixture seen here instead of base case class inheritance for compatibility reasons.
Here's an example of the SP fixture in a test that is not used Python classes.
So this is the entire Python file. There's no import anymore because you have SP here, which is the PITEST fixture.
And now that automatically gets access to slenian base methods.
So as you can see here, you can do SP.open instead of self.open.
And that is the new way that you would be calling or slenian base methods.
So this is the SP PITEST fixture with no class.
Additionally, for the next syntax format, you can use the SP PITEST fixture in a class.
So there's a slight change to the syntax because that means test methods must also include self in their argument definitions when test methods are defined.
The self argument represents the class object and is used in every test method that lives inside of a class.
Once again, no import statements are needed in your Python files for this to work.
Here's an example of using the SP fixture in a test method that lives inside of a Python class.
So here I define the class and now I immediately create the method, but the difference is you have to add the self argument right here.
And that represents the class.
So every time you have a test method inside of a class, the first argument to that must be self.
And then you can include the SP PITEST fixture and you'll use SP again to call all slenian base methods.
There's also the classic page object model with base case inheritance.
With slenian base, you can use page objects to break out code from tests.
But remember, the self variable from test methods and hairy base case contains the driver and all other frameworks specific variable definitions.
Therefore, that self must be passed as an arg into any outside class method in order to call slenian base methods from there.
In the example below, the self variable from the test method is passed into the SP arg of the page object class method because the self arg of the page object class method is already being used for its own class.
Every Python class method definition must include the self as the first arg.
So here we have from slenian base and port base case and recreating our page object class log in page.
And there is a function definition in here log in the swag labs and you'll see self as the first argument will also include SP and username.
And you see as we're calling SP methods, SP dot open, etc, those are all called with SP instead of self.
And here's the test class that inherits base case as you've seen before.
But when you use like the page object method, such as log in page, we'll do log in page dot and say the method that you define here log in the swag labs.
But keep in mind that you must pass in the self into that page object because the self variable contains all the slenian base specific code that is needed to control the browser and everything like that.
And here I'm also passing in additional arg for instance, the username standard user here, which I use on this line here when I type in the username into the username field.
So that is essentially the classic page object model with base case inheritance.
Next, we have the classic page object model with the SP pi test fixture.
And this is similar to the classic page object model with base case inheritance except this time when we pass the SP pi test fixture from the test into the SP arg the page object class method.
So that's basically what we're doing there. Now you're using SP as a pi test fixture and you no longer need to import base case anywhere in your code, such as in the example below.
This is probably going to be the same as here, but the key difference here is that now when inside your say class my tests, which no longer inherits base case because you're passing in the SP fixture into a method that starts with test underscore.
And pi test recognizes that as OK, I'm going to use SP as the fixture that we've defined previously.
And now when I call login page, I'm going to pass in SP instead of self like we did before in this line here.
So here in syntax format number five, we passed in the self because we're using base case inheritance.
With number six, we are passing in SP instead and that's basically the only difference going on there.
Some of the lesser common syntax formats are, for instance, number seven, using the request fixture to get the SP fixture with no class.
Now here, the pi test request fixture can be used to retrieve other pi test fixtures from within tests, such as in the SP fixture.
This allows you to have more control over when fixtures get initialized because the fixture no longer needs to be loaded at the very beginning of test methods.
This is done by calling request dot get fixture value SP from the test.
Here's an example of using the pi test request fixture to load the SP fixture in a test method that does not use Python classes.
So as you can see here, there's no import statement, but we use the request fixture.
Now on the very next line, we can initialize SP by saying request dot get fixture value SP.
And now we can use SP just as we did with the SP fixture, calling all the sending base methods as we want.
Additionally, you can use the request fixture to get the SP fixture in a class.
And that looks like this pretty much you have your class.
And now inside your definition for the test, you'll have self as the first argument and then a request and everything then pretty much goes the same way.
SP equals request dot get fixture value SP.
And now you're able to use all the sending base methods through that.
Now the remaining syntax formats are basically just sending base translated into multiple languages.
See here from sunny based dot translate dot Chinese, you can import the Chinese base case.
And now the entire test following all Python rules of syntax so that you're not breaking any rules there.
You can pretty much have most of that be in Chinese, but some things of course will still be in English, such as class.
Because that's a Python keyword deaf, that's a Python keyword from an import.
Those are Python keywords.
And technically self is the standard for the representing the class inside the test definition.
So you're going to have that.
But the rest we can use now the sunny based translated methods, which are now in Chinese.
And for number 10, it's the same thing but in Dutch.
For number 11, the same thing but in French.
For number 12, the same thing but in Italian.
For number 13, the same thing in Japanese.
For number 14, the same thing in Korean.
For number 15, the same thing in Portuguese.
And number 16, the same thing in Russian.
And number 17, the same thing in Spanish.
So to sum up, these are the 17 unique syntax formats for structuring your sunny based tests.
And whenever you want to design like a new test, you can basically follow one of these patterns.
And they all work to their own strengths.
And if I want to run a test, so for instance, I want to run the first test scene here just because I'm creating a tutorial.
And I should run at least one test so you can see something happening.
Let's run the test demo site from the examples folder.
So pi test test demo site.
And this is going to spin up a browser and basically run the test using the first of the 17 syntax formats.
So now that the browser is spun up, you'll see it's going to type in text automatically.
You'll see it's going to pop down, click buttons, smooth sliders, check boxes, radio buttons, iframes, links, etc.
All that is basically included.
And that was just the example of the very first syntax format that we did here with base case direct inheritance.
And if you're curious about seeing that entire test that we just ran, that is test demo site from the sunny based examples folder.
And that goes to the slinning based.io demo page and then performs all the actions that you see here.
So that pretty much covers this tutorial.
And I hope you enjoyed it.
Please subscribe to my YouTube channel and star the slinning based repo on GitHub whenever you get a chance to.
And if you have any questions, please feel free to open an issue on GitHub or go to GitHub discussions.
Or you can also reach me via the getter chat and any other options that you see listed here.
Well, that covers this tutorial and thank you for tuning in.
I'll see you next time for the next exciting slinning based tutorial.
Thank you very much and have a great day.

############################################################

[20/44] VIDEO: Making Pie Charts on Pi Day with Pytest, SeleniumBase, and HighCharts
URL: https://www.youtube.com/watch?v=TMQx3FLWvUY
------------------------------
(Source: Original Transcript)
Hi, everybody. Happy Pi Day. Today is March 14th, 314, which means it's Pi Day in America
or anywhere where the month comes before the day. Today, I will be talking about Pi Test
and Pi Charts with the Pi Test Pi Day extravaganza. And if you don't know me, for those of you
don't know me, I am Michael Mintz, the creator of Slending Base, a Test Automation Framework
that you can find on GitHub. And let's get into some coding. All right, then. So to get started,
let's go to the terminal where I'm going to run a command with Pi Test. PiTest PiTarts.py,
which is essentially going to run a Python script that auto generates,
PiTcharts like that. Let's start off with the lemon meringue Pi that we have here,
which is three parts meringue cream with three parts lemon filling and one part gram cracker crust.
Up next, actually, before we go on to that, you might actually have one of those here and stop.
Up next is the blueberry Pi, which is one part blueberries for two parts of blueberry filling
and one part golden brown crust. Up next is the fruit tart Pi, which is, which kind of looks
like this, which is essentially strawberries, kiwis, apricots, raspberries, blackberries, blueberries,
custard, and golden crust. After that, we have the apple pie, which is pretty old-fashioned. It's
got apple crust, apple filling, cinnamon, and whipped cream. And finally, we have the Boston cream
pie, which is sponge cake custard and chocolate. Mmm, is that good? Well, if you hadn't noticed,
these scripts that are generating these pies, that's all done with Python. So if I open the
piecharts.py file, which I'm running, you'll see all the source code for that. So it's actually
really easy to create a pie with Selenium base from Selenium base in port base case. Then you have
the piecharts class that you've created and inside that test piecharts where you create a presentation
and you can pick your theme and a transition and then you can start creating your charts. So to
create a simple piechart, which had the lemon meringue pie on it, we simply ran the method
create piechart. And then we added some data points to basically say how many parts say
meringue cream with lemon filling and graham cracker crust. And you can even pick the color of that.
And then when you're all set with that, you can do self.add slide and you can name it. And then
self.extract chart, which basically uses the generated chart for the pie chart as part of the
creation of the pie chart. And that's basically how all these pies are generated. A few lines of
Python code generate a lot of lines of JavaScript, which get you lots and lots of pies, which is
really exciting because pie day is such an exciting time. So many pies to eat, so much food,
it's good. And we can mix in Python and use that to generate these charts. It's quite exciting.
So for those of you who aren't familiar with Selenium base, you can easily go to GitHub where you'll
be able to find the Selenium base repository and all the instructions that you need for generating
charts. And the tool we use here today is called chartmaker, which you should be able to find a
link to from the Selenium base GitHub page. And then you have all the instructions here
that you can use to create charts such as the pie chart, which is special because day is pie day.
And today we released Selenium base 1.58.0, which basically gives you more control over creating
pie charts. So if you just want to run these tests that you saw earlier with the pies,
that's once again from the chartmaker directory. So let's say you've cloned Selenium base,
GitHub Selenium base, and then inside the examples folder and the chartmaker folder,
just run the command, pie test pie charts, and just automatically runs pie test, which is a unit
test runner. But it uses Selenium base in order to generate all the web components for building pies
and doing web automation, creating pie charts and all that. It's really fun. It's really exciting.
And yeah, it's pie day. So definitely have some pie and the pies that I have here are sponsored
by Central Perk, a place where you can find friends. Yes. So yes. So yeah. So that's pie charts.
That's pie test scripts running to create these pie charts. It's a lot of fun to do. And
pie test is an awesome framework that is very, very popular. A lot of people are using it to
write automated test scripts and test things to make sure all their web apps are working properly.
So yeah. So that's pie charts. That's a little pie test. That's pies, real pies, and all that.
And of course, there's Selenium base doing everything in the back end to make all that possible.
So yeah. So if you have any questions, feel free to visit the Selenium base page on GitHub,
and you'll be able to have all the instructions you need to get started, write some tests,
create some pies, and then you can eat some pies on the side after that. So great. Well,
thanks for tuning in to the pie test pie day extravaganza with pie charts. And I will see you
again later. Bye-bye.

############################################################

[21/44] VIDEO: SeleniumBase syntax formats: 15 ways of structuring tests
URL: https://www.youtube.com/watch?v=VvwtS9_1m0s
------------------------------
(Source: Original Transcript)
Hello, I'm Michael Mints, the director of Selenium Base,
a test automation framework that you can find on GitHub.
Today, I'm going to talk about
the 15 unique syntax formats for structuring your Selenium Base tests.
Let's start off with the very first one,
which is base case direct inheritance.
Now, one way of using Selenium Base in your tests
is by an import statement from Selenium Base Import Base case,
followed by having a class import base case directly.
Now, your tests will automatically get
a web browser window spun up when the test begins,
and then you have access to all the Selenium Base methods.
Some of the most common ones are open type,
click, assert element,
assert text, click link text,
assert exact text, and assert no JS errors.
So this is a very common structure that you will find among most
the examples that are found in the Selenium Base examples folder.
And from GitHub, you'll see that there's a lot of examples.
And you can run these tests
and you'll be able to test websites,
automate various activities, et cetera.
So that first one with from Selenium Base Import Base case,
as well as inheriting base case in your class,
that will get you set up.
Another more advanced way is base case subclass inheritance,
which is something you want to use
if you want to have more flexibility within your tests.
And you want to customize the setup and tear down methods
that are already included with Selenium Base.
So you might, for instance, want to report test results
to your own server at the end,
and you want to make an API call,
depending on whether or not the test passed or the test failed.
And you can do that by, or I'll show you from the top.
So again, you have from Selenium Base Import Base case,
and then you have a class that you create
that also gets base case.
But now you're going to overwrite, say,
the setup and the tear down methods.
So if you overwrite the setup method,
make sure that you call your custom code
after you run the Python super command,
which will call the default Selenium Base Setup method,
and therefore spin up the web browser.
And now in your own setup, you can navigate to another page
and perform additional setup steps
with a tear down method.
You most likely want to, say, have a customized tear down
based on whether or not a test passed or a test failed.
So you can see here, there's a method, has exception.
And if you call that, it will run that code if the test failed,
or with the else statement, you'll run this code if the test passed.
And you should also, if you make any changes here,
you should also call the self.saved tear down screenshot method
so that if a test failed, it will save the screenshot
at that point, rather than another step
if you say have a custom tear down that you want to perform,
which you don't want as part of that saved screenshot.
You can also add your custom methods,
such as maybe a login method, logging into your website,
of course, or other methods.
And then in order to use that, again,
you will instead of inheriting base case, as is done here,
you will inherit the name of the custom test class
that you created, which was base test case in this example.
And now you can call the methods that you created
and it'll automatically include the slimming base set up
and tear down, as well as your extended set up
and tear down steps, if that's what you've done.
The third syntax format of Selenium base is pi test fixtures
with number three is pi test fixtures of no class
and number four, pi test fixtures in class.
And SB is a pi test fixture that was created for this purpose.
And here, instead of having an import statement,
which you no longer need,
you import the pi test fixture directly
into the test method definition.
And that gives you access to all of Selenium base functionality,
including the setup and tear down steps.
So a pi test fixture is essentially
like an import statement, except instead of importing
something at, say, the top of your Python file,
you'll be importing something directly into a test.
And that fixture can also include custom setup
and tear down steps as Selenium base includes
for spinning up and spinning down web browsers.
So number three and number four, mostly the same.
You can see in number three, we're not using a Python class.
Whereas in number four, we are.
And the syntax is mostly the same,
except you'll notice that you have the additional self-argument
in the test method definition.
And that self basically represents the class.
So if you want to call method that's
part of the class object, you'd be able to call it with self.
And then you get the SB fixture as the second argument
instead of the first, because the self
has to be the first argument whenever
you have a Python method that lives inside a Python class.
And you can see here, you get access
to the Selenium base method, such as open type click, et cetera.
But unlike the base case way where you'd use self.open,
now that you're using Selenium base as a pi test fixture,
you'll be using sb.open, sb.type, sb.click, et cetera.
The fifth way, or the fifth unique structure,
is using the pi test request fixture.
Now, again, using pi test fixtures,
but now you have a little more flexibility
as to when you load the sb fixture.
So for instance, if you didn't want to spin up
your web browser immediately when you start the test,
you can put some code between this line and this line here.
And then when you're ready to spin up the browser
to do automated steps, automation steps,
essentially with Selenium base,
you can then say, sb equals request.getfixtervalueSB.
And that will load the pi test fixture, sb,
and give you access again to Selenium base methods,
the Selenium base setup step,
and the Selenium base tear down step.
And number five and number six are mostly the same,
except with number six again, we're using a class
and here, number five, we were just creating a method
without the class.
And as before, you no longer need an import statement
at the top of your Python file
when you're using pi test fixtures
because that is the import there.
I import the request fixture
and then I use the request fixture
to call getfixtervalueSB,
which returns the pi test fixture
and runs the Selenium base setup
and gives you all the methods.
And at the end, you can do a method such as sb tear down
so that you can automatically close your browser
when you're done using it.
So those are numbers five and six
for the syntax formats.
Numbers seven through 15,
it's basically Selenium base in different languages.
So for instance, number seven,
Selenium base in Chinese
from Selenium base.translate.Chinese import
the Chinese base case.
I can't pronounce that or really read it,
but basically how it works is you import the base case
from the various language translations.
And now because there's a one-to-one mapping
of Selenium base methods
to all the different languages,
you can now use those translations
instead of the English version of Selenium base
to do method calls.
And so here we have Selenium base in Chinese.
There's also Selenium base in Dutch
from Selenium base.Translate.Ch
import tests give all
and it's all in Dutch.
I don't know Dutch or most of these languages.
Selenium base in French.
Pretty much the same idea
from Selenium base.Translate.French import cost of base
and methods are again in French.
Selenium base in Italian, number 10.
Number 11 is Selenium base in Japanese.
And you can see it's using the Japanese method definitions
to call Selenium base methods.
There's also number 12 Selenium base in Korean.
There's also number 13 Selenium base in Portuguese.
Number 14 Selenium base in Russian.
And I can actually read this
because I know some Russian.
Selenium base in Spanish is number 15
and pretty much those are the 15 different ways
you can structure your Selenium base tests.
And you have a lot of flexibility
depending on which one you want to use.
The most common in the examples is of course number one
but like in business you're automating for work.
You probably want to have custom setup
and tear down steps in which case
you'll probably be extending base case
and modifying setup and tear down
so that you can call other functionality related
to what you do.
And number two is probably maybe the most common
for non beginners because if you're a beginner
the base case direct inheritance is the easiest way
to understand what's going on.
As you can see it's very clear and succinct
but if you want something more advanced
then you have that flexibility.
And so that pretty much covers the different
unique syntax formats
and I can end this tutorial with a running a few tests.
So for instance run the regular, let's say
pi test English test one which is say
a regular English translation of Selenium base.
It will run through type in text to a website, click
and do various things
and if we want to see what that looks like
S base print English test one
and it looks like this right here.
So from Selenium base import base case
that's what we just ran class my test class
you create your test
and then you have access to the Selenium base methods
that you can call pretty easily.
And let's say we wanted to run say the Japanese test
so that would be S base print
Japanese test one so I'm going to show you
what that looks like now.
So here's the Japanese test you see here.
So I'm going to run that pi test Japanese test one
and it's going to run that
and you can see that you can hit a page
that's in Japanese
and you're using Selenium base methods
that have been translated in Japanese
in order to run this automation script.
So this type of flexibility allows people
who don't speak English
to write Selenium base tests in their own native language
and that may be easier if people don't want to have
to learn all the English translations that are available
but if you speak English
then you'll probably be using the English translation
of Selenium base
and of course that gives you the flexibility
to use the first six syntax formats
which are based in English,
the base case direct inheritance,
base case subclass inheritance,
the SB pi test fixture no class,
the SB pi test fixture in class
using the request fixture
and with no class and the request fixture in class.
So that covers this tutorial of Selenium base
and if you want to learn more about Selenium base
there is Seleniumbase.io
which is essentially a copy of the GitHub readme
so you can find Selenium base on GitHub,
you can install Selenium base
from the Python package index
or you can clone Selenium base
and run python setup.py install or pip install dash e dot
all those instructions are in the readme file
as you can see for getting set up
and installing running Selenium base.
It's a very powerful web automation framework
and I hope you found this tutorial useful
and there'll be more exciting tutorials coming up
so have a great day.
Bye bye.

############################################################

[22/44] VIDEO: How SeleniumBase deploys to GitHub and PyPI
URL: https://www.youtube.com/watch?v=SVlR-guVsQE
------------------------------
(Source: Original Transcript)
Hi, I'm Michael Mints, and today I'm going to show you how slending base does releases.
If you're not already familiar with slending base,
it's a test automation framework on GitHub.
Today we're going to tackle a few issues for the next release, which currently
we're on release 1.49.12, but we're going to push this to 1.49.13 during the session.
So, a few improvements that we're going to make today are file downloads.
Right now, as you see from this stack overflow article,
you may encounter a prompt when you try to download multiple files on the same website
with using Chrome or Chromium browser such as Edge.
We're going to create the fix to this, as well as another issue where with Firefox
you may be asked to save a file and you don't want that prompt showing up.
So, there's already a solution where you can disable file prompts when downloading files
and the solution is already here, and we're also going to update some Python dependencies
and figure out which dependencies are out of date.
You can easily just run a command, pip list, dash, dash, outdated,
and it basically says the Python packages that you have that are out of date.
So, when I run this command, it shows that coverage, parso, pi test, HTML,
and richer little at a date.
So, for this release, I'm going to update coverage to 5.3 and rich to 6.2.0.
And I've actually already made all the changes that I'll be making for this.
So, let's see now with SourceTree, which is basically my UI tool for deciding what I'm going to push.
I can say I already changed the requirements file to update coverage and rich,
same with the setup.py file.
I'm also going to make the improvements to downloading files, which is done in browser launcher,
where essentially we set Chrome settings, Firefox settings,
and edge browser settings to update the download ability, as you saw from Stack Overflow.
And I'm also going to make a minor change to base case where I adjust the allowed timeout
for asserting that a downloaded file was downloaded fully.
And not much change there. I changed the small timeout to a large timeout,
but that's really only changing 6 seconds to 10 seconds.
And I'm also going to add a test for that.
And the first thing I want to do is since I've already made these changes,
I can do pip install dash.edu, which will basically install the updated dependencies.
And then if I run pipless-dash outdated again, I should see fewer outdated dependencies.
Just going to have a quick drink of tea while that happens.
Okay, so it should be getting a response now.
And here we go.
Okay, so we saw that rich was updated and also coverage was updated.
So now the only two added dependencies are Carso and PyTest HTML.
And I'm going to leave those where they are right now because having the latest version
of those is kind of going to break slunning base.
So now that I've made those changes and I've also created a test to test out the new changes
to file downloading, I'm going to run this exact test using Chrome, Edge and Firefox
to make sure all the issues are handled.
So CD into the examples folder, PyTest test, download files, dash dash browser equals Chrome,
which is the default browser.
And for this test, it's going to go to PyPy and download the wheel for slunning base
and the tar.gz file for slunning base.
So once that finishes loading, it's going to download that in the wheel and it said one past.
And I can verify that the files were downloaded by going into the downloaded files folder,
which is a directory that's automatically set for when downloading files.
So now if I do an LS, you can see slunning base 1.49.12.
The wheel file is here and slunning base 1.49.12, the tar.gz file is also there.
So I've run that with Chrome.
Let's also test that with Firefox, dash dash browser equals Firefox.
And it should again download those files when going to the website.
Also, every time you start a new slunning base test, it clears out the downloaded files folder
so that earlier tests don't impact that.
So we'll see that the download was completed and then it completed the other file.
We can already see that happening automatically from the test.
So that should pass.
And we can also test that with dash dash browser equals edge that we also have that working.
So now it's going to spin up the Microsoft Edge browser and check that there are no issues downloading these files again.
All right, so that file was downloaded and the other file was downloaded.
Perfect.
So I can say, okay, the changes that I made worked, no issues.
Let's start creating the release.
So let's go into here and say, okay, I already named the branch improve file downloads.
And now I'm going to add browser launcher to stage files.
And here's where I made the changes.
Let's see, improve.
Prevent download prompts from appearing.
And that takes care of the issues that we saw above where multiple files could be an issue could cause an extra prompt to appear.
And as well as Firefox, a certain file type may cause the prompt to appear unless I change that preference to say allow or have those files automatically be downloaded without causing a prompt to appear.
Prevent download prompts from appearing.
Okay, I'm going to commit that.
Next, I am going to change the default timeout for a certain that a downloaded file was downloaded successfully.
So update the default timeout for waiting for down for a certain, here we go, for a certain downloaded files.
Okay, update the default timeout for a certain downloaded files.
Okay, good.
Commit that.
Next, we're going to add a test to make sure that everything is good.
So I'm going to call that add test for a certain downloaded files.
Commit that.
And let's see update the require update the Python requirements.
So let's add that update the Python requirements.
And that's going to be a requirements.txt file and a setup.py file.
So commit that.
Next, we're going to update the release number.
So that is going to be in the setup.py file.
And I'm going to bump that 12 to a 13, so it has 1.49.13 as a new version.
So I'm going to move that into staged files.
And I'm going to call this version 1.49.13.
And I'm going to commit that.
So I'm going to push this to the improved file downloads branch.
Now we can go on to GitHub.
So go to slinning basin.
We'll see, hey, it appears improve file downloads had recent pushes less than a minute ago.
Let's compare and pull request.
All right.
I need a cup of tea one sec.
All right, so we're going to call this improve file downloads.
Disable prompts during automation.
All right.
And I'm going to give that a name improve file downloads to disable prompts during automation.
And all the different things that I'm changing for that prevent download prompts from appearing.
Put that there.
Let's see.
I can say on Chrome Firefox and edge.
Next, I'm going to update the default timeout for a certain downloaded files.
So that's basically giving downloaded files a little longer to appear before like failing the assertion.
All right, so that is in there.
I'm not going to say I added a test because I usually just don't mention tests that I've added for it just the changes that I've made.
I'm also going to say that I updated the Python requirements.
And I'm going to list the specific Python requirements that I updated.
So I'm going to say coverage equals five dot three now.
And I'm also going to list the rich dependency that I just updated.
So coverage equals five dot three and rich equals six dot two dot.
Now I can preview it to make sure it likes good improve file downloads disable prompts during automation.
Or I could even just say,
save all automation prompts.
There we go.
And shrink that a bit.
Nice, picky, keeping it small.
All right, now I'm going to copy this.
I'm going to need that later.
Now I'm going to create a pull request.
All right, pull request is open.
And as you can see, it's going to run some checks.
And I've got GitHub actions basically checking various versions of Python with slinning base as well as
Azure pipelines, which also is going to run tests.
So let's take a look at what that might look like.
Let's click details for the CI build.
And we can see that it's setting up the job.
And run checkout set up Python 3.8 install dependencies install slinning base.
Then to play gate.
Then it's going to install Chrome and Firefox.
Check the console scripts interface install Chrome driver and get go driver.
Make sure Pytest is working and start running a bunch of tests.
I'm going to need more to drink.
It's just.
That's good.
All right.
So let's see now.
It's running a bunch of tests that I have.
And once all the tests complete, we're just going to follow it all the way through.
Let's see.
It's got a lot of exciting tests that it uses to check to make sure that everything was working up.
The 3.8 build is completed.
And the others are getting ready to be completed as well.
So these should be almost ready.
Up.
That's done.
And one more waiting on that.
Up.
That one's completed too.
So if I go back to the GitHub page with the pull request.
And then I refresh the page.
You can see that all checks have passed.
So great.
Everything's good.
I can now get ready to ship version 1.49.13.
So I'm going to merge the pull request and confirm the merge and delete the branch.
Now I'm going to go to slinning base.
And next I'm going to click on releases.
I'm going to click draft a new release.
I'm going to call it V1.49.13.
I'm going to paste what I had in the clipboard.
Add the release title.
And click publish release.
We now have version 1.49.13.
We have group file downloads, disable automation prompts.
So now that we've got that, there is one more thing that we need to do,
which is releasing to the Python package index, which will basically be slinning base right here.
So right now it's still on 1.49.12 because it's a separate command to release to that.
I'm going to run a script.
Python setup.py publish.
And it says confirm release, publish the pi pi.
And I'll say yes.
And it's going to do a code health check with flake 8.
And once that's good, it's going to build up the packages and then ship that to pi pi.
So it looks like everything is good with flake 8.
Now it's copying files, packaging everything up.
And on the last step, publishing the release to pi pi, it's going to upload the wheel file.
And the tar.gz file.
And then finally it says the release was published successfully to pi pi.
So now if we go there and refresh the page,
that version 1.49.13 has been shipped to pi pi.
And now it's done.
So we've created the release on GitHub.
We package slinning base and put the release up on pi pi.
And now the release is complete.
And these numbers here will update shortly after enough page refreshes, usually takes a little bit.
But essentially we have the release ready.
And everyone can use slinning base 1.49.13 now.
So thank you for listening in on this exciting tutorial.
And we hope that you come back for more.
Thank you very much.
I will see you all another time.
Bye bye.

############################################################

[23/44] VIDEO: SeleniumBase Case Plans: Test Case Management integrated into GitHub
URL: https://www.youtube.com/watch?v=XvPrtSLlyck
------------------------------
(Source: Original Transcript)
Hey friends, it's Michael Mencier, the creator of Selenium Base, and today's exciting tutorial is going to be on Selenium Base Case Plans, which is essentially a very clean integration of Markdown Table Technology so that you can store your Test Case Plans right in GitHub alongside your tests.
So this can essentially replace your existing Test Case Management Software if you're bold enough to use Markdown tables like this in order to describe your tests and have those descriptions live in GitHub with them.
So as you can see here, these tables look very clean and everything is living right inside a Markdown file, which is a .MD file.
So as you can see here, description of a basic test, you have your step descriptions and your expected results.
So as we go into say another one here, we log into the SAS demo site with the standard user, and we want to make sure that log in was successful, and then we can add items to a cart, remove items from the cart, and you know, make sure there's a thank you message after you check out and all that.
If you want to see what this particular test looks like when running it, that'd be PytestTestSwagLabs.py from the Selenium Base Examples folder, and you can see it runs pretty quick.
If you want to just see this run a little slower, you can do PytestTestSwagLabs-dashslow, and it will slow down the test for you enough so that you can see exactly what the test is doing.
Although if you want to see more details about the tests, you can use dash-dashdemo mode, which will also highlight the browser actions being performed by your test.
So that is just quickly running the test quickly, and then slowly, let's go back into Selenium Base case plans where you can see this fancy Markdown table.
In order to activate the case plans GUI, this type S-based case plans on the command line, and you'll see this nice table that essentially collects all the PytestTests that it finds, and the tests that you see here will be exactly the same ones that you would find if you did Pytest-dash-co-q.
As you can see here, it has all the tests listed that you could run directly. Now with Selenium Base case plans, or the generator here, it generates a Markdown table for you.
So let's say we wanted to do a case plan for one of the tests, such as test. Let's find a good one. I think there was a test coffee cart.
Yes, here we go. TestCoffeeCart.py. That did not have an existing case plan, so we're going to check that button, and then we're going to click the green button here, generate boilerplate case plans for selected tests missing them.
We click that button, we'll see a message. One new boilerplate case plan was generated.
So if we click OK, and we go into our view, we will be able to see the TestCoffeeCart right here.
And as you can see here, it is just a boilerplate. There is no test written there because all it is is just a boilerplate Markdown table, which makes it easy for you to fill in the steps and the expected results.
And the Markdown table that you see here will render beautifully once it's completed.
So let's say we want to create the test case description of the existing tests. So we will go and open it, open test coffee cart, which basically adds a cappuccino,
a flat light white and a cafe latte to the cart. And then it goes through the checkout process types in your name email and then submits for payment and then make sure that you have thanks for your purchase.
So let's just run that one quick so you can see what it looks like.
PytestTestCoffeeCart.py goes pretty fast. So I'm going to slow it down. This time I'm going to use a demo mode TestCoffeeCart-Demo.
It's going to go in. You're going to see that it's first asserting the title. And then it's going to click on three coffees and then it's going to go to your cart.
And then it's going to show you that you know that is the total. It verifies all information types in your name email, submits, and you get a thank you for your purchase.
So let's say we wanted to create the test plan for this particular test. So we're just going to simplify things for the moment.
Let's see add three coffees to the cart and then verify coffees are in the cart and then perform checkout and then verify checkout successful.
Okay, so that is the markdown table that you have here. The next part is let's say we want to generate a summary of all the existing case plans.
Well, there is a button for that generate summary of existing case plans. You can see that now it generated a full summary.
And if we want to view what that looked like, we can go to open case summary dot md and you'll see it has collected all the different existing case plans that are there into a nice summary file.
And if we searched for our coffee one here, you can see that it has it all here using the summary, the code syntax and the markdown table.
And when all this is rendered, it's going to look just like the examples that you see here.
This was the boilerplate table that was generated. That's what the boilerplate table looks when rendered when you haven't actually filled out any steps.
And then here's how something looks when you've actually filled out a bunch of steps so that you actually have a full detailed description of a case plan, which is quite convenient.
And the slitting based case plans generator just basically integrate some markdown table technology with GitHub so that you can store everything there.
Here's an example of a case summary file that I already had checked into GitHub. It shows you the total number of case plans with customized tables, which means you've done more than just created a boilerplate, which is what you get when you create the new boilerplate for the test plan.
But you haven't actually filled it out yet. And if something went wrong, like you accidentally deleted the table or something, then this will be the symbol.
So here are the tests that are already there. And you can see that earlier we had things like test demo site and my first test, et cetera.
So as you can see here, the summaries look quite beautiful because the markdown tables render quite nicely in GitHub.
And individually you can go into the case plans folder that will be created and you can go into individual case plans and see all the steps.
Like here my first test test swag labs where you have the first demo that we ran you log in and you add a backpack to a cart and then check out and then verify that you got the thank you message.
So that essentially is a full summary of how case plans works.
Markdown table technology. It does all the heavy lifting for you, which essentially is organizing everything, creating boilerplate, markdown tables, and then combining everything for you into a nice case summary file.
So that things look really nice once everything is on GitHub.
And the case summary file here is an example of that there. If you go into the slanting base examples folder, there is one there so that you can see how it all renders once it's complete.
If you go back into the GUI, as you can see here, all the check boxes are ones that you've already decided to create a boilerplate for and a test description filled out.
The unchecked boxes are ones that you haven't yet created test descriptions for, but that is the big summary of case plans.
It's basically test case management stored in GitHub, beautiful markdown tables, everything is nice. And then you can have not just your code in GitHub, but all your test case descriptions and test case management there as well.
All right, well, thank you once again for joining me for another exciting slanting base tutorial and there will be more exciting tutorials to come.
Thank you and have a good night.

############################################################

[24/44] VIDEO: XKCD with SeleniumBase Dialog Boxes
URL: https://www.youtube.com/watch?v=zV0X1AUdWAk
------------------------------
(Source: Original Transcript)
[No content found]

############################################################

[25/44] VIDEO: Handling iframes with seleniumbase
URL: https://www.youtube.com/watch?v=tn3N1gfS2e0
------------------------------
(Source: Original Transcript)
Hey everyone, in today's slenning based tutorial, we're going to be talking all about
iframes and what makes them different from a standard web page and how you can interact
with elements inside of an iframe when using slenning based.
So to start off, let's take a look at this page which has iframes in it.
So this might look a little familiar to you.
It's like a W3 schools version that slenning based has.
You can see here, I am loading content into an iframe which essentially creates an iframe
inside the iframe that they already created.
If you take a look at the page source here, you can see that the whole right side of the
screen is a giant iframe and inside that iframe is another iframe with more content on it.
So if you look carefully, you'll notice that inside the iframe, there is an html tag
and that has its own head tag and a body tag and inside that iframe, there's a document
which has html ahead and a body which is just like the original page.
So in order to keep track of all these things, so that in case you have to maybe grab text
from the body or something specific in that.
With slenium, you have to switch into an iframe which then makes it less confusing what exactly
you're clicking on because if you have the same element that appears in your main page
and inside your iframe such as the html tag, body tag, etc. then you need a way to
differentiate those when you interact with them, for example, clicking on them, etc.
So we have some tests that we can run in order to interact with the frame and here are some
slenium based methods that you can use for that.
So for instance, there is the switch to frame method and inside that you can specify the
name of the iframe or the CSS selector for that and that will allow you to switch into
that iframe.
Additionally, once you want to leave the iframe, you have two options.
You can call switch to parent frame which basically takes you up one frame.
So if you're only inside one iframe, you'll leave that iframe or if you're inside
two different iframes at the same time, it'll take you back to the first iframe.
There is also switch to default content which will allow you to exit all iframes if you're
in multiple nested iframes.
So those are the basic commands for that switch to frame and switch to parent frame and
switch to default content.
Additionally, there's also a context manager format that you can use using the with statement
so you can do with self.frame switch and the same syntax that you would use for the
regular iframe methods.
And then whenever you leave that with block, you'll exit that iframe that you've entered.
So you can see here with self.frame switch iframe result, which was that first iframe on
the web page, you can then do another one inside here with self.frame switch and then go
into the nested iframe inside of there and then once you've left the with block which
is indented, then you're back to the original content or original iframe you came from
before you entered.
In addition to that, Selenium Base also has this really special method called set content
to frame, which basically makes the entire page become whatever was in that iframe.
And then you can do self.set content to parent to get out of that one or set content to
default to exit out of all the iframes that you've turned the page into.
So at this point, I am now going to run all these three different tests in demo mode
so it slows things down and you can see the asserts as they come in.
You'll notice that this first test here should probably get the same results as this
one because all that changed is that we're using the context manager format for the second
test, but it's entering all the same frames, et cetera.
But the one that will be quite different is the set content to frame which will totally
enter the iframe, making the whole page that, and then leave that.
So let's start by running those particular tests.
Let's see, pi test iframetests.py, dash v for verbose mode, dash dash rs so that we can
reuse the session between tests, and then dash dash demo to slow things down.
So you can see here, it's clicking run, and then it's verifying the text inside first
iframe, and then it already switched into the second one, and it's verifying text
and that.
It switches out, verifies text, switches back in, et cetera.
So now another test is running.
It's running pretty much the same test that you saw before, but now it's using the whiff
statement for the context manager format.
It's going to look very similar.
It's going to verify the text that you saw before, and then the third test is now running
and that is going to set the whole content to the page.
That's pretty special there.
So you can see here, it ran those three tests, and if I just want to rerun that last one
because it's extra special, pi test that, and then dash v for verbose mode, which basically
just prints out the name of the test as you run it, and then dash dash demo to slow things
down and highlight the actions.
You can see here, it clicks run, and then it switches into the frame.
You can see the whole page became the contents of the iframe, which is pretty cool.
So that is essentially iframe functionality and how to switch into it, switch out of
it, et cetera.
It was selenium based in a nutshell.
Here's the code that you can see here, very easy.
You can find this in iframetests.py from the selenium based examples folder.
So if you're just wondering how to get to that from selenium based, go to the selenium
based GitHub page, and then you scroll to examples, and then you can scroll down to iframe
tests.
Click on that, and you can see all that there.
Or if you've cloned the selenium based repo on GitHub, you can just see it from your clone,
and also a cool thing you can do from the command line with the espace print statement,
espace print iframetests.py, you can print all that directly to your console output.
And if you do dash n, you also have the line numbers, so you can see those tests and all
the glory that they are to show you how iframes work, and how to use selenium based to interact
with iframes and get out of those iframes when you're done using them.
All right, cool.
So that basically covers today's tutorial on iframes and interacting with iframes with selenium
based.
There's going to be a lot more exciting tutorials to come, so stay tuned and have a great
night.

############################################################

[26/44] VIDEO: SeleniumBase tests in multiple languages!
URL: https://www.youtube.com/watch?v=4ZWa9GwiqKE
------------------------------
(Source: Original Transcript)
Hey everybody, it's Michael Mints, the creator of Slenium Base, and today we've got another exciting Slenium Base tutorial for you.
Today, we're going to talk about how Slenium Base is translated into multiple spoken languages, which basically allows you to have tests in all the languages you see here.
So, you might already be familiar with the basic tests that's in English, so for instance, if we open the English test, you know, everything's in English.
However, you should note that there are also ways of writing your tests in other languages, such as Chinese, as seen here, or you can even do, let's see, open the Dutch test.
And let's see about the French test.
Okay, and next, let's take a look at the Japanese test.
And how about the Korean test?
And next, let's see the Spanish test.
And then let's take a look at the Russian test.
And then let's take a look at the Portuguese test.
So, as you can see here, just all these different languages make up all the different possible ways you can write your tests.
So, let's start running all these tests starting from the English one.
So, let's do PyTest, English test one, and it ran that.
Let's do the Chinese one.
That is that, and let's do PyTest Chinese test one.py.
Run pretty quickly.
Next, let's do PyTest Dutch test one.
And then let's do PyTest Korean test one.
PyTest Japanese test one.
And let's do PyTest Spanish test one.
PyTest Russian test one.
And PyTest Portuguese test one.
So, as you can see here, not only can you write your sliny based tests in English,
but you can also write it in a completely different language, and it runs just fine.
So, let's say if we just go back to the Chinese one, just one of the example tests that we have here.
And you can see that there's a one-to-one mapping of all the sliny based methods
to the various languages that are supported such as here.
And if we were to run this in demo mode, you would also see the highlighted text show in that particular language.
So, if we do PyTest Chinese test one, dash dash demo,
you'll see that the demo mode messages are also in Chinese.
So, basically giving you the full power of sliny based translations in a nice package like this.
So, here you can write a test in Chinese, for example,
and then run your test with lots of Chinese characters and all that.
All of that is supported quite easily, including demo mode,
which shows you what assertions you're making while you're on a page.
In addition to that, there's also the ability to translate existing tests from one language to another.
So, if I were to open the English test one here, for example, you see everything's in English.
If I do a space translate English test one,
and I do dash dash zh for the Chinese language code,
and then dash p to print, you'll see that it took that exact same test
and it printed out the Chinese version of that same test.
And with the translator, you can also make a copy of that file or overwrite the existing file.
So, if I go back to here,
a space translate English test one dash dash zh,
and I then do dash c for a copy,
it's going to create English test one dot underscore to zh.py,
which actually is now in Chinese, if we open that up,
you'll see that it translated the test into Chinese.
So, with this one to one mapping of every language to every other language in Selenium Base,
you can write your test in one language,
and then have it translated and still run in a completely different language.
Isn't that cool? You can even translate something that's not in English to another language, that's not English.
For instance, if I were to take this test here,
so, s space, translate, let's do Chinese test one,
and then let's do dash dash j to turn that into Japanese,
and then dash p to print,
you'll now see that it translated all these APIs here into Japanese
while still retaining the content which is in Chinese.
Actually, it might be confusing if you don't know Chinese or Japanese,
and you might be mixing up the languages.
So, let's make something a little more clear.
If we do, s space translate, Chinese test one,
and let's translate that into, say, Spanish,
and then dash p to print,
you'll see now that the methods are in Spanish,
but the actual things that the test does,
it's still gonna, you know, click on the same buttons
and verify the same text in the Chinese that was there,
but the APIs are the things that are translated.
So, these two lines here, you'll see like the import,
and this line here, that gets translated into the language that you want,
and then here you have all the APIs, like verifying the element,
verifying the text, or clicking on part of the page,
that is translated.
That's just one of the really cool features of Selenium Base,
the translation API,
and there's documentation on how that works,
such as all the languages that are supported,
the actions that you can do, such as printing the translation to the console,
or overwriting a file,
or making a copy of an existing file,
and then there are some examples here, in case you're wondering how it works,
and the translator, as you can see, like when you print it,
it shows you the text here.
This is sort of like an enhanced version of the s space print command,
so if I just do s space print and English test1.py,
you'll see it prints it out,
or if I do with that same code, but with dash n,
it also adds the line numbers on top of that.
So, that's just one really cool feature of Selenium Base,
the ability to translate your test into a different language,
and let's say we want to run all those tests very quickly,
multi-threaded,
we can do it like that,
PyTest, dash dash headless,
dash n8 for n parallel threads,
and it's running all that.
In addition to that,
we could also single-thread it and make it non-headless
so that you can see what's going on.
So, let's do,
instead of multi-threading it and doing a headless,
we'll just do dash,
the dash dash rs, which will reuse the browser session,
you can see in the right here, dash dash rs,
it'll reuse the browser session between all tests
so that it speeds things up,
instead of spinning up a new browser for each test.
So, it's going through all these actions,
and as you can see here,
we're just running different language Selenium Base tests
on these websites here for Wikipedia,
and it's just like a fun really cool thing to do.
And you can see here all these tests passed,
which is good.
I keep them up-to-date in case Wikipedia makes a change
to their website so that they continue working,
even as the page is changed.
I'll just update the test as needed.
All right, well, thank you for tuning in
to another exciting Selenium Base tutorial
for all your Selenium Base needs.
You can check out the GitHub page,
github.com slash Selenium Base,
slash Selenium Base,
and you'll find just all the documentation
for all the cool things that you may want to do.
Well, it was great of you to tune in to this exciting tutorial,
and there'll be a lot more exciting tutorials to come.
So thank you for tuning in,
and have a good night.

############################################################

[27/44] VIDEO: ChatGPT in GitHub Actions + Playwright vs SeleniumBase
URL: https://www.youtube.com/watch?v=4pLmqXAk6Rg
------------------------------
(Source: Original Transcript)
Hello and welcome to the automation show I'm Michael Mintz and today we're going to be covering chat GPT in Github actions
And we're also going to be comparing playwright with Selenium base. So let's get started with a live demo to kick things off
We're going to run Python raw chat GPT.py from the Selenium base
CDP examples folder. We're going to do a query compare playwright to Selenium base and under
178 words and then the script is going to find the output and then display the output inside here
So you can see here we bypassed any
Antibot defenses that chat GPT had and we scraped the data and we can also do this exact same thing from Github actions as you can see here
This is right from the repo. I have called undetected testing so you can see it made a chat GPT query
And it printed out the output and if you're wondering where that is you just go to the MD Mintz area and then undetected testing
Here we are undetected testing where I have lots of examples that people can run and many of these examples are being run inside of Github actions
So for instance, we go to CI build three. That is another example where we're running other ones such as
Data that grabs Nike shoe prices as well as prices from the price line website
Now getting back to the presentation
This is based on my previous presentation unlimited free web scraping with Github actions
Which was actually so popular that memes were generated in various discord channels such as the scraping
Enthusiasts which you can find on discord quite a popular place
There is usually over a thousand people online at the same time and if we go into this meme that someone created there
It was basically comparing the virgin api consumer to Chad independent scraper
And this of course is based on an earlier meme where the virgin api consumer
Essentially has to use tokens and api keys in order to grab the data and all the actions that that person does are
Scene and known by the api provider
Razz Chad independent scraper can bypass those limitations by going directly through the HTML
And the slanting based automation framework is one of those frameworks that lets you bypass
Captures and antibody detection so that you can grab any data that you want
So that's how this meme came about and it became so popular that more memes were generated after that
Such as this one with a Simpsons reference here
Zero days without Github actions mentioned and essentially anytime someone mentioned Github actions in
That discord server this meme came up
So that brings us back to this presentation and also note that it's not just slanting based and Github actions
That can scrape data from chat GPT
Also other companies such as deep seek have also been able to scrape open AI data
And here is another meme that was generated from that open AI complaining about deep seek using chat GPT for its training
And here's the scene from Princess fried where the Sicilian is basically holding the princess hostage
And then he's saying you're trying a kidnap would I've rightfully stolen?
So essentially there's a war going on between all these AI platforms
But likely if deep seek gets too powerful then it'll probably get banned from
Countries such as the US where open AI is supposed to be the AI leader or don't tell Google Gemini that because they're in the running too
For that top spot for AI
Let's jump off to the browser races where we're getting to the next part of the presentation
Where we're going to be comparing the speed of various browser automation frameworks
So in this example here, we have a horse race between
Slenium playwright and Cyprus and technically all these browser automation frameworks can essentially represent a
Jockey driving a horse, but in this example the horse is the web browser and in this particular image here
These are different flavors of chromin chromium. So for most Slenium tests
It's probably going to be using a regular chrome browser
Razz playwright and Cyprus are going to be using a customized chromium-based browser for their races and
Here's another action shot of those going through the race
Slenium playwright and Cyprus driving their chromium browsers and
By the end of the race, you'll have found that essentially there are really two main winners
Slenium and playwright because both are pretty much the fastest automation frameworks
There are in comparison to all the others out there
Although technically puppeteer is playwright in a way
Also super fast, but we're only going to talk about these two mainly because they're the most popular ones for test automation
So let's get to the data where we're going to be comparing all these metrics of
playwright versus slenium base and I have a nice repo for that MD men's slash playwright versus slenium base where I'm basically
recording all this data
And there are all these examples that are being used and they're being run inside the GitHub actions here
You can see here all these builds for Windows, Ubuntu and Mac OS
And if you go through the data here, you'll find that starting with Linux
Slenium base and playwright are relatively close to each other depending on what you're doing
So with a browser launch, Slenium base was a little faster, but running an individual test
Playwright was a bit faster, but if you're running multiple tests at the same time, then slenium base was able to win that race
So let's go over to the GitHub actions job for that. So for instance, I ran every test three times so that we could get an
average or actually the median of the data made it easy. So for instance
if we have slenium base launching a headless browser here
Here and here and then we have playwright launching a headless browser here here and here
I was able to collect all the metrics, grab the median number and put that into the chart that you saw there
So if we jump all the way to the headless multi one, so for instance here
You can see three tests passed in 1.12 seconds and also here
Three passed in 1.09 seconds. This is for slenium base
However, when playwright ran the same scripts, it was a little bit slower
So for here three passed in 1.70 seconds or here three passed in 1.68 seconds
showing that when you're running multiple tests at the same time, slenium base had a slight advantage over playwright
However, when we go over to the Mac runtime's comparisons
slenium base had a significant advantage over playwright
You can see here with the runtimes
Slenium base was significantly faster than playwright when running multiple tests and still a bit faster when running individual tests
So if we go over to the github actions that I grabbed that data for will jump right to the headless
Multi launches
I'm going to show you the code for these scripts in a sec just that you can see the comparison
You have three tests running and going to different URLs and then printing out the URL to the console out
So here you see 0.79 seconds and here three passed in 0.90 seconds and then if we open up the playwright version of the same
scripts you'll see that I took significantly longer three passed in 2.17 seconds or three passed in 2.24 seconds
so jumping back over to
the repo here
All those numbers are in the chart here. So now let's take a look at the tests
So for instance with the sp headless flow we're running a script and we're grabbing the runtime
Using the runtime decorator I have we're gonna print the runtime for all these actions and then run it here
And the equivalent for the playwright version is here PW headless flow
So it's the same script that slanting based ran except that it's using playwright instead
So it's going to do all the exact steps and it's also going to grab the runtime and print that out
And that's how I'm printing out the runtimes
And then if we jump over to something such as sb headless multi
You'll see that it's running three different tests
It's going to go to a URL and then print the current URL to the console output for those three different tests
And the same thing is happening with the playwright headless multi example
It's going to go to those three different URLs and print out the URL to the console
So that was the data that we were collecting from the tests that we ran and
All that is shown here also note that I didn't have the windows stats here yet
However after I looked into the windows stats from GitHub actions
Playwright was a little faster than slanting base in that particular area
So we go to windows we can let's go over to
The headless multi one where we have multiple tests running at the same time
Here's the stats for slanting base here's like three past and two point two nine seconds
And if we compare that to the playwright version
Three past and two point oh nine seconds. So playwright was
a bit faster on
Windows so essentially whoever wins the race depends on the operating system that you're using so for instance
If you're using Linux, it'll be a close call depending on what you're doing
If you're using macOS, then slanting base is going to be faster than playwright and if you're using windows
Then playwright is going to be faster than slanting base
So these are the stats and you can run all these examples yourself
We can also run it directly from the conflap put here
So let's do python rob pw have this multi to run the playwright version of that script
It's going to go through it's going to run it and oh wow that was slow for playwright
But usually there's some caching involved that you run it more than once so if you run again
It should be a little faster. Oh there we go through past in 4.60 seconds
run again
Okay, 3.77 seconds for that. So that's the playwright version and now we're going to
Run the same thing but using slanting base and here are three past in 2.00 seconds
It's run again up there we go three past in 1.28 seconds
Always varies by a bit. There's some fluctuations in internet three past in 1.46 seconds
So if we open up the scripts here
Let's do raw sb had this multi open raw sb
Have this multi just so you can see that I've got the script there and now we're going to open raw pw
have this multi
And you can see here that it's essentially the same thing but using its respective
web automation frameworks
So they're going to be using pites test for both of these and the comparison shows that
Slanting base was on top at least on macOS where slanting base has a significant advantage
So that's comparing playwright and slanting base in terms of performance and all this you can find in the
Github area playwright versus slanting base
You can see all the example scripts as well as the github actions jobs that record the data and
For the final part of this presentation
Let's go through the raw chat gpt script that I ran earlier which basically queried chat gpt
So I'm essentially doing this from slanting base import sb
And then I'm going to call with sb you sequels true test sequels true ad block equals true as sb
And then I'm going to set the URL and then I'm going to activate cdp mode
Which is the stealthy mode that allows you to bypass captures as well as bot detection systems
Now I'm just going to sleep for a second just so that it's not running too fast and gets rate limited etc
Because sometimes if automation clicks too fast even if they don't detect your bot
They might think that it's a bot simply because it's clicking too fast
And I'm going to click a thing if it's visible the closed dialog box because sometimes there's like a pop-up that appears
You know announcing some chat gpt feature or something like that
And we can just click it if it's visible
And then we're going to do this query compare playwright to slanting base and under 178 words
And I'm going to use the press keys method to slowly type out all those characters into this element with this CSS selector
And then I'm going to click on the send button and then I'm going to print input for chat gpt
And then I'm going to sleep for three seconds as it starts typing out the data
And then with the suppress exception so that even if the next part fails it doesn't fail the whole script
I'm going to wait for an element to not be visible this particular element here the button with data test id
Equal stop button because essentially there's a stop icon that appears as chat gpt is typing
So that it finishes its typing before you send in any more queries
So if that fails or if it succeeds this wait for then it's going to go on to the next part no matter what
And it's going to find the element here where it's going to find the chat from the data message author role assistant
Markdown selector and then it's going to use a Python library called beautiful soup to basically parse that HTML in a
Pretty way so that it looks nice when you print it out
And then it's going to do the print line that prints all that data to the console response from chat gpt
And then it's going to you souped out replace the new line character with a colon here
This just tighties it up and then it looks all nice and neat when you finally get to it
So that is that script that we ran there and we can run it one more time just for fun because why not here we go
chat gpt.com
We're going to compare playwrights a slinning base and under 178 words
And it's going to
Type a thing and it's going to talk about speed and performance
But I already showed you the real speed and performance metrics through github actions
That essentially shows you that even if chat gpt says that playwright is faster than slinning base
It's not true if you actually look at the raw data itself because I collected the data
And I found that on macOS slinning base is a whole lot faster than playwright and on linux
Roughly the same depends on what you're doing and yes on windows playwright is
Faster than slinning base
so
Give Microsoft a win for that one
But otherwise it's a close call for linux and slinning base has a very nice advantage in speed against playwright on macOS
So that was my exciting presentation
And remember to check out the slinning base page on github for all the information
So for instance the chat gpt example that I ran it earlier was using the cdp mode feature
Which is a stealthy feature that lets you bypass captures and bot detection
And you'll see here links to various youtube videos that I have from that page
And lots of instructions on what you need to do in order to bypass captures
There's special methods such as you see gooey click capture which lets you bypass a simple
Cloudflare capture if there is one on a page
There's also a regular bot detection
Defense that basically lets you bypass that bot detection
And all these examples are here
So much if you just go into the cdp mode folder which is in the slinning base examples folder
There just tons of different examples that you can run
Such as the chat gpt example that I ran for you earlier here
So great that is what I have for this presentation
And be sure to check out the youtube channel for more exciting slinning base presentations
On all the various things that you might be interested in
And I'll see you all next time

############################################################

[28/44] VIDEO: CASB explained, and the stealth required to test it
URL: https://www.youtube.com/watch?v=Sf6B3dMYObQ
------------------------------
(Source: Original Transcript)
Hello, I'm Michael Mints, and welcome to CASB Explained and the stealth required to test it.
So this is going to combine two of the worlds that I'm in, which is the cybersecurity world and the
automation world. So here's a simple diagram that explains what CASB is. So without CASB, the user
connects to a cloud service and data is exchanged freely between them so that any data between the
user and the cloud service is strictly between them. Whereas with the CASB service, there's an
MITM proxy, which stands for Man in the Middle, that basically intercepts all that data going back
and forth between the two, and therefore the CASB service can process that data, put it inside a
database, display in an event log, and there's also usually an admin app where the CASB service can
be configured. And the screen part here is the CASB service and it usually belongs to the company
paying for it, and the user is generally a member or employee of that particular company.
So what does CASB and what can CASB do? So CASB stands for cloud access security broker.
It's a software tool that monitors and enforces security policies for cloud applications.
CASBs can be deployed on-premise or in the cloud. So how does CASB work? So a CASB acts as an
intermediary between cloud users and cloud service providers. It monitors all activity between
users and cloud applications, enforces and organizations security policies. It provides visibility
into cloud app activity. It helps organizations comply with cybersecurity regulations and there are
lots of benefits such as being able to control sensitive data and being able to monitor and detect
suspicious activity. So this diagram should make a little more sense now. The CASB service basically
comes in between the user and the cloud service, intercepting all the data and then processing it
in summary. So let's talk about CASB in the news. So recently, Tulsi Gabbard, the director of
national intelligence for the United States, basically fired more than 100 intelligence officers
from the CIA over messages that appeared in a chat tool and those discussions went beyond work
to sexual themes and political messages. So basically the CIA employees were doing things that
they shouldn't have been doing and they got fired for it. Here's another example in the news for
that same story. Tulsi cracks down on deep state sex chat. So there you have that. And there's also
another article in the New York Post. Tulsi Gabbard said she's firing more than 100 intel
employees who took part in obscene sex chat rooms. So how did these employees get caught? Well,
there was a CASB service between them and the chat platform that they were using and all the data
was intercepted and it's basically configured so that if maybe people said something bad that
then that data would appear in the event log and then someone appointed by Tulsi Gabbard would
probably go through the event log and be like, oh wow, these employees were saying things they
should have been saying on company time, very inappropriate stuff. So then they could be fired for
that particular behavior. So that's just a quick example of how CASB works. So CASB can catch
bad employees in the act just like that example there you saw in the news. And here's just a simple
photo from a TV show called Mr. Robot where bad employees might be up to no good. So CASB can detect
and monitor online activity and that includes inappropriate online activity such as the reason
for firing those CIA employees. So CASB can also bite crime. Here's just another stock photo of
perhaps a malicious actor about to do something bad. So CASB can prevent cyber crimes, cyberbullying,
DDoS, hacking, data theft, data loss and all those things because you know hackers are out there
and hackers have to be stopped from doing the malicious activities that they intend on doing.
So CASB also helps schools. So CASB can prevent students from cheating in class or on exams for instance
if a student was trying to use chat GPT in order to do their homework for them then the CASB
service would be able to intercept that and then the teacher would be able to see that the student
was cheating. It will also prevent students from visiting inappropriate websites such as porn
sites while they're at school and also maybe prevent them from playing computer games on school
computer labs when they should be studying for their exams or doing homework. So yes, it will
prevent students from doing things that they shouldn't be doing. So CASB can also save lives.
So for instance, CASB can prevent planned attacks, terrorist attacks, school shootings and self-inflicted
harm and by self-inflicted harm perhaps a student is researching ways to harm him or herself
and therefore those keywords would appear inside the event log and then the teacher would be able to
identify students with problems and then maybe do something before it's too late.
Another stock photo of Packer. So where does one get CASB? Well, the market leader in the space
is a company called IBOS which provides CASB as well as a lot of other powerful cybersecurity
services such as ZTNA, SWIG, SD-WAN, browser isolation, etc which basically allows organizations
to secure their data. And IBOS is trusted by lots of organizations worldwide such as ADP,
Verizon and Comcast and also schools use IBOS in order to secure internet access for their
students and their staff. So schools might use IBOS in order to install CASB on students'
Chromebooks so that students can be prevented from treating or also catch students that may be
planning malicious activities. And here's just a huge overview of all the various things that are
provided with the educational package that IBOS provides. Basically you can monitor students'
activities when they go to YouTube and there's also a classroom management, a parent portal,
just various ways of enforcing safe policies on students' Chromebooks. And of course there's
also the government category where there's lots of various services that IBOS can provide to
governments. So a little about me. I'm Michael Mints and I created the SlettingBase framework
and I also lead the automation team at IBOS. Nice photo of me there. Here's a photo of me on the
job and here's another great action shot and here's a fun fact. My wife and I once got to
meet Tulsi Gabbard at a house party and this combines the cybersecurity worlds because I work in
cybersecurity and Tulsi Gabbard is the director of national intelligence so cybersecurity people
meet without even knowing it. Close up of that. So now let's talk about configuring CASB.
So depending on the service provider that you're using there's probably going to be a menu with
advanced controls where you can configure various things. So for instance with IBOS there might be
a security policies tab where you can set resource policies, routed policies, you know maybe set
web categories to block certain categories from Chromebooks, etc. You could set allow lists,
block lists, etc. so that maybe you don't want certain sites to be allowed at all or maybe do
want to always allow certain sites. You can set policy layers. There's a YouTube manager. You can
set keywords. There's just lots of different settings that can be configured in order to fully
configure the CASB service. So for instance there might be a Genai chat protection switch so that
you can basically prevent data loss prevention and other things from happening when an employee is
using chat GPT for a query. So for instance that is part of the chat GPT risk module that IBOS
provides where it can monitor chat GPT interactions and also detect risky behavior and block activity
and monitor and report all that to administrators. So for instance in this example here a user tried to
input email addresses into chat GPT but due to the CASB service setting that was set via IBOS
you'll see that an error occurred because it detected that email addresses were in the message
and therefore it was going to block the content directly. So once content is blocked or maybe
something is filtered there's going to be an incident report and there's going to be an incidents tab
that you can check on where administrators can go in and see what exactly was blocked or reported on
and triggered. So for instance here incidents were triggered via an AI risk incident
because someone was sending data into chat GPT that they shouldn't have been sending
and here you can see it contained email addresses and you can click in to get more details
but essentially this thorough report is generated and then this basically provides important details
so that people can take action. So here's a more detailed view of a specific incident where you can see
all the various details that occurred and you can go in you can see email addresses that came in
IP addresses involved the time when things occurred etc. You can see that it'll show the vendor
as chat GPT, it'll show the username and the trigger message which includes the email addresses
that tried to be sent but then were blocked. So this is exactly probably the case of what happened
with the NSA where Tulsi Gabbard fired intelligence officers because there was probably an event
triggered when people were using inappropriate language inside their chat tool and then those
messages all appeared in an incident report and then via the incident report an administrator could
go in and see okay these people are taking part in something that they shouldn't be on company time
and therefore Tulsi Gabbard came in and fired those employees. So that's all part of the
alerting, auditing, logging and reporting feature of iBOSS so essentially any business,
government, school etc can have access to all these different features such as the chat GPT
risk module that was described earlier. There's also plenty of other different capabilities that you
have such as detailed logging and reporting, risk and threat reports, digital experience management
etc. There's a lot of different tools that are available to customers so that all comes back to
this diagram that I showed you earlier where the CASB service essentially comes in, connects between
the user and the cloud service to intercept all the data and then all that data can be processed
in the database and get sent to the event log so that a system administrator can view the data
and take appropriate actions as necessary. And of course there's going to be an admin app
where everything is going to be configured and there'll be lots of switches where you can you know
turn something on, disable this feature, turn on this feature, different tabs where you can set
different settings etc so it's a very powerful tool. So now let's talk about automating CASB testing.
So as you saw before in the diagram there are cloud services out there such as chat platforms
and sometimes testing is going to occur with real cloud services such as chat GPT
so these cloud services can include search engines, email platforms, AI chat platforms,
streaming platforms etc and many cloud services are protected by antibody services
making test automation tricky because the test automation would possibly get blocked unless it
was modified to get around the antibody defenses. So in order to fully test CASB it may be necessary
to bypass the antibody services that are there so that automated testing can work accordingly
and that's how I personally got involved with making automation stealthy and that's also called
anti-bot bypass to make your automation get through so that you can access websites without being
restricted. So here's the test automation framework that I built it's called slunningbase you can
find it on GitHub and basically the description as it shows here Python APIs for web automation
testing and bypassing bot detection and as you can see here there are a lot of GitHub stars
so it's a quite a popular tool. So slunningbase already has over 25 million downloads
from Python which is the Python packaging index where people go in order to download Python packages
so here's a view of slunningbase from the GitHub page directly you can see all the data and details
for it such as stars, forks, number of people watching the number of tags etc and if you scroll
down from there you'll see a powerful read me with lots of details and tools that slunningbase provides
such as you know we're a quarter for instantly generating your tests or a dashboard so you can view
test results but more importantly since we're about to cover anti-bot bypass there are two special
modes called UC mode and CDP mode which are used to provide stealth. So with UC mode that allows
bots to appear a human which lets them evade detection from anti-bot services that try to block them
or trigger captures on various websites and I have a few different YouTube videos about that
and the successor to UC mode is CDP mode and that's a special mode inside of UC mode
that lets bots appear a human while controlling the browser with the CDP driver and CDP stands for
the Chrome DevTools Protocol. Now although regular UC mode can't perform web driver actions
while the driver is disconnected from the browser the CDP driver can because it's using the Chrome
DevTools Protocol in order to perform the various actions such as typing text into text fields
and clicking buttons while remaining undetected. All right it's live demo time so let's back
out of that and go over to here where there's a lot of slunningbase examples in the CDP mode
so for instance if I want to have a test that queries chat gbt I'm going to run a simple test
python raw chat gbt.py I'm going to run that I'm it's going to go in to the chat gbt website
and it's going to type in a query compare playwright to slunningbase and 100 178 words
and then it's going to grab the results there and then print that out to the console when it's
done like here so this is just an example of an automated test going into a website and grabbing data
where normally there's anti-bot protection so the same can be done with a google website so for
instance if we type python rawgoogle.py from the slunningbase examples folder we're going to do a
google search you can see here it's searching for a slunningbase and going into the slunningbase
GitHub page now you might not realize that slunningbase is bypassing bot detection
unless I turn off the stealth ability so let's go into the script and make a modification
going to open rawgoogle.py and I'm going to remove the part that says you see equals true
and now I'm going to run the script again so you can see exactly what happens when you're not
trying to use stealth mode to bypass bot detection so let's do python rawgoogle.py we're going
to go into google and immediately you can see that you're getting a recapture appearing because the
system detected unusual traffic from the computer so this is an example showing that if you don't have
the slunningbase stealth mode enabled then you will get blocked by google or any other websites that
try to block standard automation so I'm going to put the uc equals true right back here
and then I'm going to run the script python rawgoogle.py and this time since I put it back
I'm now able to do the google search and go straight to the GitHub page you can see that the raw
google example worked so this is just one of many examples where we're bypassing bot detection
so that test automation can properly go in to the cloud service and get the data
and that's just one component of testing kazby because if there's a cloud service involved
you need to be able to bypass that bot detection so that you can thoroughly test the kazby platform
so that is that and let's jump right back into the presentation that we had
so let's go back and click so in conclusion kazby is powerful and it needs to be carefully tested
because if you have the government using your software as a paying customer then you had better
be certain that your software works well because if the government isn't satisfied with the results
then you'll be in the hot seat just like zeleenski is here being grilled by trump because he didn't
accept the deal that he was offered and I certainly don't want to be in that tough situation
that's why I got to make sure I have 100% test coverage or else it'll be me in that hot seat
so that concludes this presentation visit iBoss for kazby and all the other cybersecurity
services that you may need such as ztna swig sdwann browser isolation etc there's a larger
list here for instance with security authorization access controls you've got malware defense
you've got data loss prevention you've got browser isolation device posture checks ssl decryption
etc there's just so many different capabilities that are extremely important for businesses
governments schools etc in order to safely and properly secure the data that you have
and basically make everything secure for users your customers and everyone else involved
and also be sure to visit slanting based on github for all your web automation needs
and it's quite popular and there's a lot of documentation in the read me so be sure to check all that out
and i'll see you all next time

############################################################

[29/44] VIDEO: Automating Flight Search while Web-Scraping Prices (Bonus: City Tours!)
URL: https://www.youtube.com/watch?v=HRMohOJHmSA
------------------------------
(Source: Original Transcript)
Hello, I'm Michael Mints, and today we're going to be automating flight search while
web scraping flight prices from various airlines, such as EasyJet, Southwest, United and L.O.
And with all this information, you're going to be able to run these scripts in GitHub actions,
such as in the example here where we have departure times, arrival times, and the price of the flight.
And here's another example from Southwest where we've got the flight times, the number of stops,
and the prices again. And here's a more advanced example where we also include the planes being used,
the flight data, flight number, etc. So all the details that you could possibly want as well as
the flight prices. So with all this automation, we're going to be using a framework I created called
SlendingBase, which you can find on GitHub. And there's a popular feature within SlendingBase called
CDP mode, which is a stealth mode that lets bots appear human while controlling the browser with
the CDP driver. And here's an example, SlendingBase script that basically webscrapes united.com
for flight times and prices. You can see here we're going to go in to find some variables and then
click inside to set the origin, the destination, and then do the flight search, and then print out all
that data. Here's another example. And this one here, you can see that we're going to close a banner
first that appears because sometimes websites make you accept cookies to continue. And then you're
just going to input the data, such as the from location, the two location, airport codes, etc,
as well as the calendar dates of when you want to fly. And then once we submit, we'll find
those flight details and then we'll print out that information. And here's another example here
from Southwest, pretty much doing a similar thing. And here's a similar script with lall.com.
So during this presentation, we're going to be flying to Paris on EasyJet, flying to Chicago on
Southwest, flying to Orlando on United, and flying to Israel on lall. And as a bonus, I'm also going
to share some photos from some of my recent trips to these destinations, and you'll be able to see
some famous landmarks that you'll probably recognize, such as the ones you see here. So up first,
we've got EasyJet, and we're going to be flying to Paris. So let's do a live demo of that.
We're going to exit out of this presentation and do Python, raweasyjet.py.
From the slunning base, CDP mode folder. And now we're going to do a flight search. So first,
we're going to close that banner. And then we're going to go into the from location and type
London Gatwick for the airport. And then we're going to do two Paris, all airports. And then we're
going to set the one time. And then finally, we'll click on show flights. And now it's going to
collect all that data for the flight from London to Paris. And now you can see here in the output,
all the data that appeared for that flight with all the prices, which are in pounds, by the way,
since it's using a British airline. And now you have all that data. So let's jump right back
into the presentation because now we're going to do a quick tour of Paris since we just came there.
So the Eiffel Tower is a definite must go to place for when you're in Paris because from there,
you can go see pretty much the entire city from the top. So make sure you take the elevator up
because that's a fun trip. And then you'll be able to see all the different areas surrounding Paris
because the view from the top of the Eiffel Tower is really nice. And also be sure to check out
the Arc de Trioupe because that is another major landmark in Paris. A lot of people go there,
there's like a giant rotary that pretty much goes around it. And if you have the extra time,
you should check out the Louvre, which is the famous museum with all the fancy artwork,
such as here. You've got a lot of people gathered around a painting where a lot of people are
gathered around a table. That's kind of meta in a way. And you might get a chance to take a selfie
with a statue that's taking a selfie. So that's a cool highlight too. And you may want to check out
the gardens around Paris because they're quite beautiful. Just the plants are amazing. And the
architecture here at the Louis Vuitton Foundation is quite stunning. So check out that if you have a
chance. And you may even get a chance to see a magic show in Paris because they're known for that.
So that's the end of the Paris tour. Up next, we've got Southwest Airlines where we'll be flying
to Chicago. So let's do a live demo of that. Exit out of here. And we're going to do
Python, raw, Southwest.py. And now we're going to run that script. We're going to see how we're going
to type in the data we need. So we're going to depart from Boston. And it's going to set that.
And then the script is going to put in MDW, which is Chicago's Midway Airport, which is a tiny little
airport within Chicago. And I can see that all the flight times and prices have emerged there.
And now all that data has been outputted to the console. So you can see here the dates, the times,
the number of stops, and the price. So let's jump back into the presentation because now we're
going to do a quick tour of Chicago. So Chicago is a huge metropolis. There are just tons of buildings
all around. And on the bottom side, you'll see there's a river there that goes through with also
more fancy views of various buildings. And there's also a boardwalk that you can walk along because
it's right off of one of the great lakes. So you're going to get some nice scenic views there.
And the building architecture is actually quite stunning because there's some fancy designs in
Chicago that you won't find anywhere else such as this building here or that building there.
Just lots of very cool architectural designs. And a must-see place in Chicago is this giant
jelly bean that's kind of silver mirror shaped. Basically has a huge reflection of everyone that
goes there. And it's actually quite nice. And it makes for a great selfie shot. So be sure to check
that out. It's definitely one of those must-see places whenever you visit Chicago. And if you have
extra time, you may want to check out the Museum of Illusions. It's also pretty nice there. And
Chicago, of course, is well lit up at night. The buildings look very shiny. So definitely check out
Chicago at night too. And if you go to Willis Tower, you can take an elevator all the way up to the
top and then stand on this glass thing where you can see the whole city. So it's pretty cool.
And there are lots of cool statues all around town like the wings. You can basically stand there
and everyone thinks you're flying around because it looks pretty cool. All right, so that's the end
of the Chicago tour. Up next, we have United Airlines where we'll be flying to Orlando, Florida.
So let's get started on the live demo for that. Let's back out of here and do python raw united.py.
And now so we're going to go to united.com and do the flight search. So we're going to set the
from location to be New York City. And then we're going to set the destination to be Orlando, Florida.
Then we're going to click to do the search. And then you'll see that the data appears right here
and you can see the various prices. And then we're going to scrape that data and put it all here.
So now you can see that we have nonstop flights with various times originating from the New
York area. And then we'll be going to Orlando. And it even tells you the various plans you might
be taking, such as a Boeing 757 200. And then it also has like the flight number details. So that's
good. And then there are various ranges for prices, such as eco basic prices or just the regular
economy prices, which can vary depending on which package you've selected. So let's jump right back
into the presentation. And now we're going to do the quick tour of Orlando. So when you get
to Orlando, you might find this giant golf ball. That is Epcot center inside of Disney world.
And it's quite a famous landmark. You know, it makes great photos if you like go there and take
some photos. It's nice. It does kind of look like a golf ball, even though you can actually go
inside a bit. There's a lot of stuff in there. Yeah, bring the whole family too, because it's
a lot of fun things to do there. And you can even see this giant golf ball all the way from Japan,
because they have a Japan section at Epcot. And you can basically see the big golf ball from all
the various countries, like you'll probably be able to see it from the China section at Epcot,
for sure. And then in addition to that, you'll probably also see it in the England section or
Great Britain section of Epcot. Here you have these popular red telephones that you can find throughout
England, but you don't have to go all the way to England to see those phones. You can see them
right here. So that's a nice little fun thing to do. And if you get tired of watching giant golf
balls, you may be able to find a giant globe at Universal. It's the Universal Globe. And it's just a
great place to be. A lot of fun things to do there. The globe is a bit smaller than the golf ball,
but you know, every the different landmark is, you know, to each their own. And if you get hungry,
you can always check out the minion cafe because there's lots of fancy food there. And of course,
minions will be making your food for you. And if that's not your style, you could also check out
the hard rock cafe, which is another popular food destination there at Universal. So check that out.
There's a lot of fancy surroundings there, like there's like a river running through. And there
appears to be some colosseum next to it, or maybe it's part of it, fancy trees. This kind of look
pretty fancy. And of course, at Universal, you can meet the whole Scooby Doo gang. If that's your
thing, you know, Scooby Doo is going to be there. So you might as well check it out. And of course,
this is the castle at the center of the Magic Kingdom and Disney World. This castle is probably
one of the most famous landmarks in all of Orlando. And it's great for, you know, selfies and all
those photos that you may want to take there. And it even lights up at night. There are all these
like fancy lights that show there. And you might even get to see a fireworks show. And also be
sure to check out the fountain by the castle because it is a magical fountain. So you never know
what you may find. And if you ever get tired of Disney, SeaWorld is not too far away. So you can
go there and check out the views there. And there's a little lighthouse there to show you that you're
there. And there'll be lots of dolphins swimming around SeaWorld. And they'll be doing fancy tricks
like standing on the water on their tail fins. You can even go up to them and see them up close
and in person, you know, because the dolphins are really quite intelligent. And you can even go
swimming with the dolphins as you can see here. And if dolphins aren't your thing, you might also be
interested in the sea lions. And those sea lions are great at putting on a show. That's for sure.
So that's the end of that tour. Up next, we have LL and we'll be flying to Israel.
So let's do that demo here. Back out of that Python rawl.py. And we're going to go in.
It's going to go into the LL website. It's going to set your departure date. So it's going to
modify that. And it's already put in the Boston to Tel Aviv because you can set that right from
the URL. And now it's going to do a search. And if it doesn't find flights on that particular day,
there is a button that appears where you can find more available flights. And you can see here
in this flight calendar, all the various prices from the various days that you may go on your trip.
And I'll find the best price for you with the algorithm that I've implemented. And now all that's
going to be outputted here. So you can see that the lowest price from Boston to Tel Aviv is $1,412
to parting on Sunday, March 30th, 2025. And the return day, Saturday, April 12th, 2025. And you
can see all the various prices that it found and all the other data that it was collecting during
that web scraping. So you can see here that you can use web automation to find you the best price.
So let's jump back into the presentation because now we're going to do a quick tour of Israel.
And whenever I go to Israel, I pretty much dress for the occasion. I might have my American flag on
one side of me and my Israeli flag on the other. And when you get there, there is this western wall
that's a very famous place to be. A lot of people go there to pray at the wall or to leave a note in
the wall. Lots of famous things happening there. And you can get a great view of the western wall
from a top of the building known as Asiatura. We can basically see the wall and the surrounding area
with great clarity. And there's usually a lot of people out the wall as I mentioned before. And
sometimes on special occasions, people go dancing. You can see the guys have formed a little dance
circle here. And meanwhile, the women have their own dance circle going. Everyone's doing their own
thing. And sometimes it gets really crowded there, such as on this day, which is Yom Shaliam,
which translates to Jerusalem Day. It's a big celebration where they celebrate the return of the Jews
coming back to the wall because technically they were displaced for a while and they didn't have
access to the wall. But now they do. So they celebrate that. And usually it's an annual tradition.
And here's me celebrating Jerusalem Day. And if you want to know more about Jerusalem Day, the people
here in this photo from 1967, they're the ones who made it possible. They were paratroopers,
they came in and they reclaimed the wall. And here's just another ashatami at a Jerusalem Day
celebration. And here's another ashatami where a radio talk show host decided to ask me a few
questions from my trip to Israel. And also definitely be sure to check out the food because the food
there is amazing. There's a place called the shuk and there's just all this delicious food there.
And if you get a chance, check out some of the cafes. There's a special dish that I particularly
like called the shak shuka. And it's basically some eggs mixed around in some tomato sauce with some
spicings on it. So it's definitely quite a delicious dish. Very fresh. And sometimes in Jerusalem,
because it's a historic place, there are other historical events that happen, such as on this
situation here where they were opening the U.S. Embassy in Jerusalem after relocating it from
Tel Aviv. And you can see here on the left, this guy here, his name is Ari Fold and he basically
organized that particular event. So that is how the Jerusalem Embassy became the V for the U.S.
And of course, if you have a little extra time and you want to do some learning,
there's a place called a Yashiva. Well, actually, there are lots of Yashivas all around the country
where people can come and do some learning. And generally, the rabbis there have a great story
to tell. So if you show up, you're going to be sure to have a great time learning. And of course,
the weddings are also quite exciting. As you can see here, the guys are dancing on each other's
shoulders. Meanwhile, the women might be off doing their own photo shoot, but note that those are
two entirely different weddings. And the artwork around Jerusalem is quite nice, like all these
umbrellas, you know, everywhere. So definitely, the artwork is very nice there in Jerusalem. And if
you're staying at the King David Hotel, be sure to check out the afternoon tea time because the tea
there is wonderful. And when I go there, I usually visit lots of my friends who are there because I
know a lot of people there. So that's why I try to visit as often as I can. And you also might like
to visit the army base because they do army based tours. But generally, in order to get on an
army based tour, you generally have to be part of some other group that's going there,
such as in this case, where I went with United with Israel. It's a group that came to the army
base. And we basically celebrated Hanukkah while we were there. Quite a great celebration.
And if you like the ocean and you like ancient ruins, there's a place called Ksaria,
which basically combines all those things together. You've got like an ancient Roman theater,
along with like ancient Roman ruins. And you've got the view of the Mediterranean right there.
So it's quite a nice place to visit. And here's an up close view of the theater there that's
at Ksaria. And here in this screenshot is a view of Tel Aviv, which is a very nice coastal city with
lots of things to do. And some of the architecture of the buildings is also quite nice as well. Here's
the view from the beach. And there's also lots of flowers all over Tel Aviv if you're interested in
flowers and gardening and that sort of thing. And if you like to run at night, there is a Tel Aviv
running club that basically does night runs. And that's part of the Adidas Runners Club. So if you
like to wake up in the middle of the night and go running, the Tel Aviv Runners Club might be the
club for you. So that pretty much wraps up the tour of Israel. So definitely be sure to check out
the Selenium Base page on GitHub so that you can learn all about the various features and functionality
and all about web scraping, bypassing captures, doing test automation. It's all here. It's right here
on the GitHub.com slash Selenium Base slash Selenium Base. So to be sure to check it out and I'll
see you all next time.

############################################################

[30/44] VIDEO: Web-Scrapers vs Anti-Scrapers
URL: https://www.youtube.com/watch?v=q71J_DbgU9E
------------------------------
(Source: Original Transcript)
Hello and welcome to the stealthy automation show.
Get ready for some serious hacking.
Today we're going to be talking about web scrapers
versus anti scrapers, and we'll be covering a lot of the tools
you see below here, which include commercial scraping tools,
open source tools on GitHub, as well as lots
of anti scraping tools and captures,
such as the ones you see there.
So back in the old days, the bots looked like bots,
and they were easily detectable.
However, recently, the bots looked a lot like humans,
similar to Battlestar Galactica's human-verse
cylon comparison, where you can't tell the two apart.
But if you have to fight some cylons,
have Lieutenant Kara Thrace, aka Starbucks at your side.
And if you're going to go up against the Borg,
you better have Commander Riker at your side as well.
So a bit about me.
I'm Michael Mintz, and I lead the automation team at IBOS.
And IBOS provides cybersecurity solutions
to companies all around the globe, including the US government.
And I also created the slain-based test automation framework,
which you can find on GitHub.
It's a powerful tool for testing and also
bypassing bot detection.
And recently, I was at the Picon conference
in Pittsburgh, Pennsylvania, which
is a major Python conference around the world.
And it was just huge.
It was packed tons of vendors and major people were there,
Microsoft, Amazon, Google, et cetera.
And even the creator of the Python programming language
was there.
That's Guido Van Rossum.
And I got to meet him, too.
There he is behind me, speaking to someone else there.
And also at Picon was Al Swagart.
He's the creator of Payato Gui, which
is a tool that lets you programmatically
control the mouse and the keyboard.
It's particularly useful in bypassing captures
and it's integrated into my slain-based test automation
framework.
So here's an example of bypassing Cloudflare's challenge
page with slain-based.
You'll do from slain-based import SP.
And then you'll initialize your driver.
You'll set the URL.
And then you'll do sp.activate CDP mode with the URL.
And then you can call sp.gui-clickcapsha to use Payato GUI
to click the capture if it wasn't automatically bypassed
when you load the page.
And here's another example.
So for instance, if the Cloudflare capture
is integrated within websites, you
may need to do additional things.
So here you have Cloudflare directly inside the website
rather than a page that appears before loading the website.
And in that case, you may need to use sp.cdp.gui-click element
with the selector that appears directly
above the shadow root element of the Cloudflare capture.
So there are different types of Cloudflare captures
and there is a different way of bypassing each type.
And slain-based has all the examples
for all the various types of captures that there are.
So slain-based was once just a test automation framework,
but it has since evolved into a stealthy test automation
framework.
Engage clock and device message check out.
And at PyCon, I gave a talk about slain-based
at the open spaces sessions.
So there you have it, slain-based deep dive.
And I basically talked about all the various features,
the capture bypass abilities, the two-factor log-in authentication
handling, et cetera.
And there was just a lot of content there.
And I spoke to as many people about slain-based as I could.
And after that, I noticed that slain-based was trending on GitHub.
So perhaps my marketing sales skills for slain-based worked out.
And as you can see here, it was trending
with over 400 stars gathered in that week for the English spoken
language, language Python, and for the week for the date range.
So only Microsoft was beating me out,
but it's really hard to take on Microsoft.
They're pretty big.
So let's talk about anti-bots, anti-scrapers, and captures.
So here are the various tools that people could use
in order to prevent bots from web scraping their websites, et
cetera.
So you have physical captures that you may need to click,
such as hcapsha, recapsha, and cladflair.
So Google makes recapsha.
And cladflair's capture is called the turn style.
And these are various captures, but they're not all created equal.
So for instance, if you can't get past the hcapsha,
it's going to make you click on images.
And this is really hard for regular automation to do,
unless you've integrated some type of AI to handle the clicking.
And in this scenario here, Google's recapsha does something
similar.
It detects the bot.
Then it's going to make you click on all the squares that
contain stairs or buses in that example.
So recapsha is pretty good.
And then there's the cladflair turn style, which
is a lot easier to bypass.
You just pretty much have to click it with piata gooey
using a stealthy test automation framework.
And that takes care of that.
So they're also invisible anti-bot services,
such as imperva and capsula, akamai, data dome, perimeter
x, kisada, shape security, and also the invisible Google
recapsha, which is not quite as powerful as the enterprise
Google recapsha.
So there might be different recapshas,
and not all of them are created equal,
some are more powerful than others.
And there's also the protector capsa, which
is an open source capsa system, where all the code
is freely available online.
And people can take it and modify it and add it to their website.
So the protector capsa is quite powerful
in detecting various bots.
For instance, here, if you try to go to a website
using regular Selenium, protectors
going to detect that through various means.
For instance, it might detect the navigator dot web
driver there, or it might detect the CDC variables
that appear inside the Chrome DevTools console.
And these appear whenever using Selenium
to spin up a browser.
So you can see here, it detected window dot CDC,
and also it might detect web driver on its own
within the web browser.
So here's just an example of the protector,
open source capsa system blocking a Selenium bot.
Now, there are several different open source still frameworks
with more than 1,000 GitHub stars.
So I'm going to cover a few of those right now,
or 10 of those, actually.
So you can see the list here.
And I'm just going to go one by one.
So we've got undetected Chrome driver,
which is a very popular tool.
It's got over 11,000 GitHub stars.
And it was basically a huge popular tool
that many people were using.
However, the creator of undetected Chrome driver
recently created the successor, no driver, which
uses CDP, the Chrome DevTools protocol,
to do even more.
So for instance, it provides a blazing fast framework
for web automation, web scraping, bots,
and other ways of basically preventing
captures and antibody systems from detecting you.
So that's pretty powerful.
That's got 2.6,000 GitHub stars.
There's also a sending base, which is the framework I created.
Python APIs for web automation, testing,
and bypassing bot detection.
That's got 11.2,000 GitHub stars.
Then there's patch right, the undetected version
of the playwright testing and automation library.
And specifically for people who are using playwright
for automation, this can patch it so that it appears more
stealthy.
And this one has 1,000 GitHub stars.
There's also puppeteer real browser, which
is designed to bypass bot detecting
captures such as CloudPlayer, that acts as a real browser,
and can be managed with puppeteer.
This has 1.3,000 GitHub stars.
There is scrapling, an undetectable, powerful,
hyperformance Python library to make web scraping easy
and effortless as it should be.
This has 5.4,000 GitHub stars.
There's PIDAL, which is a library for automating
Chromium-based browsers without a web driver,
offering realistic interactions.
And that has 4.7,000 GitHub stars.
There's Bodisaurus, the all-in-one framework
to build undefeatable scrapers with 2,000 GitHub stars.
There's Cloud Scraper, a Python module
to bypass CloudPlayer's anti-bot page with 5.1,000 GitHub stars.
And there's RISION page, a Python-based web automation
tool, powerful and elegant.
And even though it doesn't say it in the description,
it actually has some powerful stealth capabilities.
And this one is very popular with over 10,000 GitHub stars.
And also, the instruction manual for RISION page
is in Chinese.
So as you can see, there are lots of open-source stealth
frameworks to choose from.
Let's also talk about some commercial frameworks for stealth,
such as BrightData and Xenros.
So both of them are quite popular.
However, BrightData has over 20,000 customers worldwide,
whereas Xenros only has about 2,000 plus customers worldwide.
You can see that there are lots of major organizations
using both.
For instance, with BrightData, you have companies like Deloitte.
You have Mozilla.
You have NBC Universal.
You have Pfizer, et cetera.
So lots of major companies.
And with Xenros, you also have some major companies
like Microsoft, et cetera, IBM.
So perhaps Microsoft chose Xenros not because it's better,
but for other reasons.
So for instance, BrightData recently donated a lot of money
to the Selenium organization becoming a Selenium level sponsor.
Now, for those of you who don't know,
Selenium and Playwright are competitors
in the automation space.
And so Microsoft's Playwright is competing with Selenium
and they're battling it out for the market share
of web automation systems.
So there's that going on.
And also interestingly, a bunch of companies
sued BrightData because BrightData was very effective
in web scraping data from them.
So for instance, here, it talks about meta slash Facebook
suing BrightData over the right to collect data.
And at the end of this, the ruling was that web scraping
is 100% legal in the eyes of the courts
as long as it only involves public data and not private data
and that the web scraping isn't done
while logged into the website.
So this was a huge victory for BrightData.
And it wasn't just meta slash Facebook suing BrightData.
It was also x slash Twitter that was also suing BrightData
over their powerful scraping capabilities.
So it's just amazing that these two mega giants,
meta and Twitter, et cetera, basically losing
to BrightData in the lawsuit.
And there are only a few explanations
for how BrightData was able to beat out
those lawsuits against them.
And those include having possibly the best legal team
in the world.
Actually, this is Karen Reed's defense team.
So not actually BrightData's lawyers,
but it's for the screenshot.
And the other reason people might think
that BrightData won those lawsuits
is because the Mossad may have been involved.
Now, BrightData isn't an Israeli company.
And the Mossad basically does its job, which
is protecting Israeli interests and Israeli companies
from foreign invaders.
So in the case where meta and Twitter
wanted to sue BrightData, the Mossad
may have stepped in to help out BrightData in that situation,
or it might have been the legal team doing all the work.
Speaking of the Mossad, there is a rumor
that I once had a party with Mossad agents,
but actually it was a party with the IDF.
So this photo is from the time where
I proposed to my girlfriend, who's now my wife.
And this was on top of a roof in Jerusalem.
And the IDF basically joined in for a nice photo op.
Now the Mossad and the IDF are different.
The IDF is the Israel, the fence forces.
Raz, the Mossad is an intelligence agency.
And on the topic of the IDF,
I didn't once get to visit one of their army bases in Israel.
And I believe this event was for a pizza party
that was happening on Hanukkah.
So I know it's been a pretty chaotic situation
and Israel lately.
So I hope all my friends are safe, pretty dangerous,
the whole war with Iran.
So hopefully everyone's doing OK.
Lots of friends in Jerusalem, as well
as family in Netanyah and other parts of Israel.
Oh, if anyone ever goes to Netanyah,
I hear they have a highly energetic football slash soccer
team there.
So let's get back to the presentation from that diversion.
So bright data is another cool option for web scraping.
And I particularly like them because they blog about me.
So for instance, they wrote a few posts
how to use proxies with Selenium base.
And they wrote the guide to web scraping
with Selenium base in 2025.
And they just have a bunch of various powerful tools
that people can use.
They've got scrapers, they've got capture bypass tools, various APIs
for web crawling, et cetera.
They have different residential proxies there
that you can set up so that if you're
trying to automate from a proxy server,
you can hide your IP address to make it a residential IP address
so that it's not detectable via anti-bought systems
because if you're running directly from a cloud server
such as AWS, et cetera, then your IP address
is going to be known to come from somewhere like AWS.
And therefore, you could get blocked for that.
And there's also Zenrose, as I mentioned earlier.
And they also blog about me that a few articles had a bypass
that there was Selenium.
And then inside that article, they talked about Selenium base.
And then they also had web scraping with Selenium base
in Python in 2025.
And also how to use proxies with Selenium base in Python.
So they also have a bunch of comparable tools
similar to bright data.
They've got scraper APIs, they've got residential proxies,
they've got capture bypass tools, et cetera.
So those are two ideas for commercial web scraping products
if people are interested.
However, bright data appears to be considerably more popular
than Zenrose.
So that's web scrapers versus anti scrapers.
And Selenium base is the framework that I created
that you can find on GitHub on one browser automation.
There's web crawling, testing, scraping stealth,
and lots of powerful tools.
There are various modes for stealth
such as UC mode and CDP mode.
There's also a recorder so that you can generate your scripts
instantly.
And one of the things that makes Selenium base
stand apart from the other competitors in the open source space
is the sheer number of examples.
So now we've reached the live demo portion
of this presentation.
And we've got a lot of exciting live demos planned for you.
All right, so we're going to be running examples
from the Selenium base examples CDP mode folder.
If you clone the Selenium base repo,
you'll have access to that.
And then you'll find lots of various examples
that you can run directly from there.
Let's do a simple one.
Python rawgetlab.py, where we're going to be bypassing
a cloud flare page that appears when you first
try to go to the GitLab site.
So you can see here you've gotten through.
And then we're going to run some fancy JavaScript
from Selenium base to say that Selenium base wasn't detected.
So if you want to see what the code for that looks like,
we can do S-base print rawgetlab.py.
And then dash and add the line numbers.
You can see here that once we set the URL,
we activated CDP mode.
And then we did UC GUI click capture.
Now note that this is using UC equals true,
which is the undetected Chrome driver mode.
It's one of the ways of achieving stealth with Selenium base.
And in combination with CDP mode,
you get some pretty advanced stealth capabilities.
And then there are also lots of other Selenium base methods
where you can do advanced things,
such as asserting elements, highlighting elements, et cetera.
So let's run another example, Python rawplanetmc.py.
Another example of a page where the cloud flare capture
appears directly on the site itself.
The capture was bypassed automatically.
And it was just that easy.
Let's do S-base print rawplanetmc.py.
And then add dash and to see the line numbers.
You can see that all that we were doing here
was activating CDP mode and then calling sb.cdp.gui click element
in case it wasn't bypassed automatically.
Now, when you're using sb.cdp.gui click element for the selector,
make sure you're using the element that appears directly
above the shadow root of the cloud flare turn style.
This will allow you to click inside the shadow root,
which isn't normally visible with JavaScript.
All right, so now that we've covered that,
let's run another example.
Let's do Python rawwomart.py.
And we're going to basically scrape some prices
of something from Walmart.
So let's do a search for the settlers of Catan board game.
You can see that it's going in and it's found
several different items and it's going to go through
and scrape all that and then output it to the console.
So you can see here in this display,
Walmart search for settlers of Catan board game
and then all these different games
that it found with the prices there.
So that's an example of scraping Walmart.
Let's take a look at what that looks like.
Espace, print rawwomart.py, dash n.
You can see it's quite a bit more advanced
because there's more actions that you need to take.
You're clicking on various elements,
you're typing text in order to do a search
or moving some advertising.
And then we're looping through the output
that it finds, say I can scrape the names
of the items as well as the prices.
So there's a lot going on there
and because slanting base has so many different examples,
there's a lot here to help you get started
so that you don't have to create all your scripts
from scratch.
So that was the Walmart example.
Let's do another one where we're going
to web scrape hotel prices.
So let's do Python rawbestwestern.py.
We're going to go in and we're going to do a search.
So let's say we're going to set our destination to be
Palm Springs, California, USA.
And then we're going to use the default checking dates
and that's going to go in, do the search,
find all the hotels, find the various prices,
it's going to web scrape all that data
and then output that to the console once it finds it all.
So you can see here, bestwestern hotels
and Palm Springs, California, USA for the dates here.
And then you can see all the various hotels with the prices.
So this is another slanting base example
of bypassing some pretty advanced bot detection systems.
You can see here that there's just lots of different examples
you can choose from.
You can even change your fingerprint
such as changing your timezone data and geolocation.
So let's do Python rawtimezonesp.py
and example where we're going to change our timezone and geolocation.
So now we're on India standard time near luck now India.
And now in the next part, we're going to go to Japan standard time
in Japan and the geolocation has changed again.
Let's take a look at what that script looks like.
So do space, print, raw, timezonesp.py, dash n.
You can see here that we're activating CDP mode
and then once we set the URL, we're going to set the timezone here.
So here it's Asia slash Kolkata
and then we're setting the geolocation here
and then we're moving some advertising that might appear on that page.
And then we're going to do the same thing again, but we're going to go to Japan.
So we're going to set the timezone to be Asia slash Tokyo
and then we're setting another geolocation for that.
So that's just an example of changing your fingerprint
so that you can be stealthy when automating.
So up next, we're going to do some web scraping of Nike shoe prices.
So we're going to run Python rawNike.py.
It's going to go to the Nike website
and then it's going to do a query for Nike Air Force One shoes.
The data will be displayed on the screen
and then slimming base will scrape that data
and then output it to the console.
As you can see here, found results for Nike Air Force One.
You can see the various shoes with the prices.
Let's take a look at the script for that.
So let's do S-base print rawNike.py
and then dash in for the line numbers.
You can see here, fairly simple.
We activate CDP mode on the Nike website
and then we click a few things.
We type some text
and then we loop through the results that it found
and output that to the screen.
So that is that example.
This time, let's do Python rawIndeed.py
an example of searching a job search website
that has Cloudflare protections.
You can see we bypassed one Cloudflare capture there
and then after we go do a search on the Indeed page,
it's going to throw a second Cloudflare turn style capture
and then Pyrogue through Selenium Base is going to come in,
click on that and then it's going to web scrape the data there.
That's an example of bypassing multiple Cloudflare captures
all at once.
So that is that example.
If you want to see what that looks like,
we can do S-base print rawIndeed.py
and let's just do that again with the line numbers.
You can see that we're activating CDP mode.
We're going to click the capture
and then we're going to click a few buttons,
type in some text,
and then we're going to go click the capture again
because another one appears at a later point in the test,
and then we're going to web scrape the data
and print it out so that it displays on the console.
So that's just an example, a more advanced one,
where we're gathering data from a website
while bypassing captures.
You can see that there is plenty of different examples
here that you can run.
There's a lot to cover, lots to learn,
so definitely try these out.
There's also a lot of other Selenium Base YouTube videos out there
where we're pretty much running most of the examples that you see here.
So if there's anything here that you want to see run,
you can watch the YouTube video,
or you can just try running it yourself
because all the examples here should be up to date.
Let's try one last one here.
Let's do Python raw chatgbt.py
because that's an interesting one.
So we're going to then go to the website and do a query,
compare playwright to Selenium Base in under 178 words,
and chatgbt is going to display the response there,
and then Selenium Base is going to copy that response
to the console output.
So you can see here, if we scroll up,
compare playwright to Selenium Base in under 178 words,
and we have the response from chatgbt.
I won't read the whole thing, but here we go.
Playwright and Selenium Base are both end-to-end testing frameworks,
but they differ in design, philosophy, and capabilities.
So that's an example of web scraping chatgbt.
And all these examples that you see here can also be run
from GitHub actions, and those examples are also
in various YouTube videos that I've also already posted.
So that's basically it for today.
I hope you had a lot of fun learning about the various automation
frameworks that are out there for web scraping,
as well as some commercial possibilities,
and the tools that are used to stop automation in their tracks.
It's a big battle out there, but it's a lot of fun,
and hey, web scraping is legal,
as long as you're web scraping public data
while you're not logged into a website,
we've got bright data to thank for that.
So that means scrape away, and have a great time.
So we'll see you all later, everyone.

############################################################

[31/44] VIDEO: How to bypass paywalls
URL: https://www.youtube.com/watch?v=qQ6nn9pSiiY
------------------------------
(Source: Original Transcript)
Don't you just hate it when you go to a website looking for some information and then all of a sudden they throw a paywall right at you
I mean come on
Well, I don't like it any more than you do. All I want to do is find out some information about this cool hike
Thundering Brookfalls in Vermont because who doesn't like being outside enjoying nature?
Oh wow, it's warm and
The paywall just keeps throwing me out. I can't scroll down to get the information
So how does one go about getting around those paywalls? Well, that's easy
You just right click and inspect in the web browser then click on the gear icon below
Then scroll down and near there you'll find disabled JavaScript
So click that and then you can scroll freely without getting hit by a JavaScript paywall that comes up
So that's one way of bypassing a paywall and now I can get all this information about this hike
Another way of getting at that information is through a website called web.archive.org
Which basically saves a copy of many websites to its database and then you can access that information there very easily
And this is also another way of getting around paywalls for other websites as well such as here where you may have stumbled upon
exclusive content and
Web.archive.org will get that information for you because it will have saved a copy of that
Website without you having to go through the paywall
So that basically is an example of getting at the information that you want and that's how to bypass paywalls
Which is only part one of this presentation
Part two of course is how to bypass paywalls for web scraping
So we're going to get into more exciting stuff. You have reached the stealthy automation show
So we're going to be using an automation framework called Seleniumase to do some web scraping of the altrails.com website
Which has the paywall?
So here's what the script is going to look like we're going to do from Seleniumase and port SP
Then we're going to initialize it and then we're going to set the URL to be altrails and then we're going to activate
CDP mode which is a stealthy mode of Seleniumase which lets you bypass bot detection
Then there might be a banner that you click to close and then we're going to do a search for a thundering
Brookfalls which is the trail I'm interested in finding out about and then we're going to type that in and then click to search
And then we're going to go through and then we're going to print the description that's there
We're going to scroll to the bottom of the page to trigger the full content loading and then we're going to scroll back up to the top
Then once all that is done we're going to take a screenshot and then save the page source
So that all this data is there
Demonstrating that we can web scrape the data get a screenshot and get the page source
So let's get started with that
We're going to go to the CDP mode folder within Seleniumase
So just go to Seleniumase examples CDP mode then you can do Python rawtrails.py and then it's going to go to the website
You'll see here
Alltrails.com. We're going to search for a thundering Brookfalls trail
And then it's going to go to the site. It's going to then scroll down
You'll see that the paywall comes up, but we're going to hide it
But we need to scroll to the bottom so that all the data loads and now we've gathered the data here so you can see here
We've got the description of thundering Brookfalls
You got to check out this half mile you know long trail near Killington Vermont. It's a popular area
We're going to just grab the basic data the summary of it. You know highlights include beautiful waterfalls etc
And then we're going to grab the reviews such as here short hike and good condition
And then we're going to save a few files such as a PNG image
Rub the website and we're also going to save the HTML file
So if we go into the file explorer we can go in here for the PNG
It's going to open that up. Let's expand on that and then increase the size so that we can see that we've got the whole website
So here we go thundering Brookfalls
You can see here. We've got screenshots. We've got the description there
What trailgoers are saying etc just lots of data and
You just scroll down you can see you know top trails nearby etc and in addition to that there is also
We go back up to the downloaded files folder. There's going to be a thundering Brookfalls HTML file
So you can see here at loaded
Let's just refresh that again
And we can scroll and
Grab the data here as well
So there you can see we're bypassing the paywall because we were able to load the website
From a different origin so the regular JavaScript that's there won't load
So that's probably one of the ways that some websites like web.archive.org
Were able to grab a whole website and drop it on their site
Without having to trigger a paywall if a user looks at that later
So that is how to do web scraping when there's a paywall and of course we already showed you how to bypass it from the regular means
For instance if you went to the website and then you clicked to disable JavaScript
Then you can also scroll down and avoid the paywalls that are there. So yeah, that's web scraping 101 for paywalls
The example I showed in this presentation uses a Python automation framework called Selenium Base
Which has a stealthy mode called CDP mode which lets you bypass bot detection and even bypass
Captures on websites. So of course, this might be the tool that you want to use to get around bot detection
Because then websites can't detect you. It's 2025 and most websites still can't tell the difference between humans and non-humans
And in case anyone's wondering my wife and I did check out Thundering Brook Falls in Killington, Vermont
It's quite a nice area. You know, you got the waterfall. It's fantastic
And if you're gonna be there, you might as well just hike Killington mountain while you're there because that's probably the main attraction
As a bonus, the lines are much shorter than in Disney World. If you go there in the winter
There's gonna be a lot of skiing for sure. So that concludes this automation show
Check out some of my other YouTube videos and the Selenium Base GitHub page for more awesome
Capture bypass abilities and I'll see you all next time

############################################################

[32/44] VIDEO: Chrome removes Manifest V2 extensions. Here's how to keep ad-blockers working.
URL: https://www.youtube.com/watch?v=-1IeSgHDX3o
------------------------------
(Source: Original Transcript)
Manifest V2 extensions are finally going away. Is this really the end of ad blockers? Find out on the hacker show.
Get ready for some serious hacking. So Manifest V2 is the old standard for Chrome extensions
that's being replaced by the newer Manifest V3 which has improved security, privacy, and performance.
So what does this mean for users? Well, they might now start to experience issues with their
extensions that are still using Manifest V2 and many ad blockers such as U-block origin
are going to be affected by this change. And U-block origin is used by tens of millions of people.
For instance, Chrome has over 29 million users using U-block origin. There's also many users on
Firefox as well and other browsers. And the latest version of Chrome, which is 138,
turned off Manifest V2 extensions such as U-block origin for all users. And the impact
was felt worldwide. For instance, on hacker news, you may have noticed various posts such as U-block
origin on Chrome is finally gone. The latest version of Chrome, 138, removes Manifest V2
and all extensions that rely on it. And this is what you might have seen if you're using U-block
origin. This extension was turned off because it is no longer supported. And here you can see it was
deactivated and people couldn't switch it back on. So most people took this news update surprisingly
well. I'm just kidding. They're all freaking out on the internet. For instance, on Reddit,
you have all these different posts such as U-block origin fully disabled on Chrome now with a lot of
upvotes. And what happened, U-block origin, or U-block origin has been permanently disabled for
Chrome, etc. So just lots of different posts where people wanted to rant about what was going on.
And Chrome 138 is the last version to fully support Manifest V2 extensions. And you can see here
Chrome 139 is going stable on Tuesday, August 5th, 2025. And on that day, the stable release day,
that's when Chrome will auto update for all users. And then people will have Chrome 139,
which will be unable to use Manifest V2 extensions at all. Now if you noticed in fine print here,
there is an enterprise policy that basically allows the temporary continuation of Manifest V2
extensions on Chrome 138. But that is going to be removed in Chrome 139. So if people still need to
use Manifest V2 extensions until that August 5th, 2025 date, there is a way to do it. And that is via
the extension Manifest V2 availability, which you can see here. And that's good through Chrome 138.
And there are instructions on how to use that on Reddit. So for instance, here if you follow the
instructions for what's currently the best way to force re-enable U-block origin in Chrome,
here's what you can do. You can go to the Chrome flags page, search for a loud legacy extension
Manifest versions, enable it, relaunch the browser, download the latest zip from the U-block GitHub page,
and then you can extract it to a folder. And then in the extensions tab in Chrome,
you can load an unpacked extension. Here's how that might look. So here is the Chrome flags page.
You can see under experiments, allow legacy extension Manifest versions. Make sure you click to
enable that. Then go to github.com slash corehills slash you blocked slash releases. And then
download the Chromium zip file, which contains the ad blocker. Then after you've unzipped that to
a folder, make sure you go to the Chrome colon slash slash extensions page and then click to turn on
developer mode. That will be in the upper right corner here. And then you can go to load unpacked,
which basically then has you select a folder where you've unzipped the extension. And then once you've
loaded it, then you have U-block origin development build. And right now that's 1.65.1.0. And it's
essentially the same as the previous version. But now you can see you might have two different
versions of U-block origin installed at this point, which would be the old version that was turned
off automatically by Chrome. And then the new one that you just added through the enterprise policy
that basically continues U-block origin up until Chrome 139. So that is the workaround for now.
And note that the error that you see there is because manifest version 2 is deprecated and support will
be removed in 2025, which is pretty much happening now. And of course, remember that stable release date,
that's the important date to keep in mind to stay August 5th 2025. That's the end-all date where
you have no choice but to auto update to the newest version of Chrome. And then you won't be able to
use any manifest V2 extensions anymore. So here you can see this will go away next month according
to Reddit. Yep, version 139 releasing August 5th will remove all workarounds for manifest V2
extensions. So keep that in mind. So what if you still need manifest V2 extensions after August
5th 2025? Or what if you need to run test automation on sites containing ads and you need to click
on everything, but you don't want to accidentally click on any of the ads, you know, to prevent the
click fraud because that's pretty bad. Well, you've got a few options available to you if that is the case.
Option 1, there's a thing called Chrome Protesting, which is designed to solve these problems.
Chrome Protesting is a dedicated flavor of Chrome targeting the testing use case. And it doesn't
have auto update, which means that once you install a specific version of Chrome Protesting,
such as Chrome Protesting 136, it's not going to update to a newer version that may remove features
such as the ability to use manifest V2 extensions. And if you're wondering where to get
Chrome Protesting binaries, that's pretty easy. The Chrome for Developers page has a solution for you.
The easiest way to download Chrome for testing binaries for your platform is by using the
command line utility here available via NPM. So here are some examples, for instance, NPX,
puppeteer slash browsers install Chrome stable, or you can use those command line utilities
in order to get an earlier version of Chrome. And I would recommend run 36 because then you can
avoid some other issues that are there. So where do you get Chrome for testing? Well, if you go to
google chromelabs.github.io slash Chrome-4-testing, there is a Chrome for Testing Availability section,
which shows you the stable beta dev and canary channels. And there's also a link to the JSON API
endpoints so that you can also download earlier versions of Chrome for testing. So if you go to there,
that'll take you to the GitHub page for that Chrome for Testing Availability, where there's going
to be several API endpoints. And there's also going to be several supported binaries and platforms
for this. So there's Chrome for Testing, Chrome Driver, and Chromeheadless Shell. Now Chromeheadless
Shell is basically a special version of Chrome for testing that you can't see because it's running
headlessly, and this might be good for test automation because it might speed things up because
it doesn't have the additional overhead of having to spin up a regular browser that you see.
So there's also a bunch of supported platforms for that. There's Linux 64, Mac ARM 64,
Mac X64, Win32, and Win64. So tons of different supported platforms that you can use. And there
are also additional API endpoints that you can use to figure out what the latest version is at a
specific point. So note that if you expand the JSON API endpoints page, you'll see at the very
bottom there is a latest versions per milestone with downloads.json. If you go into that, you're going
to find the specifics such as the URLs where these binaries live. So for instance, in the case
that you're getting Chrome for Testing 136 on, say, Mac X64, you will have the URL here,
hdps, colon slash slash storage.googleapis.com slash Chrome for Testing public. And then the version
number and then Mac-X64, although you're probably at Mac-Arm64 by now if you're using like an M1,
M2, M3, Mac, et cetera, or if you're running on Linux, there's a version for that. Windows has
its own section. So here's where you'd get the links for the binaries for Chrome for Testing
in order to get earlier versions. Google supplies those freely. And the reason I mentioned before
going back to Chrome 136 or Chrome for Testing 136 is that the load extension flag is still there
because that was removed in newer versions of Chrome. And that basically allowed you
to load an extension as you spin up your browser for automated testing. So that can be convened
if you're, say, running a manifest V2 extension right from your automated tests.
Here you can see that there is a commit, remove dash, dash, load, dash, extension, switch,
on Chrome builds. So that was already removed and that was done in April 2025. And that's why
Chrome 136 is the version you probably want if you're going to downgrade to an earlier version of
Chrome for manifest V2 compatibility. So option two, you can migrate to manifest V3 and that is the
latest, greatest standard for Chrome extensions. And there's a whole set of checklist items on
the developer.chrome.com page. And then if you go to the docs, extensions, develop migrate section,
you have all these things that you need to know if you're trying to migrate your old manifest V2
extension onto the newer manifest V3. So for instance, you would update the manifest.json file to be
specific to V3, you'd migrate to a service worker, you'd update your API calls, etc. All these
different items of the checklist that you can go through to make sure that your old manifest V2
extension is working properly when you migrate it to manifest V3. If you go to the GitHub page,
Google Chrome slash Chrome extensions samples, there's tons of different examples that are already
using manifest V3. And this can help speed up the process of upgrading your extension to manifest V3
because you might be able to find an example that already does what you're looking for.
And if you're trying to build an ad blocker, you may want to familiarize yourself with this
chrome dot declarative net request. Now this is the API used to block or modify network requests
by specifying declarative rules. This lets extensions modify network requests
without intercepting them and viewing their content thus providing more privacy.
This is the key to building an ad blocker. And after I read that, I followed the instructions
and all of a sudden I had a simple ad blocker using manifest V3 with fewer than 40 lines of code
handling all the basics of ad blocking. So if you go in, you would set your manifest version to
three, you'd give it a name such as simple ad blocker, you'd set the version you want,
and then make sure in permissions you set declarative net request. And then under the declarative net
request section, you would then go to rule resources and then you would set your ID, you'd set
enabled to be true, and then you'd set your path to be say rules dot json, and then you'd have
a rules dot json file where then you set the ID priority and then the action to type block.
And then you could set the condition and the URL filter to have say URL double click dot net.
And that would make it so that any double click dot net URLs on a certain page would not load.
And another common domain that you'd want to block for blocking ads would be Google ad services.com
and it would follow the same format that used for the double click dot net. You just set a different
ID. So for instance ID 2, you could also set priority 1, action type block, set your condition,
URL filter, and then that domain, and then all of a sudden you've got a working ad blocker with
fewer than 40 lines of code. And you can see here as we were testing it on w3schools.com slash
jess slash default when we're going to JavaScript tutorial, you can see that the extension has loaded
simple ad blocker and all this white space you see here is the ads that were blocked via this ad blocker
because normally there would be advertisements there, but now they're not there because the ad blocker
blocked them. And if you go to the chrome colon slash slash extensions tab for that ad blocker,
you'll see that it is really small size less than one megabyte, probably making it one of the
smallest ad blockers in the whole world. And if you look down, you can see in permissions block
content on any page and the site access shows this extension has no additional site access,
which means that there's a better privacy. You can still block content on any page
and it's like minimal size. So all of a sudden there, you've got a working ad blocker with very
few lines of code. If you're interested in downloading your own copy of the simple ad blocker,
you can get it from the slenium base get up page. Just go to github.com slash slenium base slash
slenium base. And then once you scroll down, you'll see the folders and there should be a slenium
base folder in there. So if you click on that, you'll see a few more folders inside there, scroll
down again. And then you should find the extensions folder. If you go to there, you'll find all the
slenium base extensions, which includes adblock.zip, which contains the simple ad blocker that I
demoed for you. So if you clone the repo and then extract the zip file to its own folder ad block,
then you'll find the manifest.json file there and the rules.json file there. And if you go
inside those, you'll see that the code in there should be exactly the same as what I already showed
you. And it's less than 40 lines of code. So it's pretty easy to get adblocking in manifest v3.
So option three, you can see what else is out there that uses manifest v3. So for instance,
if you went to reddit.com, you might find that someone was recommending U block origin light,
which is built for manifest v3. Now some people might say that it is a bad, inferior alternative,
but then other people might say, OMG, it works. Thanks so much. So hey, you never know. Sometimes people
judge an extension before actually trying it out. So you never know what's out there or how good
something is unless you try it out and find out for yourself. Option four is you can switch to edge
because apparently that still works with manifest v2 extensions. You can see here U block origin
is enabled on the latest version of edge. So maybe they're not transitioning off that yet.
Or you can try other browsers. For instance, on Firefox, there's also U block origin
and it's enabled on the latest version. So maybe it's working there too. That's a possibility.
And on reddit, there are a lot of people complaining that manifest v2 didn't work on Chrome. So
they're maybe trying to switch to Firefox or something else. Or maybe they're just saying that
and not actually switching to Firefox because Chrome is like a million times better. It's got all
this flexibility and stuff that you can do. People might just be like rage saying they're switching
even though they're not actually intending to switch. But note that 9 out of 10, Microsoft
employees recommend edge. And that's because the other 1 out of 10 get nominated for the next round
of playoffs. So there you have it. Lots of options to choose from. But be sure to decide by August 5th
2025 because that's when Chrome 139 has its stable release and that's when manifest v2 extensions
will be switched off for good even if you're using the enterprise policy to keep them on a little
longer. Funeral services for manifest v2 extensions will be held across the street from the cemetery
where Google Glass, Google Wave, and Google Plus are buried. Long live manifest v3 extensions.
So some people think that talking about ad blockers is a taboo subject maybe because they can
impact profits from advertising. And if ad blockers were legal, then they'd be removed from
the extension section of the web store. You can see here Chrome Web Store. You block origin light
is there, which means Google is okay with having ad blockers there. The original U block origin
was removed because it didn't support the newer manifest v3 extension system. You can see here
this extension is no longer available because it doesn't follow best practices for Chrome extensions.
So there you have it. If you don't follow the rules or the best practices, then your extension
is out of there. So on the topic of legality, some people thought that my previous YouTube video
on bypassing paywalls was going to get banned. In those specific cases, the websites had already
made the data public to search engines, but attempted to make the data private to the general
visitors via JavaScript. Now in those cases, the sites with the paywalls had already made the
data public to search engines, but attempted to make the same data private to general visitors via
JavaScript. And that's not much of a paywall because web browsers allow users to disable JavaScript
easily just by clicking a checkbox in the dev tools debugger. There you have it, the debugger.
Click disable JavaScript. All of a sudden, any paywall that's activated when you scroll a page
won't trigger because JavaScript is disabled. So very simple loophole for those types of cases.
So therefore, sites should assume that if search engines can see their data, then they should
expect that general users can find that same data too. So at the beginning of this presentation,
I may have skipped the part where I introduced myself.
I'm Michael Mints, and I do cyber security, automation, and a bunch of things with Python
and JavaScript. I also created the slinning-based automation framework, which has over 10,000
stars on GitHub. You could say that I'm a bit of an automation superhero.
When I'm not in my computer, there are several places where you might be able to find me,
such as on the jumbo tron at sporting events. Or maybe in the season ticket holder section
of a soccer slash football game to witness the greatest comeback in major league soccer of the
last 20 years. That was New England Revolution's greatest comeback in club history, which occurred
on Saturday, June 28, 2025, when they rallied from a three-row deficit to draw three-three against
the Colorado Rapids. What a game. Even movies can't perfectly mimic that same level of energy and
excitement from scoring the tying goal in a soccer match. But some come close.
On the topic of Google and me, here's a fun fact. So I met Google co-founder Sergei Brin
before Google even existed, and that's because my parents went to college with Sergei Brin's parents.
So here's my parents here. Here's Sergei Brin's parents here. They had all went to Moscow State
University together, graduated together, and because of the anti-Semitism in the Soviet Union back then,
they decided to leave the country together. So this is back in 1979, and they left, and then they
came over to the United States where they spent summer vacations on Cape Cod together because they were
friends. Here's me and Sergei Brin and my sister, Sergei and my sister. So they were around 13
years old, around the same age, whereas I was three years old. This was like 1986. The four photos
my sister, Sergei Brin again, me, Sergei, my sister, etc. So it was close family. My mom made a lot
of phone calls to Sergei Brin's mom because they were close friends. They talked sadly,
Sergei Brin's mom, Eugenia, passed away of Parkinson's late last year. So I guess, you know, bad things
happen, but they were pretty much really close friends up until then, let's see, but it's not the
first time that my family had to move from one country to another. So pre-World War II, my mom's
parents were living by Kiev, Ukraine, and they decided to get the heck out of there in order to go to
Moscow because they sensed the imminent danger that was approaching, and it's a good thing they
sensed the danger because in World War II, Germany invaded Ukraine as part of Operation Barbarossa.
The German invasion of the Soviet Union, codenamed Barbarossa, began on June 22, 1941.
There was a massive ground in aerosol. Over 3.5 million German and other Axis troops
launched an attack along a 1,800 mile front. And once they conquered it, really bad things
happened because they killed off lots of Jews as part of the Holocaust, you know, over a million
Jews in that area died. It was pretty grim. Outside of Kiev, there was a ravine called Bobby R,
where a lot of Jews were tricked to going there, and then once they got there, they were murdered by
the Nazis and Ukrainian collaborators that basically got them there. So yeah, that was a pretty
grim, really bad event, and just maskers happened all over Ukraine during the Holocaust because
the Germans were there, and they didn't like the Jews. So bad things happened, although if any
Jews had managed to escape Ukraine before World War II, or even before World War I in this screenshot
here, then they might have had a better chance of survival. So my mom's family is Da'an, and there
were some Da'an family members that left pre-World War I, Shmul Da'an and Devora Da'an, who basically
became famous because their son was Moshe Da'an, famous general in the Israeli army, and I think
something like Moshe Da'an's great grandfather was my great-great-great-grandfather, or something
like that. Anyway, there's the Da'an family connection for my mother's side of the family,
so yeah, the Da'an family became quite famous in Israel, and of course I visited Israel a lot,
and even though I was never a general like Moshe Da'an, or even a soldier, I did visit quite a
few IDF people because I was living in Israel in 2010, and then I went back to Israel several times
after that. So in this like top left photo here, that's me proposing to my real friend, who's now my
wife, and you've got the IDF in the background, and then in the bottom left, that's me visiting an
IDF base in Israel, and bottom right, that's just hanging out with some IDF people at some rest stop.
So yeah, essentially, I spent quite a bit of time with the IDF, just not as a soldier. If I was actually
in the Army, they'd probably place me in a very special unit. And even though I never got to
meet with a sitting president, just like Moshe Da'an did with Richard Nixon, my wife and I did get to
meet Tulsi Gabbard, and Tulsi Gabbard is, as many of you know, she's the director of national
intelligence for the United States, and she works for Trump, and here's my wife and I meeting with
her at a house party in New Hampshire, before she became the director of national intelligence,
and even though she was never a president, she did run for president. So there is that similar
connection there. So note that translations of last names may vary slightly when translated into
English from other languages. For instance, Da'an versus Da'an, you know, to go from Ukrainian to
Hebrew to English, or Ukrainian to Russian to English, the immigration service, when they write
down the last name, when they're, you know, translating it to like official card or something,
it might vary slightly even if it's the same last name. Situation kind of happened with my uncle,
got like a slightly alternate spelling of Da'an when he came over with his family
to America, to join my family, that were already there, and you know, my uncle kind of resembles
Emotia Da'an slightly just without the eye patch. There's some similarities there. So that's
just some interesting history related to my family, distant family, and family connections.
Let's get back to the presentation. So long live, manifest V3 extensions, which are the future
of Chrome extensions. And let's hope ad blockers don't go away forever, because some people really
need them to stay focused on whatever activity they're working on. Otherwise, people could get
distracted and then go way off topic, just like you saw a few times during this presentation.
And be sure to check out Slending Based on GitHub, which is the web automation framework that I
created. It has lots of capabilities for testing and even stealth capabilities for bypassing
captures, et cetera. There's lots of powerful tools built within it, such as the recorder,
which lets you generate scripts automatically. And there's just tons of different functionality there
that could be quite useful. And there's a whole section called UC mode and CDP mode for the stealth
capabilities. So that concludes this presentation. Fly safe, automate well, live long and prosper,
and maybe see you on the bridge of the USS Enterprise. See y'all next time.

############################################################

[33/44] VIDEO: Learn how to build your own ad-blocker for Chrome!
URL: https://www.youtube.com/watch?v=5ehqgFjdnGg
------------------------------
(Source: Original Transcript)
Over the next few minutes, I'm going to show you how to build your own ad blocker in
under 40 lines of code, and we'll be using the new manifest v3 format for Chrome extensions.
So this is pretty much all the code that there is, and here's what it looks like before
you block the ads, and here's what it looks like after you block the ads.
So it's actually quite simple.
Let's go into a browser that still has all the advertising still there, and then go
into Chrome, colon slash slash extensions.
You can load an unpacked extension using a folder containing those two files that I showed
you.
So if you open the folder, you'll see that simple ad blocker is there, and now if you
refresh the page, you'll see that the advertising is gone.
And if you click on this tab here, you'll see that simple ad blocker is there, and within
that extension, if you click on details, you'll see that it's really quite small, less
than a megabyte, because it's less than 40 lines of code total, and has the permissions
to block content on any page.
So it's really quite simple in how it works.
So if you want more details, it's using the Chrome dot declarative net request feature.
If you go to developer dot chrome dot com slash docs slash extensions, there's going to
be a reference guide.
This basically lets you block any type of URL instantly.
So here you can see all the functionality and how it works and examples.
And if you want to block more than URLs, for instance, maybe you want to block a certain
type of CSS selector on a website, there is also the declarative content.
So Chrome dot declarative content basically lets you block any type of selector on a page.
So if it's not specific to a website, you can block right on the selector itself.
So for instance, here CSS input type equals password and all that.
So another example here.
So basically declarative net request lets you block URLs, and with declarative content,
you can be more specific and also block specific types of selectors and elements on a webpage.
And this is really all the code that there is, you're going to have two files, you're going
to have a manifest dot JSON file where you set the manifest version, you'll give it a name
such as simple add blocker, give it a version, and then you'll set permissions to declarative
net request and inside the declarative net request, you'll set rule resources, then
you'll set the ID, set enable to true, then a path.
So let's say use rules dot JSON here, then the file is going to be called rules dot JSON.
And again, you'll set the ID priority, action with type block, and then inside the condition
field, you'll set a URL filter and it's going to block double click dot net, which is
a common URL for advertising.
And we're also going to duplicate that, but change the URL so that it also blocks Google
add services dot com, which is another type of URL used for sending people advertisements
on a webpage.
So if those two things blocked, you can block a large number of ads on the internet, it's
quite easy.
If you just take these two files, you can modify it, copy it, basically add your own
URLs that you want to block.
And as I mentioned earlier, if you go to chrome dot declarative content and follow the examples
you have there, you can also block certain types of selectors.
So with that blocked, pretty much you've got no advertising on the page.
So if you go back in here and you go into the extension, so then you could just click
to disable it.
And if you refresh the page, so for instance here, I'm going to refresh it.
And then with the extension disabled, you'll see that advertising starts appearing back
on the page.
Here we go.
So you can see here, advertising is there, but we click to enable that simple add blocker.
And then we refresh the page, the advertising is gone.
And this is all using the simple manifest B3 format.
So here you have all extensions.
And if you have other types of extensions, you can add them here.
For instance, you might have one extension that just blocks types of URLs.
And you could have another extension that blocks specific elements on a page.
And you would just do load unpack to load the extension.
If you go into the folder, you'll see here, let me expand on that.
You're going to have two files, the manifest dot JSON and the rules dot JSON.
That's pretty much it.
So if you're wondering where to basically get a boilerplate adblock.zip, which is what
we used for those two files, you can find that from the slenium base page on GitHub.
So let's go to the slenium base page.
And then if you scroll down, you can click on slenium base.
And then if you scroll down here, you should be able to find extensions.
So click on that, and then you'll find adblock.zip.
If you basically fork the repo or clone the repo, and then go into this folder, and then
unzip adblock.zip into its own directory, then you can load that directory with these
two files.
And I don't think you need this metadata here.
I think that's auto generated from somewhere, but essentially those are the only two files
you need.
So that's the adblock folder.
And then we've loaded it inside Chrome using the load unpack button, and make sure that
you have developer mode enabled for this to work.
So that set, you pretty much have a working ad blocker, and that really is all there is
to it.
And this is all you need for the files.
So essentially a manifest.json file, and a rules.json file, less than 40 lines of code
for this basic boilerplate, but you can easily modify it to do way more.
All right, well, that concludes this tutorial.
Hope you have a great time automating.
I'll see you all later.

############################################################

[34/44] VIDEO: Anti-Bot Defenses Reviewed & Graded
URL: https://www.youtube.com/watch?v=-dHQxHg0cXI
------------------------------
(Source: Original Transcript)
In today's video, Antibot Defenses Reviewed and Graded, you'll find out exactly how and
why some of these services are better than others.
And then you'll understand why major websites, such as LinkedIn, have upgraded their security
to use stronger Antibot services such as Enterprise Recapsha, seen here.
Wow, those websites are protected by Enterprise Recapsha.
The automation is going to have a really hard time bypassing that.
So for the stealthy bot, we'll be using the slanting-based test automation framework
which you can find on GitHub, and it has a special mode called CDP mode, which basically
masks the bot so that appears human and will bypass those Antibot systems that try
to detect it.
So here's an example of bypassing CloudFlare's Challenge page, and this is one of the many
tests that we'll be running today to determine the effectiveness of slanting-based against
various Antibot systems.
You can see here that it was able to bypass CloudFlare detection on the GitLab.com page.
So all these tests that are going to be run today will be run both locally and in GitHub
actions.
This is how the grading system was determined.
So here is an example of these tests running in GitHub actions.
From a special repo, you can find at github.com slash MDMins slash undetected dash testing slash
actions.
And you can see that there are many continuous integration builds that are being run in
order to test the various websites that have the Antibot defense systems.
You may have also noticed an ABC grading system, and each grade has a very specific meaning.
So for instance, if you get an A, that means that the Antibot service can consistently stop
my bot, which is the slanting-based bot.
If you get a B, my bot can usually bypass the Antibot service.
And if you get a C, my bot can consistently bypass the Antibot service.
And to be more clear on those definitions, when I mean consistently, I mean greater
than 99% of the time anywhere.
And when I say usually, such as when you get a B, I mean 99% of the time locally and
not consistently in GitHub actions.
So here you have the grades.
So in the A category, we have HCAPSHA, FunCAPSHA, and Enterprise Google ReCAPSHA, which basically
these three here are very powerful, and I wasn't able to bypass those bot detection systems.
In the B category, we have human slash perimeter X, and we have F5 plus shape, Akamai, and
Datadome.
So my automation was able to bypass those defenses locally, but sometimes there were issues
when running it in GitHub actions.
And in the C category, we have Cloudflare Turnstile, Friendly CAPSHA, Cassada, and Imperva
and Capsula.
And my automation was basically able to bypass those in every single environment, both locally
and running in GitHub actions.
So let's visit GitHub actions so we can take a look at all the data that we've gathered
from these tests.
Here is the MDMinslash undetected testing repo, which is where these specific GitHub actions
scripts have been running.
If you click on the Actions tab, you'll see that it's been running a lot.
Let's take a look at some of these.
So let's jump over to here, where we have a build, CI build one.
And we're going to basically web scrape a few different things.
So for instance, on the Upwork website, they're using some Cloudflare defense systems, and
I was able to bypass that in order to web scrape the various job postings that they
had there.
You can see here, these are all reached and web scraped by Selenium Base, showing that
we're able to bypass the bot detection there.
Let's move on over to a different job where we're able to web scrape data from the Nike
website for shoe prices, as you can see here.
And more of the Upwork web scraping, as seen here, let's move on over to the next one,
where we're going to be web scraping Walmart prices from a certain search that we did.
So we did a Walmart search for sellers of Catan board game, and here are the different
results with the prices that we're found.
Let's jump over here, and I believe we had a CI build where we gathered some data.
So let's take a look at that.
This particular one, we're web scraping chat GPT, and we made a query, compare playwright
to Selenium Base and under 178 words, and then we were able to get the results.
This is all running right from GitHub Actions, it's bypassing any bot detection systems
that they have there, and we're able to get the data that easily.
And here's another one where it ran again, you'll see that the result is slightly different
because it's basically every time you run something against chat GPT, it's going to generate
a new response, even if you have the exact same question that you had before.
So let's take a look at a different round of tests, where we're going to be web scraping
Southwest Airlines. You can see here, we've got the various times that the flights were in,
because I wanted to know flights from Boston to Chicago's MDW Airport. You can see here,
the date, the time, the length of the flight, and the cost. So here, 229 dollars,
like here it's 279, here it's 244, so it's basically able to web scrape all that data.
We have just like several different tests that we're running here, just to prove that we can
web scrape data and bypass those indie bot defense systems. Let's take a look over here.
Here, we're web scraping prices from a search for Hayat Hotels in Anaheim, California.
So you can see here for the date Thursday, July 31st through Friday, August 1st,
one room, one guest. You can see all the various results that we're here, such as Hayat House
at Anaheim Resort Convention Center, $205. Let's see, we've got the Hayat Centric Delfina Santa
Monica for $263, Hayat Regency Newport Beach West, 313. So you can see here, just all this data
was scraped by Selenium Base, and here in another example, we're web scraping the Albertsons website,
which is basically a supermarket. You can see here, we're getting various search results for
avocado smoke salmon, and then here we have smoked salmon bowl with ginger, rice, edamame,
mango, and avocado, etc. Here we have miso, smoked salmon, egg, bell pepper, and avocado wrap.
So essentially, we were able to web scrape all the data there, and these are just lots of different
examples that I'm running in order to demonstrate what can bypass the bot detection when running
something from GitHub Actions. And some of these tests, you can also run locally. So for instance,
let's run the python robbestwestern.py so that we can get some hotel prices through there,
and this time we're going to run it locally instead of in GitHub Actions. So it's going to go in,
it's going to type destinations, such as Palm Springs, California. We'll use the default check
and dates. It's going to then get to the results page, and then it's going to web scrape all that
data, and then it's going to print it out over here. So you can see here, it printed it out. You've
got Best Western Hotels in Palm Springs, California, USA. You've got the various dates that you wanted,
such as July 31st, check in one night, and then the hotel name with the hotel prices.
So you can see here, that's just web scraping in action, and based on all this data I collected
from the various tests that I ran, we were able to establish a grading system to determine what
gets what. Let's run a few more examples, just so you can see things in action. So let's go into
the Selenium-based folder, Examples, CDP mode, and we have a lot of examples here. So let's run
another example where we're going to bypass Cloudflare on the GitLab webpage. So let's run that.
We're going to go to GitLab.com, and you can see here that it was just bypassed right away.
Then we're going to highlight some elements. It's going to show Selenium-based wasn't detected,
so that's pretty easy. Let's run it one more time, but this time we're going to give it a
bad user agent, so it forces the capture to be clicked. So let's do python.rogitlab.py-agent equals
cool. So I'm deliberately going to give it a bad user agent, so that the capture isn't bypassed
automatically, and then Pyotogui controls the mouse, and then clicks the capture, and then it's
bypassed just like that. So that's just an example where Selenium-based is able to bypass that
bot detection. Let's run another example. Let's do python.rogunited.py, where we can
web scrape prices from United Airlines. So we're going to go in. We're going to add in our
from destination, which is New York, New York, or actually New York, and then go to Orlando,
MCO. It's typing all that in, going very quickly, trying things. All right, so I found some
prices, and it looks like it's web scraping that. So if you look to the side here,
you can see all the various flights that it found, bunch of non-stop flights, the type of plane
that you're running on, your airport, et cetera, and then you've got prices like eco-basic
and economy. So all that was easily web scraped, showing that Selenium-based was able to bypass the
bot detection there. Let's run another example, python.rogunited.py, the different airline,
but we're going to do a similar thing to scrape those web prices. So let's go and depart
from, let's see, Boston. And then we're going to go to Chicago, and then it's going to search through all
that. Let's see, it's going through finding what's available. And we see here, not too many flights
were available, but I think it's due to using the date August 2nd, two stops, one stop, et cetera.
So I've found a few flights there. Let's see what else we can do. Let's do python, rawfootlocker.py.
That one has some anti-bought defense systems on it. So we're going to go in. We're going to search
for, let's see, Nike shoes. And then it's going to grab all the results, and then it's going to
start printing that out. So if we go over here to the console output, you can see all these various
Nike shoes with the prices and descriptions. So that is here, you know, Nike Air Max 90.
You got customer average rating, five out of five stars, 1,223 reviews, and the price 135
dollars. As just one example, there's just tons of different shoes there. So showing that the
web scraping was working successfully. Let's run a few more. Let's do python, raw, chat GPT.
So you can see that example working directly here. Let's do compare playwright to Selenium
Base and under 178 words. And it's going to display all that data from the query. And then once
it completes that, it's going to output that to the console. You can see that here. So this is the
output. It was able to web scrape chat GPT easily. And I also ran the same exact example in GitHub
actions where it worked as well. So let's take a look here. We've got other examples that we may
want to run. So let's do python raw planet minecraft.com. It's going to go in and success.
Cloudflare was bypass successfully. So yeah, that's an easy one. That was one of the ones I got
a C rating because I was able to bypass it easily both locally and also within GitHub actions.
So let's see what else we got here. Let's do python, raw, coals.pyk, O-H-L-S.py. There we go.
Going in, lots of various items. So let's do a search for Mickey Mouse 100 Friends Teal Pillo.
And you'll see that the results are coming up here. And then we're going to just go through,
see all the different results that came up. As it's web scraping that you can see here,
it outputted that to the console right here. All right, let's run another web scraping example.
Let's do price lines. Good python raw priceline.py. Because they've got some good anti-bought defense
systems. So we're going to search for hotels again. This is a different website that we haven't
yet tried. Let's go to Portland, Oregon, USA. We're going to select our dates. It's going to search for
that. And let's see, found a bunch of hotels like Kendall Wood Suites, Holiday Inn, etc. The
Radisson, a bunch that is showing. And you've got those prices right here. Price line hotels in
Portland, Oregon, USA with the checking dates listed here, etc. So yeah, that is going through
that. Let's see what else we can web scrape. Let's do python raw indeed.py. There's an example
of a site where there's a Cloudflare turn style capsa. We're going to bypass it. And then we're
going to search for a jet propulsion laboratory. And then we're going to hit a capsa.
Patagooh is going to automatically bypass the capsa. And we're going to see here NASA jet
propulsion laboratory. We've got info about the company, the CEO, description, etc. So all that is
here. NASA jet propulsion laboratory. So that was easily web scraped. So as you can see here,
there's just tons of different examples showing that we can bypass these anti-bought defense
systems. And a lot of these examples were running in GitHub Actions. It looks like there's a job
running right now right here. So if we click on that, I believe that's the one that quarries chat
GPT. Oh, it just started. So it's going to take a bit to actually get to that part because it's got
to go through and install all the Python dependencies, get sledding based going, etc. And then finally,
it's going to query chat GPT. So you can see here it's just getting all the setup done. And finally,
once that happens, it will run the Python scripts, such as Python raw chat GPT.py. And it's going
to run into bug mode so that if there's anything interesting there in the bug logs, it will display
that to the console here. So we're going through. We've got the input for chat GPT. And let's see if
we query that successfully because right now it's running up. There we go. We've got the answer
right here. So you can see here input for chat GPT and response from chat GPT showing that it works.
So I've just got all these different examples running here in GitHub Actions. So I can accurately assess
which anti-bought defense systems are good and which ones aren't. So if we go back to the presentation
slide, let's go over here and let's just make that big. Let's talk about the final results
of these grades. So you can see here, so hcapsha, funcapsha, and enterprise google recapsha basically
earn the a grade because I wasn't able to web scrape those at all. Whereas in the b column,
you have these here and the c column, you have those there. So now you know if you're a website and
you want to prevent bots from scraping you well, the ones that I struggled with the most are the
ones that got the a grade because they're very good at keeping the bots out. Whereas if you're using
a b or even a c type of anti-bought defense system, then maybe the system isn't that great because
I was able to bypass it. The grades do change year over year because sometimes things get better,
sometimes things get worse, but actually the grades have gotten a lot worse than two years ago
because of all the changes that happened in Chrome. So for instance, I did a query where essentially,
let's see, in a continued effort to enhance user privacy, many modern browsers have implemented
features that restrict or block certain tracking methods like detailed user agent data and installed
plugins. So based on all these changes that happened over the last few years to Chrome, less data
was being picked up by the websites. So they're having a harder time determining whether or not
you're a bot or a human. And that's why a lot of these grades fell into the BC category that might
have been a lot better a few years ago. I think Akamai has a good description on the timeline for that
on their website in their blog. You can see that this might have been the original user agent
for something. And then it became this. So you can see that the specific hardware details like that
were removed. And also the specific Chrome version has been shortened. So instead of the exact
like minor versions there, it just says something like this, like hundred dot zero dot zero dot zero
hiding some of that data and they even have a timeline for when Chrome made these changes that
impacted websites so that they weren't able to get as much data from you as they could before
making it harder for these websites to determine if you're a bot or a human. So that's pretty much
that. And you can read that on your own time because yeah, there's just lots of different
information about that there. So yeah, that is the presentation. And these are the grades that
everyone gets. Next time we're going to probably deep dive into more detailed anti bot bypass,
but essentially if you're looking for just a quick overview, these grades should give you a nice
summary of that. Well, that concludes this presentation. I'll see you all next time. Happy automating.

############################################################

[35/44] VIDEO: ARM64 Linux Browser Automation with CAPTCHA-bypass
URL: https://www.youtube.com/watch?v=bPQ3GZz1AtM
------------------------------
(Source: Original Transcript)
Welcome back to the automation show. Today we're going to be covering arm 64 Linux browser automation with capture bypass and we're also going to be talking about GitHub actions and Microsoft co pilot by the end of this presentation. You're going to combine everything that you've learned in order to be able to run browser automation scripts directly from GitHub actions.
It's Ubuntu arm 64 and then we'll be querying co pilot which has some captures on it to protect the information. So we're going to bypass that and then get the data and then upload that artifact to GitHub actions so you can download the full page source from what you just queried.
So let's run a simple example of that right from the command line. We're going to call a script Python raw CDP co pilot which is going to use the slinning base test automation framework in order to query co pilot and then as it does this you're going to see that a cloudflare capture is going to come up that's not going to be a problem for slinning base because it has a special tool that allows you to click on captures and bypass them.
And then as you can see here co pilot is creating the answer for slinning base and like scroll down here you can see that it's all coming out.
And then once it completes its response slinning base is going to save that information and then output the HTML to a file.
So you can see here it was saved here in the downloaded files folder co pilot results. So let's open that up. I'm going to do open that and you can see that these co pilot results were saved.
So this is a script that I ran and if you're wondering where that script came from you can find it in slinning base if you go to the examples folder and then go to CDP mode which is the special stealth mode of slinning base.
You'll find a ton of various examples the one that we ran just now was raw CDP co pilot here it is right here and you can see had various actions such as performing the query clicking the capture waiting for results and then finally outputting the HTML of that to the special folder that was provided.
And then that is basically the script that we're going to be running in GitHub actions as you can see here.
So you may have noticed that earlier this year Linux arm 64 hosted runners became available in GitHub actions for free for public repositories here's the blog post on that you could easily specify using Ubuntu arm 64 with this command here.
So that inside your GitHub actions YAML file you could specify that also a few things to point out that may be important chrome does not officially support arm 64 Linux however there were alternatives such as using regular chromium instead of Google Chrome in order to do this.
So just by doing pseudo apt install chromium browser as you can see below here you would be able to install chromium onto an arm 64 Linux machine so you could use that for your browser automation.
And if we go into the script here's a script that we ran and you'll also see there's a recent news update in the slinning base repo that arm 64 Linux support has been added which is good because you combine all those things and now you can basically have your GitHub actions YAML file running slinning base and bypassing captures in order to scrape co pilot results.
So here you can see in the matrix we're specifying that Ubuntu arm 64 instance and then we're going to be installing dependencies and then running the script you can see here Python examples raw CDP co pilot dot py and then we're going to upload the artifact using the actions slash upload artifact command.
And if you upload the artifact you'll see that there will be a link to it so if we click on that from the GitHub actions job and we save it you'll see that if we open it and we click here and we go to co pilot results dot HTML.
You can see that it was able to save those co pilot queries or the co pilot query that we made with slinning base right here so that you can just download it directly from GitHub actions and this is pretty cool because I don't think anyone else is able to query co pilot and scrape the data like that bypassing captures I mean there are other frameworks that come close.
But nothing with the stuff capabilities that slinning base provides so if you're not familiar with slinning base already it's a powerful browser automation framework it's basically Python API is for web automation testing and bypassing bot detection and there's just a lot that it can do.
For instance, it can do multi threading pretty well now, which is probably didn't before so we do something such as Python raw multi capture dot py it's going to spin up several different browsers and then for each one pyro gooey is going to come in and click on the capture so that it can bypass all that.
So all those are pretty much happening multi threaded but since there's only one mouse pointer pyro gooey can only click one capture at one time so that's why it queries them all up and then it goes from one capture to another as pyro gooey clicks through all that so that essentially covers everything that we're going to be learning today.
So here's the get up actions YAML file I run a bunch of tests in the slinning base examples repo from MD men's my own personal repo but I also create slinning base in its own separate thing with the slinning base organization and then slinning base repo where you'll basically have the read me file and all the instructions that you may want in order to bypass captures grape data perform automated testing it's pretty cool.
You can run all these tests in GitHub actions and it works just as well there and there's always lots of updates coming in I'm always you know I think I just updated it like 21 minutes ago because I needed to give co pilot more time to think because sometimes it's really slow to come up with an answer so I just add a little more wait time there just in case it needs it.
But yeah we get tons of releases regularly and there's lots of stuff here so be sure to check out the slinning base page on GitHub and there'll be tons of examples running from GitHub actions so that you can basically run whatever you want.
Alright well have fun automating everyone and I'll see you all next time.

############################################################

[36/44] VIDEO: High-speed CAPTCHA-bypass with Python
URL: https://www.youtube.com/watch?v=aF3ee0uTBm4
------------------------------
(Source: Original Transcript)
It's time for some high-speed capture bypass.
All right, let's see if Payato GUI can bypass a lot of captures.
Here we go.
Click, click, click, click, click, click, click, click.
Yeah, now that's what I'm talking about.
Today on The Hackers Show, we're going to show you how to bypass
captures using Python and a few advanced libraries to help you out.
Get ready for some serious hacking.
For this to work, you'll need to use two different repos,
Slinging Base and Payato GUI.
Slinging Base lets you control the browser,
be stealthy, and detect the location of the capture on the screen.
Whereas Payato GUI lets you control the mouse and the keyboard
so that you can move the mouse over the capture checkbox
and then click it with Slinging Base.
And both of these packages you can find on the Python packaging index.
So here's Slinging Base there, and here's Payato GUI there.
In order to install these packages,
you could do a command such as Pippin Stall, Slinging Base,
and that will install Slinging Base.
And then to install Payato GUI, you would do Pippin Stall, Payato GUI.
And with those commands run, you now have the libraries
needed in order to perform the next actions
for clicking on captures and bypassing them.
So let's take a look at some of the code that's used here.
So here we have a classic Slinging Base format.
First we'll import it from Slinging Base, import SB.
And then here you'll have with SB,
UC equals true, test equals true, as SB.
And it's using the Python Context Manager format.
UC is a special stealth mode of Slinging Base,
undetected Chrome driver mode,
and activate CDP mode here activates another stealth mode
called CDP mode, which is even more stealthy
because you can perform advanced stealth actions.
And there's a nice method here,
UC GUI click Capture, which lets you click on a capture.
So let's just run that example to see where we're at,
just one capture at a time.
Let's see Python, raw, turnstile.py.
It's going to spin up a browser.
It's going to go to the turnstile page.
And then Payato GUI is going to go and click on it.
And if everything was successful,
you'll see a success message.
So if we go back to the code,
you'll see it's actually quite simple.
Now note that in some cases,
you may want to add additional sleep time
between activating CDP mode and clicking on a capture
if you're immediately going there.
So you can do something such as SB sleep,
oh, let's say three seconds to be safe,
and then click the capture because sometimes
there's a few seconds where it loads in the beginning,
but it's hard to detect when the loading has completed.
So just like add in the sleep there and you're good.
So that's using the classic SlendingBase format
to click on a capture.
There's also another format, SB CDP,
which uses the pure Chrome DevTools protocol format
without using WebDriver at all.
And here's the syntax from that.
Let's see, from SlendingBase and port,
SB underscore CDP,
and then you'll do SB equals SB underscore CDP dot Chrome
with URL,
and then you'll use a method SB dot GUI click capture.
So it looks slightly different from what we used before,
but it is a different format.
And also as before, sometimes you may want to add
additional sleep time between loading the URL
and clicking the capture.
So you could do SB dot sleep, maybe two or three, et cetera,
and then do that.
So let's run this example here.
It should look a lot like the one we just ran.
So we'll do Python, raw CDP turnstyle.py.
We're gonna get here,
and then we're going to click the capture,
and if everything is good, you'll see a success message.
So that is how that works.
And then we can expand on that using multi-threading
by using a different library.
So we'll be using concurrent.futures,
and inside there you'll see thread pool executor,
which is used in order to spin up multiple threads
in order for performing actions.
So it uses a context manager format,
just like Selenium base does.
So you can see here with thread pool executor,
and then max workers equals a number.
So here would be the length of the URLs
because I created a list of URLs, which are identical,
but it's basically the same URL five times.
And then here as executor,
and then for URL and URLs,
then we do executor.submit with main,
which is the main method right here,
which has all that code,
and then the URL that we're passing into it,
because here it's main URL.
And that's how you'll do multi-threading.
So let's run that example.
Let's do Python, raw, multi-capture.py.
All right, it's gonna spin up five different browsers.
Up, throw hiding underneath that window.
That's funny.
I'll do that one more time.
Let's see, hopefully it's not gonna hide
underneath the window at the beginning.
Five browsers are spinning up, and oh, there we go.
You can see if you now,
I just click here, you can see all these different browsers.
There we go.
Uh-huh.
So that's essentially how the multi-threading works
using Threadpool executor in order to get all those
browsers spun up.
So all the code for these examples
you can find from the SlendingBase GitHub repo.
So if you go to github.com slash SlendingBase slash SlendingBase,
you'll find that there is an examples folder,
and inside that folder,
there will be a CDP mode folder
with even more examples that you can run.
So the three examples that I ran just now are all here.
So for instance, you'll have raw turn style.
That was the first one I ran.
Here it is right here.
And then we had raw CDP turn style.
That's right here.
And then we have the raw multi CD,
or raw multi-capsha, here we go.
And then that's the example that we ran there.
So all these examples,
you'll be able to find from the SlendingBase GitHub repo.
Also it's on the Python packaging index.
And also fun fact,
I got to meet the creator of Piyato GUI,
Al Swagart at Picon,
which is the International Python Developers Conference
where all the famous Python people around the world
come to hang out, talk,
give speeches, go to dinners,
and lots of other things.
So it's a fun event.
So I got to meet Al Swagart there.
So it's essentially combining SlendingBase with Piyato GUI,
which is what we were using for the examples that we saw there.
So there's that.
And all these examples,
such as the one here where we're using multi-threading,
that's all found from the SlendingBase GitHub page.
And there is a huge library there.
So if you're wondering about the CDP mode methods,
you can just scroll down to the CDP mode section
where there will be instructions on what you need to do.
And then there'll be various more advanced examples like here.
And then if you scroll down,
you'll see that there's a CDP mode API slash methods.
So all the methods that you'll want to use will be there.
So if you want to know about clicking on CAPSHA,
so that would be a search for click, there we go.
UC GUI click CAPSHA.
I just do a search for that.
You'll see the various places that it is.
And here it is in the CDP mode methods list right here.
There's lots of other methods for, say, clicking,
typing text in the text fields, drag and drop.
Just pretty much any type of browser action
that you can think of.
And some of these methods use piato GUI for the more advanced things
where you may want to control the mouse and the keyboard
to perform advanced actions.
Lots of other examples.
You want to find other examples of CAPSHA.
I think many of the other examples have that.
So for instance, if we do Python, rawgetlab.py,
there's going to be a Cloudflare turnstile at the beginning.
And then if it's not automatically bypassed,
slanting base will click on it.
Sometimes the slanting base stealth is advanced enough
that it will bypass the CAPSHA without the CAPSHA
forcing you to click on it, which is nice.
So there's lots of various examples like that here.
Now let's see.
So if we do, like, say, Python, rawgetlab.py,
there's going to be a Cloudflare CAPSHA on this page,
I believe.
Let's find out.
Oh, it's not making me click a CAPSHA.
Oh, maybe we bypassed that page entirely.
Let's try a different one.
That seemed us.
This was just an example of scraping data from Indeed.
Usually they have a CAPSHA on it,
but that time it was not even present.
So maybe I'd bypassed it really quickly.
Let's try a different example.
Let's do Python, rawglastore.py.
That also usually has a CAPSHA.
There it is.
Cloudflare turnstile.
And it was automatically bypassed by slanting base
without even forcing Pyrogui to click on it.
So that's also convenient.
There's a lot of stealth there.
So sometimes you don't even need the advanced things
like Pyrogui to click on the CAPSHA
because the CAPSHA will be automatically bypassed.
But there's just a ton of various examples.
Let's do one more.
Python, raw, planet, mc.py.
There's usually a CAPSHA here.
Oh, there we go.
Cloudflare turnstile.
And it was automatically bypassed.
And just for a bonus, Pyrogui went and tried to click it anyway.
In case it wasn't, but there you have it.
So that is CAPSHA bypass.
All these examples can be found
from the slanting base GitHub page.
These examples also can run in GitHub Actions
because the stealth works there as well.
And I have other YouTube videos
where I'm essentially going into GitHub Actions
and performing all these tests
and like clicking through CAPSHAs in there.
So it's quite versatile.
And there's a lot of documentation
if you go to the GitHub page and see the readme.
So lots of various examples.
You can use the framework for testing.
You can use it for bypassing bot detection.
You can use it for just general web scraping
and automation purposes, et cetera.
There's a lot that you can do.
And there's just lots of examples.
Probably multiple examples and the examples folder.
But for the stealth examples, be sure
to check out the CDP mode folder.
And you'll just have tons of examples
that you can try out there.
So that's essentially high-speed CAPSHA bypass.
And of course, the multiple CDP drivers,
oh, not that one.
I think we wanted multi CAPSHA.
There we go.
I've got a bunch of different multi-threaded ones.
But yeah, the key thing is that thread pool executor
lets you handle the multi-threading.
And also, inside SlendingBase,
we use another Python library called FileLock,
which basically handles the thread lock
so that when Pyotogui has to click on maybe five
different CAPSHAs at the same time,
thread locking works well so that only one CAPSHA
is clicked at one time because there's only one mouse pointer.
So therefore, you got to share the mouse pointer
with all the different browsers that are there,
popped up from the automation for clicking on the CAPSHAs
because you can only have Pyotogui click on one CAPSHA
at one time.
You can spread them out by maybe a second each click,
as you saw in the earlier example,
so that you can click all of them
without Pyotogui stepping on its own toes.
So yeah, that is pretty much everything
that we have for today's tutorial.
There'll be a lot more exciting SlendingBase tutorials
to come.
I'm always creating new releases and adding new features.
So be sure to check that out.
There's also Discord Room.
So if you're wondering about the link for that,
there should be a link right here,
SlendingBase on Discord and it'll show you the link there.
So if you have questions, you can always open an issue here
or get a discussion or go to Discord
where there's probably about 1,000 people or so around there
right now on the Discord for SlendingBase for that server.
So lots of help when you need help.
And lots of readme files for when you have time
to read something if you want to learn how to do it all.
All right, well, that concludes today's presentation.
I will see you all later.
Have fun automating everyone.

############################################################

[37/44] VIDEO: Using Comet Browser for stealthy automation and CAPTCHA-bypass
URL: https://www.youtube.com/watch?v=MJ-0rE6RmVc
------------------------------
(Source: Original Transcript)
A few months ago, Proplexity released a brand new web browser called Comet.
But is it stealthy?
Can it bypass bot detection and solve captures?
Find out today on the hacker show.
Get ready for some serious hacking.
All right, let's jump right into the examples.
We're going to be using a framework called Selenium Base,
which has the ability to spin up a Comet browser and be stealthy.
So let's run an example.
Python rawgetlab.py dash-commit to use the Comet browser.
And on GitLab, there's going to be a Cloudflare turn style
at the very opening when you get there.
So let's see.
There you go.
Comet browser was able to bypass that capture with Selenium Base.
Let's run a few more advanced examples.
Let's do Python rawglastor.py dash-commit.
Let's see if we can be stealthy there.
It's going to go in.
As you can see, there's another Cloudflare turn
style on the opening page.
And we've just bypassed it with Selenium Base.
So that's another example showing that Comet browser can
be used for stealthy activities.
And it can even bypass captures.
Let's do a more advanced web scraping example.
Let's do Python rawordertickets.py dash-commit so that we
can use the Comet browser in order to get details on Jerry
Seinfeld shows coming up in the near future.
Here we are.
Jerry Seinfeld tickets, 34 results,
and all those results were just printed
to the console output showing that Comet browser can be
stealthy when used in conjunction with Selenium Base.
All right, let's go into the CDP mode folder where there's
going to be more examples.
Let's get some hotel prices with Comet.
Let's do Python rawglastor.py dash-commit.
It's going to spin up a Comet browser.
And it's going to go to the Hyatt website.
It's going to accept cookies and then put in destination
Anaheim, California, USA.
And then it's going to click to find hotels in the area
for the selected dates.
As you can see here, a bunch of results came up.
So now you have a bunch of Hyatt hotels and their prices
for Anaheim, California.
And wow, prices aren't bad.
So yeah, maybe a trip to California in the near future.
So that's some web scraping there.
In the next example, we're going to bypass some bot detection
for a website that uses hcapsha for defense.
Let's do Python rawnavada search.py dash-commit.
And let's see if we can get past that hcapsha defense that
would generally come up if it detects automation systems.
So it's going to go in.
And we made it past the part where they were generally
throw an hcapsha at you.
And we're going to search for businesses in Nevada
that are laser tag related.
And we can see here, business search for laser tag
and the output has appeared in the console output,
showing that that works.
Let's do Python raw.py.py dash-commit.
And we're going to see if sunny base with the comment browser
can web scrape data from Microsoft co-pilot.
Let's see how to start automating with selenium base.
And there's going to be a capture that appears.
However, selenium base was able to bypass that successfully
from the comment browser.
And now we've got a lot of data showing up.
And then once it's done grabbing all that data,
it's going to save the results into an HTML file.
So let's see if it was saved successfully.
It was saved into the downloaded files slash co-pilot results
section of my computer.
So let's do open that so that we can see if the data came through.
And yes, it definitely saved the HTML file.
You can see here if you open the URL,
it's the co-pilotresults.html.
So co-pilot was able to go in,
scrape the data, take a screenshot with selenium base,
and that data is here.
Up next, we're going to do an example with an airline search.
Let's do Python, raw, southwest.py, dash-commit
to see if comment browser can web scrape some airline prices.
Let's see if it works.
Going to southwest airlines.
And we're going to book a flight.
For the departure area, we're going
to set it to Boston.
And then we're going to arrive in Chicago.
And then it's going to perform a search.
And let's see if we can get some results.
Up, here we go.
Looks like results are appearing.
And selenium base is outputting those results
from comment to the web browser.
So here we go.
We have lots of flight data for Thursday, November 6th,
and the flight times, whether it's non-stop and the price.
So that's an example of scraping data from an airline.
So as you can see here, there are lots of examples
for bypassing bot detection and solving
captures from the selenium base examples CDP mode folder.
You can find selenium base on GitHub.
So if you go to github.com, selenium base,
you'll see that it's quite a popular repository.
And there's just a lot of documentation.
And selenium base lets you automate
on any Chromium browser such as comment.
So if you like one browser or another, you can pick it.
And I think OpenAI recently released a new browser
themselves called Atlas.
So now with all these new Chromium browsers,
you can easily set selenium base to automate with those
from the configuration.
Just on the command line, do dash-comment for a comment browser
or dash-atlas for Atlas browser.
And there you go.
For the CDP mode documentation, which
is what you'll be using for bypassing captures,
there's documentation right here.
Selenium base, CDP mode.
There are various YouTube tutorials.
There's one that I'm making right now
that I'll put up after this.
But essentially, everything that you need to know
in order to bypass bot detection with selenium base
using any Chromium browser that you want such as comment.
Well, that concludes today's tutorial.
I hope you have a great time automating
and I'll see you all next time.

############################################################

[38/44] VIDEO: Playwright Codegen vs SeleniumBase Recorder
URL: https://www.youtube.com/watch?v=Kl2z8JFiF7o
------------------------------
(Source: Original Transcript)
Today on the Hacker Show, we're going to be comparing two powerful tools used for generating test automation scripts.
One of them is called Playwright Code Gen, and the other is the Slending Base Recorder.
Get ready for some serious hacking.
Both these tools are very capable of generating automation scripts for you.
However, there are some noticeable differences, such as being able to perform hover and click actions,
clicking and iframes, clicking and shadowroot, drag and drop actions, and a few other things, such as stealth mode.
So, we'll get to these differences later, but first let's get started with the live demo.
So, we're going to be running a Playwright Code Gen.
Actually, it's already running, so I'm just going to close that out and start it from the beginning.
So, here we go.
So, once you've activated Playwright Code Gen, you're going to have a regular browser window open followed by the Playwright Inspector.
So, inside the regular browser window, you can put in a web page that you want to automate.
So, let's do SlendingBase.io slash demo page, which is an excellent demo page that has various items on it,
such as buttons, drag and drop items, sliders, drop down elements and more.
So, we've got the Playwright Inspector here, it fills in some information by default,
and you'll see as you hover the mouse over various elements on that page,
that the selector will appear and the area will be highlighted so that you know what you're doing.
So, let's create a simple script.
Let's go into this input field and type text1,
and then let's go into this text area and type text2,
and then let's go to the hover drop down and click link2,
and then let's go click this button here, move the input slider to 100%,
set this to 100% for the drop down, click a radio button,
click this checkbox, click this checkbox in an iframe,
and then do a drag and drop, although the model isn't letting me do that,
so there might be a bug there with Playwright.
So, once you've got that, you'll see that you script is generated.
You can select the target for your export.
So, for instance, if we do PyTest, you'll see a PyTest script generated.
We're going to copy that into a blank file here,
and it's going to be called recording.py.
And now, let's try running this script with Playwright.
So, let's do PyTest Recording.py-headed,
and it's going to go through, and you'll notice that it grows
because it can't do the hover action, so I'm just going to do it for it.
There we go.
So, the hover action for hover and clicking is one of the actions
that isn't recorded by Playwright when you're generating your script.
So, there are a few different things that it can't do,
but you might see that slunning base will be able to do those.
So, let's go back into the script that we had generated from that.
So, you'll see it has page.go2 with the URL.
You'll have various actions that it's going to perform,
such as finding an element, and then clicking it,
and then filling text inside it.
And then you'll see that even though it didn't do the hover for the hover and click,
it just got the click part recorded.
And then you'll see that it clicked the button here.
It moved the slider in this line here.
The select drop down was here, radio button, the checkbox,
and it even handled the checkbox that was inside an iframe,
which is something that slunning base would have trouble with,
since sometimes it can't really record inside iframe is depending
on if it's a cross origin iframe or something else.
And then, in the attempt to do a drag and drop where it wasn't really working,
all it really did was click on the element.
So, that is the script that was generated there.
Let's try to do something similar with the slunning base recorder.
So, I'm going to open up a new window for that,
and let's do S-base recorder.
It's going to spin up this little window here.
So, let's say we call it new recording,
and then we're going to record on slunningbase.io slash demo underscore page.
And we're going to click record.
And now, we're going to do the same actions.
So, we're going to do text one, text two,
hover click the link to click the button,
move the slider, select from the drop down,
click a radio button,
click a checkbox here,
click a checkbox in an iframe,
and then perform the drag and drop action here.
And once that has been done,
we're going to go into the script here,
and you can see here it's using a PDB debugger.
So, we're going to type C and click enter to continue,
and you'll see that it generated the script right here.
So, it has the open command where you're opening the URL,
you're typing text into the text field,
you'll see here is for text two,
and then it did a hover and click action there.
So, this is something that playwright was not able to do,
but slunningbase was,
and then it clicked the button,
it set the value selected from a drop down option.
So, this was from the my slider,
the set value thing here,
and then it clicked a radio button,
and then it clicked a checkbox.
It didn't record the click for a checkbox in an iframe.
However, it did get the drag and drop action here.
So, you can see that it was able to record a few things
that the playwright recorder was not able to.
So, if we see the script there,
you'll see that it wasn't recording all those things
with the playwright version of that script.
All right, so let's try running it now,
now that we've generated this.
So, let's go into this menu here,
and click the X to exit that.
Now, we're going to do Python, new recording.py,
and let's see if it did all those actions.
There we go, performed it again.
Let's run it one more time so that we can see it.
All those actions were performed,
and also, slunningbase has a cool thing called demo mode.
So, if we do that, dash, dash, demo,
it's going to run the same script,
but then you're going to see all the actions
that it was performing as it does this.
So, slunningbase has a few additional command line options
such as demo mode that playwright doesn't have,
so that you can do more advanced things,
for instance, highlighting elements
as you're clicking on them.
So, that was that example.
So, that is comparing basic actions with playwright
and slunningbase.
So, let's exit out of this,
and let's try a different example with playwright.
Let's do, we're going to run playwright code gen again,
but this time, let's go to a website
that has CloudFlare Capture Protection around it.
So, let's do getlab.com,
and we're going to go there,
and we're going to go to sign in,
and you'll see here that there is a CloudFlare Capture
appearing, so let's see if we click in here to record that,
and let's see.
Looks like nothing is happening,
so it looks like it's not able to bypass that capture
with playwright, all right?
So, that didn't work,
but let's try it with slunningbase
and see if that works.
So, let's go into the window and do space recorder,
dash dash you see for the stealth mode,
and that stands for undetected Chrome driver mode.
Let's go to getlab.com, and click record,
and then it's going to open the getlab page,
and then we're going to click sign in,
and let's see, bypasses that automatically,
also opened a new tab,
and now let's activate the recorder again
because you can see that the red bar disappeared,
so let's just do,
because it's a new tab,
let's do self.activate recorder.
All right, so now the recorder mode is active for this tab,
so let's just type name,
and then pass,
and let's go in here and type C to continue,
and you can see here it generated a script,
so let's play that back and see if we're bypassing the capture.
Here we go,
bypassed automatically,
and it did all that.
Now if we want to slow it down,
we can do playback in demo mode,
so let's try that,
goes in here,
and then it's doing it slowly,
it clicks sign in,
bypasses the capture,
types the name,
and the pass,
so all that recording was done successfully
using SeleniumBase.
Playwright was not able to get through due to the
anti-bot protection on the GitLab page,
so this shows that SeleniumBase is able to record
on websites when you need to bypass bot detection,
whereas playwright may have some trouble with that.
So if we go back into the chart to see what the differences are
between SeleniumBase and Playwright,
you can see here,
both these tools can record standard browser actions
and record assertions.
However, only SeleniumBase gives you the hover and click functionality
for recording.
Playwright,
code Gen is better with recording actions in iframes,
as well as in shadow root elements,
which SeleniumBase may struggle on.
However, SeleniumBase is able to record drag and drop actions,
as well as using stealth mode
in order to bypass bot detection on websites that are using those services.
So quick recap,
calling playwright code Gen from the command line,
spins up the playwright code Gen tool,
real have two windows,
the web browser window,
and the playwright inspector,
which will have the results of what is being recorded
in order to spin up the SeleniumBase recorder in stealth mode,
just type S-based recorder dash dash you see from the command line
and you'll get the SeleniumBase recorder app,
where you can type in a URL to start recording on and click record,
and that basically handles that.
And note that all the instructions for this can be found on the SeleniumBase GitHub page.
So if you go to github.com, SeleniumBase SeleniumBase,
and scroll down,
you'll see there is a recorder link,
which gives you full instructions for using the SeleniumBase recorder,
as well as a link to another YouTube tutorial on that,
and that will get you started with that.
And if you're looking for information on playwright code Gen,
you should check out the playwright section on github.
So let's go to Microsoft slash playwright,
and I'm sure somewhere in this documentation is a code Gen tool.
There we go, code Gen.
Click there,
and you have the test generator,
and you'll have an intro and how to generate tests in VS code,
and these are all the instructions that you'll need
for generating tests using playwright code Gen,
although note that if you need stealth capabilities,
then playwright code Gen might not be the solution for you,
in which case the SeleniumBase recorder with its stealth mode
will have an easier time bypassing bot detection
and recording on sites that try to block bots,
and that's a space recorder dash dash you see.
All right, well that concludes this tutorial.
I hope you had a great time learning about these various code generation tools,
and I will see you all next time.

############################################################

[39/44] VIDEO: Bypass bot-detection to get turkey (with Python)
URL: https://www.youtube.com/watch?v=GyOCRHINtzU
------------------------------
(Source: Original Transcript)
Thanksgiving may be over this year, but it's not too late to bypass bot detection and get more turkey in this
Example that we're running right now
We're going into stop and shop and doing some web scraping and as you can see from the beginning
There is a capture that tried to detect if you're running a bot and stop you but we bypass that using slinning base
So let's run that one more time so that you can see what's going on
We're going into stop and shop calm. It's verifying the device
Once it thinks you're not a bot anymore, let's you in and then slinning base takes over and then starts web scraping data from that
Website where we're getting results on fresh turkey and then printing that output to the console
So you can see here lots of results for fresh turkey from stop and shop
So you can see here various different items and their prices
So all that is an example of web scraping stop and shop if you want to see what the code for that
Looks like we're going to dive right in
So you might be familiar with slinning base in which case you'll notice the from slinning base and port SP line for this
particular slinning base format and then we're going to activate stealth mode so that's us equals true
And then we're also going to activate the more advanced stealth mode on top of it, which is CDP mode
So you can see here sp.activate CDP mode and you'll notice that there are other args that we've added in besides us equals true
such as test equals true, which adds in the runtime as you can see right here in this line here and
There are a few other things that are being added such as ad block equals true in case there's some additional
Advertising being added in we can block that out
So once we've activated CDP mode and we've waited a few seconds to see if we're bypassed the
Capture automatically then you'll see that we're going to wait for the brand logo link
Which is essentially the stop and shop logo that appears if you actually made it to the real stop and shop page
And then if it's not there, we're going to refresh the page and wait a little bit more and make sure that we're on the right page
Now we're going to set up our query which is fresh turkey and then the required text here is going to be what we're going to check for in the search results
In case stop and shop tries to throw in something that we didn't want and then the search box is going to have the CSS
selector for the search box on the stop and shop site
So we're going to wait for that element to appear and then we're going to type the query into the text box
And then click the search button to search for it
And then we're going to print some additional text right here
And then we're going to find all the elements that basically match div dot product tile
content and then we're going to loop through all the items and if it's not out of stock
We're going to print that out to the console and we're also going to flash some JavaScript onto that item so you can see it
And then we're going to basically make sure that we don't already have that item listed so that we're not printing out duplicates
And then print it out. So let's run that one more time so you can see that in action
So python raw stop and shop dot py and this is an example
You'll find from the slanting base examples CDP mode folder going in we bypassed the cap shot
We're doing some web scraping stop and shop is just one of many different websites that have bot protection on them or
Captures now you might be familiar with other types of bot detection out there such as Cloudflare's turn style
So if we just go web scrape a different page you can see what that looks like
So we do python raw get lab dot py you'll see that on this page
It's a different type of capture. It was the Cloudflare turn style cap shot and this different example that we're showing
So there's lots of various different types of cap shots now and
Others are getting more popular what we saw with the stop and shop one was a unique type of capture that's different from the
Cloudflare one and verify as the device
Once it's verified that everything's good it lets you in and then the web scraping just happens quite naturally
And you can get all the data that you want
So here we go going into the website grabs all that data
This was the full script for that. So if you're interested in
Getting more turkey because as you know Thanksgiving is over here in America
So people still want to get more turkey because you know turkey is good tastes good you know and all that so
Here's an example that just lets you search for more turkey and then you can make a decision to get which one you want
And if you want to know more about slenning base
You can go to the slenning base page on github
This was the example we were running which was the raw stop and shop dot py you can see the full script is here
So you can basically clone the repo and do your own search
Here's what the main slenning base github page looks like
Here we are slenning base
You can see it is a packed repo with a lot of different features
And one of the more popular features as people may know by now is the stealth mode which would be the cdp mode
Lots of different instructions and tutorials for how to use that so you can web scrape any website
Even if they're using bot detection and other advanced stealth abilities on it to try to detect your bot and other things
So that is slenning base and what you saw earlier was getting turkey. So yes
If you like turkey
Stop and shop is a good example that you can run although note that if you're not coming from a us based ip address
Then it's possible that they're going to block you because stop and shop is unique to the us
So they might try to block everyone else coming into their website that isn't from us
But i'm not really sure i haven't tried that yet
But in case you get blocked there are other examples of getting food from shopping sites
So for instance, there's an Albertsons example
I think they're outside the us
You just do python
raw
Albertsons.py from that same folder that the stop and shop example is in
We're gonna go to Albertsons
And it's going to do a search
So let's see
This time we're going to search for avocado smoke salmon
Another great recipe or great thing to eat
And once we've gotten all the results it's going to go through
You can see all these avocado smoke salmon results right there
And now as it loops through all these items it's going to display all those
Items to the console and as you can see here lots of different avocado smoked
salmon
Items from the Albertsons website and above that was the earlier example that we ran
Where we were web scraping fresh turkey items from stop and shop
Well, that concludes today's tutorial
Hope you have a great time automating and i'll see you all next time

############################################################

[40/44] VIDEO: Stealthy Mobile Emulation with CDP (Chrome DevTools Protocol) and Python
URL: https://www.youtube.com/watch?v=QcfNk_wYi7A
------------------------------
(Source: Original Transcript)
Today on The Hacker Show, we're going to be using the Chrome DevTools Protocol in order to make mobile emulation stealthy for automation.
And to do this, we'll be using the emulation.setdevicemetrics override method, which you can find from the Chrome DevTools Protocol page.
Let's get started with a live demo.
Let's do Python, rawmobilegetlab.py
And this is an example that uses Chrome's mobile device emulator.
You can see that there was a capture that appeared, but it was bypassed successfully.
And you can see that slenium wasn't detected.
To show you what that example looks like if we're not using mobile emulation, we're going to run Python, rawgetlab.py.
And you're going to see that it uses the full screen instead because it's not using the mobile emulator.
So you can see the mobile emulator can be stealthy.
And now we're going to run another example using the mobile emulator.
Let's do Python, rawnordstrom.py, dash-mobile in order to kick off the mobile device emulator mode.
You can see that it's going to Nordstrom.com.
And we're going to do a search for cocktail dresses for women in the teal color.
And it's going to go through all the items that it finds.
And then for every item, it's going to display that item with the price in the console output showing that the web scraping is working successfully.
So you can see here there are a lot of different items that are coming up in that web scraping example.
So that was the rawnordstrom.py example, which you can find on the slimming base examples CDP mode folder on GitHub.
So these are all the examples that you see here that are in that folder.
And you can just clone the repo and run any of these anytime you want.
So if we go into the details for the Chrome Dev Tools Protocol, you'll see that there's lots of different arguments for set device metrics override.
And you see here, you've got with height, device scale factor, mobile scale screen width, screen height, positions, the viewport, etc.
And because we're using a Python web automation framework in order to make this work in our Python framework, we're going to be using a separate framework that well, we're actually already using it.
It's called my CDP and it basically has a translator that basically converts the Chrome Dev Tools Protocol into a Python format that can be called directly from a Python automation framework.
So if you're wondering more about my CDP, here's the link on GitHub.
It's a Python interface for the Chrome Dev Tools Protocol, which enables direct control of Chrome without external automation drivers.
You can use any CDP method from there.
And this, of course, the framework we're using is slimming base.
And the examples that we're running are from the slimming base examples CDP mode folder, which you can find right here.
And these are all the examples that we ran here.
So let's go into the code so that you can see what exactly it looks like and how to use the mobile device emulator.
So in this particular example here, we're going to be doing loop dot run until complete with tab dot send to send the my CDP dot emulation dot set device metrics override.
And that basically passes the arguments such as with height device scale factor and mobile to it.
And if you want to use these exact same arguments, but not have to write all this code here, there's a simplified way to do that by just saying mobile equals true.
And it will accomplish the exact same thing, but without having to put out all this code here in the long format.
So let's run that example just to show you how it works. That's raw basic mobile dot p y.
So type on raw basic mobile dot p y.
And it should look the same as before.
We've got the get lab dot com page with the capture, but that was bypassed automatically because mobile mode is stealthy with slimming base.
So let's go into the examples again and see how it all works out.
So in the long format, you'd have import my CDP at the top.
And then you'd import slimming base. So from slimming base import sp.
And then you'd set up the context manager with sp you sequels true. That's the undetected Chrome driver mode, which is stealthy.
And then test equals true basically outputs the data to the console output like this.
You can see that the test ran and passed in a certain number of seconds.
That's what you get from the test equals true parameter.
And then inside we'll set the URL and then we'll activate CDP mode, which is the super stealthy mode that uses the Chrome DevTools protocol.
So we'll set the tab by getting the active tab.
And then we're going to set the event loop so that we can call an async method from within a sync context.
And because all the CDP code is actually in async format, we have to do this event loop so that we can get it to this sync format.
Although note that there is also an asynchronous format for the Chrome DevTools protocol my CDP.
And it looks like this. So instead of having to do the event loops, you could do a wait.
And then call the method directly driver.maintab.send and the same mycdp.imulation.set device metrics override method with the arguments such as with height, device scale factor and mobile equals true.
So this is the async version of that same script. Essentially, it looks a little different because instead of the synchronous API, you're using the asynchronous API.
So that would be an async method there for the main.
And then you'd have awaited methods called from there so that you can use the asynchronous format.
So back to here, once we've done the loop dot run it until complete so that we can set the device metrics override.
Then we open the URL and do all the other things such as calling the solve capture method, which basically if the capture wasn't passed automatically, it'll take care of that for you.
And then a few assert statements to show that you made it to the page successfully. Otherwise you'd get a stack trace in the console output because something would have failed.
So there are different formats for this. So as you can see here, that's just using mobile equals true in order to simplify the code by a lot.
And there's also another format that uses spcdp. So here from sunny basin port sp underscore cdp.
And then you'll see the call is a little bit different in the beginning. You have sp equals sp underscore cdp dot chrome.
And then you do the same loop dot run until complete in order to call my CDP method that sets the device metrics override.
So there are various formats for this. Also in this particular example here, which we're about to run the raw mobile row blocks dot py example.
We're going to be changing the user agent because that is an option, although note that if you do change the user agent, your bot might become detectable because if the user agent doesn't match your browser perfectly, a website may be able to detect that and then block you as a bot.
So let's run that particular example. Let's run Python raw mobile row blocks dot py.
And you can see here roblox.com. And it's the mobile emulator version. So roblox for Android and then continue an app.
So you can see that that ran and that used the mobile emulator. You can also run the async version and it should run the same as the regular version.
So let's do raw mobile async. So you can see that async pretty much runs the same way as sync, but it just looks different in the code.
So that's raw mobile async Python raw mobile async dot py. And let's run that. You can see does the same. There was a clad player cap chef beginning, but it was bypassed.
And now you've made it through successfully. So that is that example.
And there are plenty of other examples that you can run from the slain base page on GitHub. Some of these work well with mobile.
Just be sure to add the dash dash mobile argument. If it doesn't already set mobile equals true because dash dash mobile is a shortcut for that.
Going back into the code, you'll see from here mobile equals true, but dash dash mobile also lets you do the exact same thing.
So that pretty much covers the Chrome Dev tools protocol for mobile emulation and note that emulation dot set device metrics override is the API method that does all the magic for that.
Also note that if you have any questions, we do have a very active discord server where lots of new members come daily.
Today is December 4th, 2025, and a bunch of new members appeared and there's lots of different channels. There's a discussions channel. There's a releases. There's a YouTube section where new videos come.
There's the general chat, the UC mode chat, CDP mode chat. There's a support channel. There's also the community room where there might be a poll where people can pick to see what video they want me to do for my next YouTube presentation.
Also note that I often speak at Microsoft conferences, such as in this photo here, where I was speaking about slinning base at Boston code camp hosted at Microsoft.
So if you're around the greater Boston area, you might find me speaking about slinning base at one of those Microsoft events.
So that pretty much covers all the Chrome Dev tools protocol talk that will be covering today with slinning base and of course my CDP.
So if you have any questions, be sure to reach out, check out the slinning base get up page for all the details.
And if you want to know more about the stealthy mobile mode, just click on CDP mode and you'll find lots of documentation as well as links to YouTube videos that will help you get started on creating your automation scripts bypassing captures and doing all the other things that you'd like to do with your web automation.
Well, that concludes today's presentation. I will see you all next time. Happy automating everyone.

############################################################

[41/44] VIDEO: How changing the user-agent affects mobile emulation
URL: https://www.youtube.com/watch?v=WfAMalkiG_0
------------------------------
(Source: Original Transcript)
Websites may change what they show you depending on your web browser's user agent.
With the Chrome DevTools protocol and an automation framework, you can change your mobile experience on any website and even bypass bot detection.
I'm about to show you how to do that with Python and there'll be live demos on more than 10 major websites.
This is the Stealthy Automation Show.
Get ready for some serious hacking.
In order to make the magic happen, we'll be using the Chrome DevTools protocol in order to change the user agent and set mobile device settings.
So one of the methods that we'll be using for this is emulation.setuseragentoverride, which you see here.
Now let us override the user agent.
And additionally, we'll be using the emulation.setdevicemetrics override method in order to set the mobile device metrics for the emulation that will be running through our automation.
And Sunnybase will be the web automation framework that we'll be using.
And my CDP is basically the connector to the Chrome DevTools protocol that allows us to call CDP methods from an automation framework.
Alright, so let's jump into the code for the live demo that we'll be running.
So this is the example, rawmobileagent.py, and you can see that it's going to be setting mobile equals true.
But that's just a shortcut for all this code here, which basically calls mycdp.emulation.setdevicemetricsoverride with some mobile device settings.
And it's also going to be setting the user agent that we've defined up here in here.
So let me explain this script that we're going to run.
So in this script, so we've set this custom user agent and we're going to set a bunch of sites that we're going to automate on.
You can see here, we've formed a little list and with all these sites, we're going to extract that and generate the full URL.
And then we're going to do a loop for URL and URLs.
And then we're going to use Sunnybase to launch a mobile web browser in UC mode.
And then we're going to set the window position, activate CDP mode, open the URL.
Wait a few seconds, open a new driver, set the window position to be more to the right, activate CDP mode again.
But this time with the custom user agent, open the URL and then wait for a bit so that I have time to explain the differences that you see.
So now that you see the code that we're going to run, let's get started with running it.
So let's do Python, raw, mobile agents.py and here comes the fun.
Here we go.
First, we have Facebook without a custom user agent and then we have Facebook with the custom user agent.
So you can see that there's a difference in how the website appears when you have a different user agent going into the site in mobile mode.
For the next example, we're going to be using Twitter.
So you can see here, this is how the site looks without a custom user agent.
And on the right, that's what it looks like with the updated user agent.
So you can see the website is basically throwing something new at you, depending on what your user agent string is.
Here we go.
This is an example for LinkedIn.
And here's the example on the right with the changed user agent.
It looks similar, but there are some differences like explore jobs.
Welcome to your professional community, et cetera.
The page looks a little different, the buttons, et cetera.
Up next, we have YouTube.
And you can see here it's a little simple, try searching, get started.
But in the one where we modified the user agent, you now have the search bar visible and the YouTube logo in big, bright red.
So that's the difference in YouTube.
Up next, we have Firefox.
Take control of your internet, download Firefox in the non user agent one.
And on the right, we have the custom user agent, get Firefox browser per Android, et cetera.
So you can see that's the same URL, but the website is giving you a different version of its website, depending on what your user agent is.
Up next, we have Amazon.
So you can see on the left without a custom user agent.
And on the right with the custom user agent, you can see that the website looks quite different.
But it is the same URL, just a different version of the website that they're serving to you based on your user agent string.
Here we go.
Here is chat GPT on the left, and then chat GPT on the right.
But the main difference is right here at the bottom right, the voice control versus the message send thing.
So it's pretty similar, both versions of the website, but there is a small difference there.
Up next, we have Gmail.
So you can see here on the left without the custom user agent and on the right with the custom user agent very different.
You have like the email type in for the sign in, et cetera.
So you're seeing a different version of Gmail based on your user agent.
Up next, we have perplexity AI.
And you can see her on the left without the custom user agent and on the right with the custom user agent.
And here it says once you to download now, when it's using that custom user agent string, it's a different version of the site again.
So you can see here, lots of different sites have different versions depending on your user agent on the left, one snap chat and on the right, a different snap chat.
You can see that it's a little different.
You have like the open and snap chat bar right there.
So different again up next.
We've got let's see TikTok and TikTok.
We'll see here up there we go on the left one version and on the right once you to get the full app experience by opening TikTok through the app, et cetera.
So different version of TikTok.
Let's go to the next one.
Let's see we've got roblox.com on the left once you to sign up and start having fun with the registration.
And on the right, it wants you to continue in the app roblox for Android.
So you can see here, all these different versions of the exact same website, depending on your user agent string.
And let's go jump in to the code again, just so you can see what it was.
This is all quite simple, what is happening here.
We set our custom user agent.
We set a bunch of websites to basically loop through in this for loop.
And then we've activated CDP mode with mobile mode and UC mode.
And then we've set the custom agent on the second time.
And that's how you saw the differences in those websites.
So that essentially basically shows you that the user agent makes a difference.
And it's also important when it comes to bypassing bot detection because the user agent can affect whether or not the website thinks your web browser is being controlled by automation or not.
So up next, let's try running some examples with bypassing bot detection from the examples CDP mode folder we have here.
Up first, let's do Python, raw, mobile, GitLab.py.
This is one of the examples I ran previously in the previous tutorial.
You see there was a Cloudflare capture there, but it was bypassed successfully because slunning basis able to bypass bot detection in mobile mode.
And there's just tons of different examples you can try.
So we go to, let's do Python raw pixel scan.py dash dash mobile in order to set the mobile device emulator.
Let's see how this one runs going to pixel scan where it's going to check if you're a bot.
And it looks like the browser fingerprint is consistent that no masking is detected and no automation behavior detected.
That showed that slunning base was able to give you a stealthy mobile emulation within your web browser that a website could not detect.
So there are just tons of examples here and lots to try.
Up next, let's try a new example.
Let's do Python raw copilot.py dash dash mobile.
Let's see if this one works.
So we've got copilot dot Microsoft dot com.
And let's see if we can query that how to start automating with slunning base.
And let's see if it goes through in this mobile emulator up.
There you go.
You can see that it's thinking and it's able to get an answer here.
So this is the copilot site that you would see if you're using the mobile device emulator you can see here.
It got the different results and it didn't block you for any, you know, bot detection, etc.
So it showed that slunning base was able to be stealthy in the mobile mode.
And there are just tons of examples here that you can run at your own time.
But let's jump back to the Chrome DevTools protocol.
So that you understand the methods you need.
You need to set your user agent with this method emulation dot set user agent override.
And of course, you've got the emulation dot set device metrics override.
So you can set all your mobile device metrics, such as the viewport, the scale, etc.
And all that is basically in the Chrome DevTools protocol.
And my CDP is the connector that allows you to take that Chrome DevTools protocol
and bring it into your Python automation framework, such as slunning base,
which we were using for this example.
And there are just tons of examples you can find in the slunning base examples folder.
And then there is a CDP mode mode folder for more advanced stealth examples.
That's slunning base examples CDP mode.
And there's just a huge read me.
If you want to understand how all that works,
I'm continually expanding on this read me with more instructions,
such as stealthy mobile, etc.
There's a lot more exciting features to come.
And you're going to find out just how stealthy this can be with all the new advanced features
that will be releasing soon.
All right.
Well, that concludes today's tutorial.
I hope you enjoyed your automation session and I'll see you all next time.
Happy automating.

############################################################

[42/44] VIDEO: Playwright can hijack web browsers and become stealthy with connect_over_cdp()
URL: https://www.youtube.com/watch?v=vT19Uri0ntw
------------------------------
(Source: Original Transcript)
playwrights connect over CDP method is the most powerful playwright method that you've never heard of it could have easily been called hijack web browser, which is what the connect over CDP method actually does but due to other implications you can't really call it that and if Microsoft did do that then security researchers from all over the world would be jumping at Microsoft saying how could you possibly create such a method well the method does exist. It's just connect over CDP and
it basically lets you take control of an existing Chromium browser via the remote debugging port and then playwright can do whatever it wants with that web browser chat gbt also summarized it quite nicely it connects to an already running Chromium based browser using the Chrome DevTools protocol and it uses that ability via the remote debugging port so any Chromium browser will have these features that will allow you to have playwrights
use the connect over CDP method to take control of that web browser and do whatever it wants with it and if you look through the playwright code base you can see that there's connect over CDP all over it here's the example from the regular Microsoft playwright repo and here's the same thing but with the Microsoft playwright Python repo you can see the connect over CDP method
and then here's an example where the URL is being passed and it contains the remote debugging port so there's that which basically lets you connect playwright to an already opened browser via this remote debugging port and this allows the playwright browser to basically inherit the abilities that this other Chromium browser already had
so essentially it gains control of that browser and all the superpowers that are abilities that that browser had now this sounds like something from a movie or a TV show you're probably right I asked chat gbt about it and they basically said that there are several known villains from various shows such as siler from the TV series heroes that basically can take powers away from people and there's also rogue from X-Men
X-Men which she can absorb powers by touching someone and then she gains their superpowers but that is essentially what playwright is doing with the connect over CDP method there's already an existing browser running playwright comes in calls connect over CDP takes over that browser and then gains those browsers abilities
and then you can run any playwright method from within that new instance so in this example here we have a web browser that's being spun up by slenium base a completely separate framework and then once we've grabbed the endpoint URL we can feed that endpoint URL into the connect over CDP method which then makes playwright take over that web browser
and gain all its special abilities so let's run an example of that just so you can see how that works this is the raw basic sync dot py example from the slenium base examples CDP mode playwright folder so let's go run python raw basic sync dot py slenium base is going to spin up the browser but then playwright comes takes control of it
and then can do whatever at once with that browser because the connect over CDP method is really powerful let's take a look at the script let's open raw basic sync dot py and you can see here is the code for that we're going to be importing playwright we're going to be importing slenium base we're going to spin up a slenium base browser we're going to grab the endpoint URL
and then we're going to feed that endpoint URL into the playwright connect over CDP method which then allows playwright to take control of that web browser and then after some default setup steps that you'll see with regular playwright scripts
you can then call regular playwright methods such as page dot go to with the URL and then do all your other playwright methods and you can still use the existing methods of whatever framework browser that you took over for instance here we're calling a slenium base method which just sleeps for one second
so you can see the last page before the browser closes at the end basically allowing you to combine all the abilities of your first framework with your second framework and now playwright has all the powers so we just put in a break point right here we're going to pause execution
just so you can see that the browser was spun up with slenium base and then we're going to continue from the debugger so you can see playwright coming in and taking control and basically doing whatever it wants with that browser
so let's run that again let's do python rob basic sync dot py we're going to run that from the command line you can see that the browser paused and now we're in a break point so we're going to go into the line where does page dot go to because we just run connect over CDP
and now if we go back to the browser we can see that it went to that page so basically you have all the apis that slenium base has because that was the original browser and you have all the apis that playwright also includes so for instance if you do page dot and then hit the tab key
you can see all 109 possibilities so here are all the playwright methods that are available to you from within this special browser session
in addition to that you also have all the slenium base methods that you can add in on top of that so for instance sp dot and then hit the tab key
you can see 188 possibilities and then you have all the slenium base methods there as well
so essentially when you combine the connect over CDP that playwright has with another automation framework you have the abilities of both automation frameworks
it's like some super villain coming in taking someone else's powers from you know from like a superhero and then it's able to basically use those powers with its own abilities
and that's essentially what we have here so if the framework that you take over has maybe a stealth ability that lets it bypass captures then all of a sudden playwright gains the ability to bypass captures in that web browser
so let's do an example of that so let's take a look at some of the examples that we already have here for instance there's a special Bing Capture
let's open up that example that would be Python raw Bing Capsync but let's first open it up so that you can see what it looks like
so here you can see we're going to go into the Bing dot com slash Turing Capture Challenge page and there's going to be a capture there
and we're going to see if playwright becomes stealthy once it takes over that slenium base browser that already had a stealth ability inside CDP mode
so let's run that so this is raw Bing Capsync so let's do Python raw Bing Capsync.py
it's going to spin up a web browser there's a capture there verifying and success showing that playwright gained the ability to bypass that capture
so let's see what else we've got there let's see uh-huh let's do a co-pilot example because usually they throw a capture at you if you're going too fast
however slenium base has a method solved capture that can bypass a capture and then playwright will inherit that method too with the connect over CDP method
so let's do open raw co-pilot sync so you can see what that code looks like here it is slenium base spins up the browser and then playwright comes in takes control
you can see all these methods there and you can see that in some cases you may need to solve a capture and slenium base already has that method so we're going to call it from there
so let's run that method let's do Python raw co-pilot sync.py
all right so we're going in and slenium base spins up the web browser we encounter a capture because playwright took over but now slenium base has the solve capture method
which lets you bypass that capture and now you can see information about using the connect over CDP method with playwright
so this shows that playwright is able to gain new abilities like stealth abilities and the ability to bypass captures just by taking over a framework's browser that already has those special stealth abilities imbued in it
so that was the example with co-pilot and playwright and slenium base basically combining the two frameworks together because playwright's connect over CDP method lets you do that
now let's try another example let's open up the raw seat geek example that's going to be an example of another web page that's going to have bot detection on it
we're going to launch those stealthy web browser with slenium base and grab the endpoint URL and again playwright is going to come in take control of that web browser
and then you're going to see playwright code that basically does most of the other work but then slenium base comes in and solves captures or whatnot if need be
so let's do a search for jerry sign failed tickets with the playwright example here so let's do python raw seat geek sync dot py and we're going to open that up
so slenium base is spinning up the web browser and then playwright's using connect over CDP to take control of it and do a search for jerry sign failed tickets
and as you can see here playwright inherited the stealth abilities that slenium base had in order to get that information
so this is an easy example of playwright coming in and absorbing the superpowers of any framework that it wants to take over because the connect over CDP method lets you do that
it's very powerful playwright can essentially do whatever it wants with any web browser because you can just take control of it assuming it's a chromium based browser
and then it gets all those abilities it gains the methods of that and you basically have a super framework that can do anything
and this is the power that playwright has there are a few other examples that you might want to check out from there
let's see let's do the walmart example that's a good one so let's open that up just to take a look open raw walmart sync dot py and you'll see that it has a lot of code here
so slenium base basically just spins up the stealthy web browser then playwright takes over it as you can see here
and then it combines some playwright methods with some slenium base methods and then essentially you can do whatever you want
there's a lot more flexibility because you can use the methods of either framework and let's run that just so you can see how that works
let's do python raw walmart sync dot py and let's see if playwrights able to still be stealthy when it inherits slenium bases stealth abilities
here we go we're gonna search for the settlers a good tan board game and you can see here that results came through showing that playwright was able to grab all this data and be stealthy
because it inherited the superpowers that slenium base has which is the ability to turn any chromium browser into an anti detect browser
and so playwright now has those abilities too so if you're wondering more about the slenium base integration that I have for playwright
I basically created a thing called stealthy playwright mode which spins up a stealthy browser with slenium base
and then playwright uses its connect over CDP method to take over that stealthy web browser and then it's able to do whatever it wants
and still be stealthy so generally playwright by itself is not that stealthy but when combined with another framework that is stealthy
and connect over CDP method playwright essentially has the superpowers that it needs to basically do whatever web scraping that it wants to do
so that is stealthy playwright mode and there's gonna be a lot more information on that in future videos that I'll be posting to youtube
so be sure to like and subscribe if you like the content and I will see you all next time happy automating

############################################################

[43/44] VIDEO: Stealthy Playwright Mode: Bypass CAPTCHAs and Bot-Detection!
URL: https://www.youtube.com/watch?v=PnFD_gSmGUc
------------------------------
(Source: Original Transcript)
Today on the hacker show, we're going to be bypassing bot detection and solving
captures with playwright. Specifically, the Python version of playwright, however,
the same principles will also work for other versions, such as JavaScript, etc.
So this is the playwright Python library on GitHub. And inside the documentation,
you'll see that there are no trade-offs and no limits. However, I'm going to make some slight
modifications in order to make that statement be actually true. So this is what playwright
generally looks like for Python. You're going to be importing it, and then you'll have a line
such as with sync playwright as p, and the async version looks like this. And normally,
the web browser is launched with a command like this, browser equals p.chromium.launch.
However, that is the part of playwright that spins up a web browser that isn't so stealthy.
However, the rest of the commands that playwright runs, which uses the Chrome DevTools protocol,
that is stealthy. So in order to make playwright more stealthy than it is now, we need to replace this
line here with something else that gives us a stealthy browser. Now, playwright already has a method
called connectovercdp, which basically lets you attach playwright to an existing browser instance
using the Chrome DevTools protocol. And this is the key to making playwright stealthy,
because you can use a stealthy web browser as opposed to the fault web browser that playwright
gives you, which isn't so stealthy. So now you'll see that the browser is spun up with this line,
browser equals playwright.chromium.connectovercdp with the local host and then the remote
debugging port, which is usually 9222. And then you'll set up the default context like this
and the page like this. And that's going to basically allow you to make playwright stealthy
assuming that you've already given it a stealthy browser to work with. And for more details
on connectovercdp, you can go see chat gpt. Basically, it lets you connect to an already running
chromium browser and it uses the Chrome DevTools protocol. So going into the code, you can see that
connectovercdp is used already quite frequently within the playwright library. And here is an example
of it being used in the Python context. And this is from github.com, Microsoft playwright Python.
So all that is already being used in various examples. But we're going to take that one step
further by spinning up a stealthy browser connecting to it and then performing playwright actions
while bypassing the bot detection and getting through captures. So we'll be spinning up the web
browser with another framework called selenium base, which is quite popular on github about 12,000
github stars right now. And it basically has a stealth mode called cdp mode, which lets you spin
up a stealthy browser. And with playwright, you can then attach to selenium bases stealthy browser
and then run all your existing playwright methods as you would normally. So if you've already
installed playwright, you can then spin up the web browser with selenium base if you have that
installed, and then connect to the web browser using connectovercdp. So there are a few different
formats where you can do this. So there's three in particular. There is the spcdp sync format,
the sp nested sync format, and the cdp driver async format. So for this tutorial, we're mostly going
to cover one and three. And two is a little special because it spins up the web browser with web
driver instead of Chrome DevTools protocol direct connect. So we're going to focus on the cdp
version of that. So here's an example of what that code might look like from playwright.sync API,
import sync playwright. This you've already seen many times before. And then you'll have from selenium
base import spcdp. And then you'll spin up the web browser with selenium base and then you'll grab
the endpoint URL using the get endpoint URL method. And then you're going to see some playwright code
that you may already be familiar with with sync playwright as p. And then you're going to set the
browser to connectovercdp and then set the other variables as needed. And then you can start running
any playwright commands that you want, such as page.go2. And then you'll be able to go to a web page
while using stealth mode so that you'll bypass any bot detection that they throughout you,
as well as getting past captures that may also be there. And then let's jump over to the cdp
driver async format because some of you might be interested in using the async version of Python
instead. And it looks a little different, but it's mostly doing the same thing underneath.
You're going to be grabbing the endpoint URL and then passing that endpoint URL into the connect
over cdp method. And then you can resume calling all your playwright commands as needed in order to
bypass the bot detection. So let's start with running some examples just so you can see how things
work. Let's do Python raw Bing cap sync.py. And we're going to run that. And there's basically a
Cloudflare capture there on the Bing.com Turing Captcha Challenge page. And playwright with Selenium
Base was able to bypass that. Let's take a look at that code here. So that's going to be the raw
Bing cap sync. This is the example that we just ran. And you can see here that we grabbed the
endpoint URL. We put it into playwright here using the connect over cdp method. And then we did
page.go2, which is calling playwright methods right from there. And you can see you went to the URL.
And then we bypassed the capture and it didn't even need the solve capture method, which is added in
case the capture isn't solved automatically. So Selenium Base not only gives you the stealthy web
browser that playwright can connect to, but it also gives you additional methods that may be helpful
depending on special situations that you may run into. So for instance, playwright does not have
you solve capture method. Selenium Base will provide that as needed. So you can use that if
captures aren't always bypassed on a page load. And there's lots of examples here that we're going
to cover. The next example that we're going to run is the planet minecraft example because there's
a cloudflare capture on it. So let's do that. Let's do Python raw planet and see sync.py.
We're going to run that. You can see here there is a cloudflare turn style there. And then with the
solve capture method, you can see that it successfully clicked the capture with that method and it was
bypassed. So let's take a look at that code again, just so you can see what happened there.
It pretty much looked similar to the Bing capture example we saw before, except this time we're going
to the planet minecraft website. And then it clicked the capture by using the solve capture method.
And then we verified that the capture was indeed clicked because on that specific website,
the input that was initially disabled, that input field, until you solve the capture,
and then it was no longer disabled. And this test here showed that the capture was bypassed
for that particular website. There's lots of other examples that we have. So let's show you
some of these other ones. Alright, so let's do another. Let's do Python raw footlocker sync.py.
Alright, so we're going to go in. You can see that there is the footlocker page. And let's do a
search. Let's see, it's doing Nike shoes. And then let's see if we can scrape data from that
website. So you can see here, data was scraped on various Nike shoe prices. And this is one of
those websites that has some pretty strong bot detection on it. But playwright was able to bypass
that bot detection with salining base. And we were able to get at all this data. For example,
what you see here, all these shoe prices and the details. That is all here. So let's take a look
at what the code for that looks like. That would be the raw footlocker sync.py.
It's a longer example, but pretty much same idea. Use playwright to open the page once you've
given it the stealthy browser. And then you can call playwright commands like here's page.click.
Here's another page.click. Here's page.wait for selector. However, with this special format
that we have, we can mix playwright methods with salining base methods into the same example
so that you can pretty much call methods from either framework all within the same script.
Because that's basically what you get when you've combined the frameworks, you've got the APIs
from both frameworks to choose from. So we can just mix and match. You can use whichever method you
want to use. And if you're more familiar with playwright, you can pretty much just use playwright
for everything except specifically some methods such as solve CAPSHA, which only salining base provides.
So you can see here we printed out the output that we found after we made the search
and we bypassed the bot detection in that process. And there's lots of various examples here.
For instance, if we go to the BingCap sync example, you'll see that here's what it looks like
when you do the async version of that. So it looks a little different because you'll need to
import async.io and then you'll be importing the CDP driver and then you'll have an async main method
such as here. You're going to spin up the web browser with salining base and then playwright will
attach to it becoming stealthy and allowing it to bypass bot detection and solve CAPSHA with the
solve CAPSHA method. So that's what that looks like. There's just tons of different examples.
Here's one where we're just calling a bunch of playwright methods just to show you that any
playwright method that exists can be called within this format. Let's see, there's just a bunch of
different examples here. There's a GitLab example because on this website there is a Cloudflare
CAPSHA that appears when you first go to it. However, salining base can bypass it. So let's run that.
Let's do Python raw GitLab sync.py. It's going to go in. There's a Cloudflare CAPSHA and it was
bypassed automatically because it was stealthy enough. You can see here that we went through and it
succeeded. So we can also run the async example. It should run the same, but the code will look
a little different. Let's do Python raw GitLab async.py and it should look the same as before. It
bypassed the CAPSHA and it got to the GitLab page which was protected by the CAPSHA but playwright was
able to get through it because it was stealthy. So lots of different examples there. I think we covered
all the main ones. Let's see any more good ones to run. I think, yes, let's do SeatGeek for the next one.
So let's do Python rawSeatGeekSync.py. It's going to go to the SeatGeek website which is
protected by Bot Protection and we're going to search for Jerry Seinfeld tickets. So the ticket list
is going to come through for the shows near you. You can see that it was outputted to the console.
So you can see here all the various Jerry Seinfeld shows that are coming nearby.
Let's take a look at the code for that example. That would be right here the rawSeatGeekSync.py
and as before, it's going to look very similar. Grab the endpoint URL and then feed it into playwright
and then open the page, do the search. So you type text into the input field and then you'd click
to get the results and then we'd find the results and we'd display that to the console. So that is
the SeatGeekSync example. I think there's another good example we can run. That would be the raw
WalmartSync.py. So let's run that next Python raw WalmartSync.py. All right, so it's going to go
to that page. It's on Walmart.com and let's do a search for, it's going to search for settlers
like a tan board game and then it's going to find all the results and then output that to the
console. You can see here all the various games and their prices. So that is the settlers
of Catan example for Walmart. Let's go look at the code for that. Here it is. This should all look
very familiar to you at this point. You use playwright to go to the page and then you'll click to do a
search. You'll do the search and then you'll use some code in order to nicely display all that output
to the console so that you can take a look at it. But you could also save that data to a data
structure of Python to use for later. So there's lots of different ways you can handle that. So that's
the raw WalmartSync example and just going back to the basics. This is what like the Async format would
look like. It uses a slightly different syntax but it supports both the Sync format and Async
format. And although we didn't really cover it much in today's tutorial, there is a nested Sync
format that uses WebDriver as well. So regular Sunny Bay Sync format with the CDP mode, the pure
CDP mode, it doesn't use WebDriver at all. However, the nested format does. So that that was you
to use WebDriver methods with Sunny Bay's methods with playwright methods. So it gets pretty
intense at that point. Although Sunny Bay's doesn't necessarily use WebDriver depending on the
format that it has because the newer Sunny Bay's formats use a pure CDP connection without using
WebDriver at all. So there's lots of different methods available and the APIs are listed from the
GitHub page. So back to the Sync example here, you'll have one context manager, and then you'll
have your playwright context manager from within that context manager that basically continues the way.
So in summary, if you want all the details on stealthy playwright mode, which is a special
mode of Sunny Bay's, that lets you use playwright when Sunny Bay spins up that stealthy browser
and then playwright takes over. That's essentially how it works. You've got all the examples,
the three formats that you'll want to take a look at carefully. Note the sync format, that's probably
the format you're going to be using unless you like using Async, in which case go to the Async
example here, and that will have the code that you'll want to follow. And there's just lots of
details and instructions on how to do everything that you'd want to do with playwright, with Sunny
Bay's, that whole combination basically gives you the stealth that you wouldn't necessarily get,
but if you make some slight modifications, now playwright gets the stealth abilities that you need.
And note that you have to change the default web browser that playwright spins up that you'd normally
use Chromium.Launch4, and that's where we're using ConnectOver CDP instead. And that is what makes
playwright stealthy. It's the web browser that playwright spins up that determines whether or not
playwright is going to be stealthy because all the other methods that it calls are stealthy by default.
However, the thing that gets you is that default web browser because playwright's default web
browser that it spins up is not stealthy. And that's why you need to use playwright's ConnectOver
CDP method in order to connect to an existing web browser that's running off of a remote debugging
port. And that basically allows you to make playwright stealthy and bypass all the captures and
bot detection that you want to bypass. So that pretty much covers this tutorial with playwright and
slennium base with stealthy playwright mode. And there's going to be a lot more exciting tutorials
to come, so I can't wait to show you what's coming up next. All right everybody, I'll see you all
later. Happy automating.

############################################################

[44/44] VIDEO: Stealthy Playwright on Linux Servers (with CAPTCHA-bypass)
URL: https://www.youtube.com/watch?v=6ab9HFxOyf4
------------------------------
(Source: Original Transcript)
Today on the hacker show, we're going to be using playwright and Python in order to bypass
captions and bot detection on Linux servers, specifically on GitHub Actions. As you can see here,
this is an example GitHub Actions job where we did some web scraping of various websites,
such as co-pilot and Nike and SeatGeek and Walmart. So we're going to go over the details of
that momentarily, as well as the GitHub Actions YAML file that made all that possible. But first,
I want to say that this is the follow up to my previous tutorial on stealthy playwright, which
you can find on YouTube. And it's recommended that you probably watch that before this.
So playwright Python is the automation framework that we're going to be using today for all the
stealthy automation and capture bypass. And this is what the scripts look like, although instead of
using the standard browser equals p.cromium.launch command in order to launch a web browser,
we're going to do something slightly stealthier, which is using playwright.cromium.connectovercdp
with the remote debugging URL. Looks like this, so it'd be localhost for your machine,
and then a port, which is usually 9222 by default. And this connectovercdp method is the key
to making playwright stealthy, because otherwise the default playwright browser that is launched,
when you launch a playwright script, that's not so stealthy. So let's take a look at the GitHub
Actions example where we're going to be running some automation, or actually the automation has
already run. So after setting up the job, which we did with this YAML file, which will come back
to in a moment, let's first take a look at how powerful the web scraping actually was. So
Copilot has some anti-bot protection on it. Yet with this GitHub Actions job, you can see that we
were able to query Copilot and get results from that. And then after that, we also wanted to find
out about Nike shoe prices right from the Nike.com website. You can see here we did a search,
and here are various shoes with their prices right next to them. So this is an example
of scraping the Nike website. Over here, we have an example where we found out about concert times
and dates from SeatGeek. So you can see here we did a SeatGeek search for Jerry Seinfeld,
and you have all the various days that he's performing. He's pretty good actually. He came by this
area not too long ago, and lots of dates there. So that is showing that we were able to bypass the
bot detection that was on SeatGeek. And then over here, we have the Walmart example where we're
web scraping Walmart for settlers of Catan board game, and it shows the various items that came up
as well as the prices along with it. So as you can see here, the stealthy playwright was able to
get at the data right from a Linux server, which is usually very hard to do, but it was able to do it
and we're going to show you exactly how all that works. So you can see here, we web scraped Walmart
successfully and got all that data. So let's take a look at the GitHub Actions YAML file. Actually,
if you just like click on Workflow file here, it will take you to that. So we're basically setting
up a job. We might give it a name, say CI build 8 because I have a lot of other builds that I do
for testing. And then this one is running on Ubuntu. And it's got a schedule run at the 42 minute
of every fourth hour seen here for all every day. And then it'll basically run every time you
push to the master branch. And then we're running on Ubuntu latest with this Python version 3.13,
which isn't the latest, but in case there are any bugs in Python 3.14, we're just using one less than
the latest. We're going to set the actions check out V6 and then set up the Python. And then
since this is Linux, we're going to execute this code here, where we're basically going to apt get
a few extra libraries that you'll need, such as TZ data, locales, etc. And then we're going to set
that, use the link to be US. And then update locale there. And then we're basically doing some
testing to make sure it works. But first we want to install a bunch of dependencies. So we're upgrading
pip. We are upgrading other Python packages. We're getting playwright, etc. And then let's see,
we also want Python xlib for the virtual display because we want to make sure that it still works
on Linux, which generally has a headless display, but automation is typically detected if you run it
in a headless web browser. So this Python xlib allows us to have a virtualized display that
appears real and allows the web browser to run as normal. So then we're just going to, you know,
make sure everything works, you know, test out what the different Chrome binaries that are on
the machine. And then we're going to start running the scripts you can see here. We're getting to
copilot, the Nike, the SeatGeek, and the Walmart examples right here. So here's where we ran
those. And then we gathered the data. And you can see here, after all that ran, if you can see
that, you can basically see the data coming in. And it's outputted to the console here in GitHub
actions. So this is all due to using the connect over CDP method in order to make playwright stealthy
because we're connecting to an existing Chrome browser that has already been spun up.
And in order to provide this Chrome browser, we're using stealthy playwright mode from
SlendingBase, which essentially spins up a SlendingBase CDP mode web browser that playwright then
connects to. So we have lots of instructions for that. You have the various formats that you can
use. And most of those examples that we ran in GitHub actions were using the SP CDP sync format.
This is essentially how it might look. You'd basically import sync playwright. And then you'd
import SP underscore CDP from SlendingBase. And then you'd spin up your stealthy web browser.
Then you would grab the endpoint URL and then feed that into the connect over CDP method. So then
browser equals p dot chromium dot connect over CDP. And then you can do all your regular playwright
methods, et cetera, in order to scrape the data. So let's take a look at what the script looked like
for the co pilot example that we ran. Here it is. So essentially we did page dot go to the co pilot
dot Microsoft dot com. And then we did wait for selector. And then a few other things where we
basically did page dot fill in order to set the query. And then we clicked submit here. And then
we basically if needed, we run sp dot solve capture. So that if there's a capture that appears,
but when you go into making a playwright query on co pilot, then SlendingBase solves the capture. And
then your script continues as is where you can use a combination of playwright methods along with
SlendingBase methods. Because essentially when you use connect over CDP, you're connecting playwright
to the existing automation instance. So now you have the methods and APIs from both frameworks
that you're using. So for instance, you'll have the initial SlendingBase methods that are there
when you spun up Chrome, as well as the additional playwright methods that were added in after you
used connect over CDP. And this basically lets you combine all the features of both frameworks so
that you can pick and choose what methods to use from which framework in order to do all the
web scraping that you want to do. And there's just tons of various examples that you can find
from the SlendingBase examples, stealthy playwright mode folder. Actually, it's the it's the
SlendingBase examples CDP mode playwright. And then if we do an LS, you can see all the various
examples that are already there that you can run. So if we want to run any of these locally, we could just
do Python, raw, co pilot, sync.py. And then you can see that you're going into the co pilot website.
There's the capture that came in. But then we used the SlendingBase Solve Captcha method in order
to get past that. And then we were able to get all that data from co pilot. And this is the exact
same example that ran successfully from GitHub actions right here. So if we go up to co pilot,
this is the data that we got here. And here's how it looks like running from the screen, although it
looks a little messy with the font size and all making it wide and all that. But essentially, there are
there's the data. So there are lots of other examples that you can run. So for instance, we ran a
SeatGeek example. So we could do Python, raw, SeatGeek, sync.py. And here's how that one looks like when
you run it from your local machine, we did a search for Jerry Seinfeld. And then it showed all the
shows near the location near you. And then it outputted that to the console. But technically, it'll show
all the shows all across the US. So here you go. Here you have that. So that was the other example
that we ran here. Let's see, raw, SeatGeek. So it looked like that. There is also an example where we ran
the automation on the Nike website. You can see it bypassing captures and anti-bought defenses and
GitHub actions here. If you want to see that one locally, we can do, let's see, Python, raw, Nike, sync.py.
Spins up the web browser. Then it's going to do the search once it finishes the page for
Pegasus. And then it finds all the Nike shoes that have Pegasus in the name. And it outputs that to
the console. And that was the same thing that we ran here in GitHub Actions. So as you can see here,
whatever you can run locally will also work in GitHub Actions because it also has the ability
to be stealthy if it's configured properly. And we showed you all the steps that you needed in your
GitHub Actions.YML file. Now, if you can't memorize all this, don't worry. You can just fork the
repo or clone it, et cetera. And then copy out the YAML file so that you can get all the specific
details that you'll need in order to make your automation stealthy when running from a Linux
server, such as GitHub Actions. Now, if you plan on doing like intense automation, we're running
at a high frequency. This is where you may need to use something called residential proxies.
Now, there are lots of different companies out there that provide residential proxies,
where basically you can set a proxy and run your automation using that. So for instance,
bright data is one such company that provides them. And I'm mentioning them now because they
actually use Selenium-based a lot. As you can see here, if you do a search in the bright data blog,
it got a lot of posts of Selenium-based, which is the framework that we're using in order to
provide the stealthy web browser. And they have a few different guides on using proxies with Selenium-based,
specifically their bright data proxies, et cetera, and bypassing CloudFlare and all that. So bright data
is one such option for getting these residential proxies. And in order to set the proxy when you run
your script, there may be a few different things that you want to add. So for instance,
when you run your script, let's actually go into a script so you can see what we would change.
So inside here where we have various options, such as here we're setting locale equals n,
and then adblock equals true. We could do something such as proxy equals, and then it would be like
user colon pass at IP colon port. And then assuming you actually have a real user name and password
and a real IP address and a real port number, that'll work. However, one other thing you'll
need to add, due to some recent changes in Chrome, you want to set use Chromium equals true,
because instead of using regular Chrome, we're going to use Chromium instead. And if it's not
already on your system, it will get downloaded. Essentially Chromium is a bare bones version of Chrome.
So let's just run that same example there, but let's do it without the proxy since we didn't give
it real proxy data. This is the raw footlocker sync example. So if we do Python raw footlocker sync.py,
you'll see it spun up a Chromium browser instead of regular Chrome. And the big difference here is
that with Chromium, there's basically more features supported than Chrome, because due to security
reasons, okay, first you can see all the data that came in. Due to security reasons, recently,
Chrome removed the load extension command line option in official branded Chrome builds,
starting with version 137 in order to improve security and stability. However, for people who do a
lot of automation, they might be using extensions as well. So this also prevented extensions from
loading from the command line when launching a regular Chrome browser. Now there are some tricky
workarounds, but the easiest one is essentially to use Chromium instead of Chrome, or the regular
base Chromium browser instead of Google Chrome. And then you still have the load extension command line
switch, which is what you need in order to load extensions. And since proxy is being set
via an extension, you'll want that in. However, if you're using regular Selenium base, proxy is also
able to be set when activating CDP mode, because then proxy is set via the Chrome DevTools protocol
instead of extension. And you'd have to change your script a little bit if you're using the
playwright version, such as here, because you'd have to load the URL before actually going to do
actions with playwright. So you wouldn't be able to use page.go2, you'd have to do like sp.open,
and then your URL. And then if you're using the proxy arg, so for instance, we weren't using
Chromium, if we had proxy equals user, colon, pass, IP, colon, port, then all of a sudden when you
open the URL, like that with Selenium base, then the proxy settings would take effect because Selenium
base would set those settings via the Chrome DevTools protocol. All right, so that is probably a lot
of information for you to digest today. For more details, you can check out the MDMins
undetected testing repo on GitHub, where I'm actually running these examples. And you can take a
look at the YAML file that's also there. And this will be the key to showing you how to do stealthy
web automation. There's also lots of docs on the playwright.dev website itself. And of course,
the Selenium base GitHub repo, which if you go to the stealthy playwright link,
you'll find the stealthy playwright mode documentation. And that will basically show you how to get
set up with running playwright in a very stealthy way. Additionally, there's also a discord server.
So if you do a search for playwright on discord, you'll actually get two results right now.
You'll have the regular playwright discord. And you'll have the Selenium base discord. Now that
there is a stealthy playwright mode there. So you basically go into the Selenium base discord.
You'll find a wide range of channels that you can go to. There's a stealthy playwright channel.
There is the CDP mode channel, etc. So there's lots of different ways to join the community
in order to get more information. And of course, the regular playwright python repo has examples
of using connect over CDP, which is the key to making playwright stealthy because you're going
to be connecting to a stealthy instance of playwright rather than launching the regular browser
that playwright provides, which isn't as stealthy. All right. Well, that concludes this tutorial.
I hope you have a great time automating. And I will see you all next time. See you later.

############################################################

