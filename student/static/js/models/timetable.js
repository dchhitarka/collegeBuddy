class TimeTable{
    day = null;
    subjects = []

    constructor(timetable){
        this.day = timetable?.day ?? null;
        this.subjects = timetable?.subjects ?? [];
    }
}

export default TimeTable;