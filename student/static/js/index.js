window.onload = ()=>{
    config.load_data();
	let d = new Date();
    let dayToday = d.getDay();
    defaultView(dayToday);
    showQuote();
 }

//  Load Timetable
let viewSchedule = document.querySelector('.view-schedule');
let dayArr = ['sun','mon','tue','wed','thu','fri','sat'];

const defaultView = (dayToday)=>{
    let loader = document.querySelector('.loader');
    viewSchedule.innerHTML = '';
    if(config.data){
        if(dayToday == 0){
            viewSchedule.innerHTML += `<h1 class="class-value showDisp">It's Sunday fellas! Enjoy</h1>`;
        }
        else{
            let dayView = config.data.timetable[dayToday - 1];
            let dayTab = document.querySelector(`.${dayArr[dayToday]}`);
            dayTab.classList.add('active');

            for(classObj of dayView.schedule){
                if(window.innerWidth >= 768){
                    viewSchedule.innerHTML +=
                        `<li class="class-list" style="color: white;">
                            <span class="class-value">${classObj.start}</span>
                            <span class="class-value">${classObj.end}</span>
                            <span class="class-value">${classObj.subject}</span>
                            <span class="class-value">${classObj.room}</span>
                        </li>`;
                }else{
                    viewSchedule.innerHTML +=
                        `<li class="class-list" style="color: white;">
                            <span class="class-value">${classObj.start} - ${classObj.end}</span>
                            <span class="class-value">${classObj.subject} (${classObj.room})</span>
                        </li>`;
                }
            }
        }
    }else{
        viewSchedule.innerHTML += 
        `<div class="class-value showDisp" onclick="setDefaultData()">No data available! Show default?</div>`
    }
    loader.style.display = 'none';
}

const setDefaultData = ()=>{
    config.set_data();
}

const loadView = (day)=>{
	viewSchedule.innerHTML = '';
    
    let currentDay = document.querySelector('.active');
    if(currentDay)
        currentDay.classList.remove('active');
    
    let showDay = document.querySelector(`.${day}`);
    showDay.classList.add('active');

	let dayView = config.data.timetable[dayArr.indexOf(day) - 1];
    for(classObj of dayView.schedule){
        if(window.innerWidth >= 768){
            viewSchedule.innerHTML +=
                `<li class="class-list" style="color: white;">
                    <span class="class-value">${classObj.start}</span>
                    <span class="class-value">${classObj.end}</span>
                    <span class="class-value">${classObj.subject}</span>
                    <span class="class-value">${classObj.room}</span>
                </li>`;
        }else{
            viewSchedule.innerHTML +=
                `<li class="class-list" style="color: white;">
                    <span class="class-value">${classObj.start} - ${classObj.end}</span>
                    <span class="class-value">${classObj.subject} (${classObj.room})</span>
                </li>`;
        }
    }
}

// Load Quote of the Day
const showQuote = async ()=>{
    let quote = document.querySelector('.quote')
    let quoteAuthor = document.querySelector('.quote-author')
    const res = await fetch('https://quotes.rest/qod')
    const resJSON = await res.json()
    quote.innerHTML = `"${resJSON.contents.quotes[0].quote}"`;
    quoteAuthor.innerHTML = "- "+resJSON.contents.quotes[0].author;
}