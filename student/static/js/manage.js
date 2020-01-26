window.onload = function() {
    config.load_data();
    let d = new Date();
    let dayToday = d.getDay();
    default_schedule(dayToday);
};

let count = 0; //For counting number of times add bi=utton was clicked

const default_schedule = (dayToday)=>{
    let manage = document.querySelector('.show-list');
    manage.innerHTML = '';
    if(dayToday == 0){
        let optionDay = document.querySelector('.monday')
        optionDay.setAttribute('selected', true);
        let dayObj = config.data.timetable[dayToday];
        console.log(dayObj);
        for(classObj of dayObj.schedule){
            manage.innerHTML +=
                `<li class="manage task">
                    <input type="time" class="taskValue" value="${classObj.start}" size="5" />
                    <input type="time" class="taskValue" value="${classObj.end}" size="5" />
                    <input type="text" class="taskValue" value="${classObj.subject}" size="15"/>
                    <input type="text" class="taskValue" value="${classObj.room}" size="5"/>
                </li>`
        }
    } else {
        let dayObj = config.data.timetable[dayToday-1];
        let optionDay = document.querySelector(`[value="${dayToday-1}"]`);
        optionDay.setAttribute('selected', true);
        for(classObj of dayObj.schedule){
            manage.innerHTML +=
                `<li class="manage task">
                    <input type="time" class="taskValue" value="${classObj.start}" size="5" />
                    <input type="time" class="taskValue" value="${classObj.end}" size="5" />
                    <input type="text" class="taskValue" value="${classObj.subject}" size="15"/>
                    <input type="text" class="taskValue" value="${classObj.room}" size="5"/>
                </li>`
        }
    }
}

const show_schedule = ()=>{
    let manage = document.querySelector('.show-list');
    manage.innerHTML = '';
    let selectday = document.querySelector('#dayname');
    
    let dayIndex = selectday.options.selectedIndex - 1;

    let dayObj = config.data.timetable[dayIndex];
    
    for(classObj of dayObj.schedule){
        manage.innerHTML +=
            `<li class="manage task">
                <input type="time" class="taskValue" value="${classObj.start}" size="5" />
                <input type="time" class="taskValue" value="${classObj.end}" size="5" />
                <input type="text" class="taskValue" value="${classObj.subject}" size="15"/>
                <input type="text" class="taskValue" value="${classObj.room}" size="5"/>
            </li>`
    }
}

const addNew = () => {
    count++;
    let manage = document.querySelector('.show-list');
    manage.innerHTML +=
            `<li class="manage task">
                <input type="time" class="taskValue" value="" size="5" />
                <input type="time" class="taskValue" value="" size="5" />
                <input type="text" class="taskValue" value="" placeholder="Subject" size="15"/>
                <input type="text" class="taskValue" value="" placeholder="Room No." size="5"/>
            </li>`
}

const deleteThis = ()=>{
    let manage = document.querySelector('.show-list');
    manage.removeChild(manage.lastChild)
}
const save_schedule = () => {
    let newValues = document.querySelectorAll('.taskValue');
    let selectday = document.querySelector('#dayname');
    let dayIndex = selectday.options.selectedIndex - 1;
    let scheduleData = config.data;
    let newSchedule = []
    let newData = {}
    for(let i = 0; i < newValues.length; i += 4){
        newData.start = newValues[i].value
        newData.end = newValues[i+1].value
        newData.subject = newValues[i+2].value
        newData.room = newValues[i+3].value
        newSchedule.push(newData) 
        newData = {}      
    }
    
    scheduleData.timetable[dayIndex].schedule = newSchedule;    
    config.save_data(scheduleData);
}

