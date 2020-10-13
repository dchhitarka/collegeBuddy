// import {saveTimetableApi} from './api.js';

const showTimetable = (timetable, day) => {
    let viewSched = document.querySelector('.view-schedule');
    viewSched.innerHTML = '';
    if(timetable.length == 0) {
        viewSched.innerHTML += `<h1 class="showDisp">No Timetable available!</h1>`
        document.querySelector('.week').innerHTML = '';
    }
    else{
        document.querySelector('.active')?.classList.remove('active');
        document.querySelectorAll('.weekday')[day].classList.add('active');
        const dayView = timetable[day];
        if(dayView.subjects.length == 0){
            viewSched.innerHTML += `<h1 class="showDisp">Nothing to show here :)</h1>`;  
        } 
        else{
            for(classObj of dayView.subjects){
                viewSched.innerHTML += 
                        `<li class="class-list" style="color: white;">
                            <span class="class-value">${classObj.subject}</span>
                            <span class="class-value">${classObj.from} - ${classObj.to}</span>
                        </li>`;
            }
        }
    }
}

const saveTimetable = (timetable) => {
    let oldSched = timetable[document.querySelector(`#dayname`).value]
    let newSched = document.querySelectorAll('.task');
    let newData = [];
    newSched.forEach(task => {
        let sub = [...task.childNodes].filter(child => child.nodeType == Node.ELEMENT_NODE)
        newData.push({"subject": sub[0].value, "from": sub[1].value, "to": sub[2].value})
    });
    timetable[document.querySelector(`#dayname`).value].subjects = newData;
    console.log(timetable);
    saveTimetableApi(timetable);
}

const editTimetable = (timetable, day) => {
    let viewSched = document.querySelector('.show-list');
    viewSched.innerHTML = "";
    const dayView = timetable[day];
    if(dayView.subjects.length == 0){
        viewSched.innerHTML +=                 
        `<li class="task">
            <input type="text" class="taskValue" value="" size="15"/>
            <input type="time" class="taskValue" value="" size="5" />
            <input type="time" class="taskValue" value="" size="5" />
        </li>`;
    } 
    else{
        for(classObj of dayView.subjects){
            viewSched.innerHTML +=
                `<li class="task">
                    <input type="text" class="taskValue" value="${classObj.subject}" size="15"/>
                    <input type="time" class="taskValue" value="${classObj.from}" size="5" />
                    <input type="time" class="taskValue" value="${classObj.to}" size="5" />
                </li>`
        }
    }
}

const addSub = () => {
    let viewSched = document.querySelector('.show-list');
    viewSched.innerHTML +=
                `<li class="task">
                    <input type="text" class="taskValue" value="Subject" size="15"/>
                    <input type="time" class="taskValue" value="00:00" size="5" />
                    <input type="time" class="taskValue" value="00:00" size="5" />
                </li>`
}

const deleteLast = () => {
    let viewSched = document.querySelector('.show-list');
    let lastChild = document.querySelectorAll('.task');
    if(lastChild.length > 0)
        viewSched.removeChild(lastChild[lastChild.length - 1]);
    else
        alert("Cannot delete empty schedule")
}