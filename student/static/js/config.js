var config = {
	
	set_data: function() {
		localStorage.setItem('config_data', JSON.stringify(config.defaultData))
		alert('Default Data set! Refresh the page to see the timetable.')
	},

	load_data: function() {
		data = localStorage.getItem("config_data");
		if (data != null) {
			try {
				config.data = JSON.parse(data);
			}
			catch (SyntaxError) {
				alert("Error: Wrong data structure!");
			}
		}
		// return JSON.parse(data);
	},

	save_data: function(new_data) {
		localStorage.setItem("config_data", JSON.stringify(new_data));
		config.data = JSON.parse(localStorage.getItem("config_data"));
		// console.log(config.data)
	},

	reset_data: function() {
		localStorage.removeItem("config_data");
	},

	defaultData: {
	   timetable:[
	      {
	         "day":"Monday",
	         "schedule":[
	            {
	               "start":"08:30",
	               "end":"09:30",
	               "subject":"Open Elective",
	               "room":"LT - 4"
	            },
	            {
	               "start":"09:30",
	               "end":"10:30",
	               "subject":"OOAD",
	               "room":"LT - 4"
	            },
	            {
	               "start":"10:30",
	               "end":"11:30",
	               "subject":"AI",
	               "room":"LT - 4"
	            },
	            {
	               "start":"11:30",
	               "end":"12:30",
	               "subject":"FLAT",
	               "room":"LT - 4"
	            },
	            {
	               "start":"13:30",
	               "end":"14:25",
	               "subject":"Project C1",
	               "room":"LT - 4"
	            },
	            {
	               "start":"14:25",
	               "end":"15:20",
	               "subject":"FLAT Tut C1",
	               "room":"LT - 4"
	            }
	         ]
	      },
	      {
	         "day":"Tuesday",
	         "schedule":[
	            {
	               "start":"08:30",
	               "end":"09:30",
	               "subject":"Open Elective",
	               "room":"LT - 4"
	            },
	            {
	               "start":"09:30",
	               "end":"10:30",
	               "subject":"Seminar",
	               "room":"LT - 4"
	            },
	            {
	               "start":"10:30",
	               "end":"11:30",
	               "subject":"MM",
	               "room":"LT - 32"
	            },
	            {
	               "start":"11:30",
	               "end":"12:30",
	               "subject":"FLAT",
	               "room":"LT - 4"
	            },
	            {
	               "start":"13:30",
	               "end":"14:25",
	               "subject":"Java",
	               "room":"LT - 4"
	            },
	            {
	               "start":"14:25",
	               "end":"15:20",
	               "subject":"AI",
	               "room":"LT - 32"
	            }
	         ]
	      },
	      {
	         "day":"Wednesday",
	         "schedule":[
	            {
	               "start":"08:30",
	               "end":"10:30",
	               "subject":"Java Lab",
	               "room":"Lab - 8"
	            },
	            {
	               "start":"10:30",
	               "end":"11:30",
	               "subject":"FLAT",
	               "room":"LT - 4"
	            },
	            {
	               "start":"11:30",
	               "end":"00:30",
	               "subject":"Java",
	               "room":"LT - 4"
	            },
	            {
	               "start":"13:30",
	               "end":"14:25",
	               "subject":"MM",
	               "room":"LT - 15"
	            }
	         ]
	      },
	      {
	         "day":"Thursday",
	         "schedule":[
	            {
	               "start":"09:30",
	               "end":"10:30",
	               "subject":"Java",
	               "room":"LT - 4"
	            },
	            {
	               "start":"10:30",
	               "end":"11:30",
	               "subject":"MM",
	               "room":"LT - 32"
	            },
	            {
	               "start":"14:25",
	               "end":"15:20",
	               "subject":"AI",
	               "room":"LT - 32"
	            }
	         ]
	      },
	      {
	         "day":"Friday",
	         "schedule":[
	            {
	               "start":"08:30",
	               "end":"10:30",
	               "subject":"WT Lab",
	               "room":"Lab - 7 "
	            },
	            {
	               "start":"10:30",
	               "end":"11:30",
	               "subject":"MM",
	               "room":"LT - 32"
	            },
	            {
	               "start":"13:30",
	               "end":"14:25",
	               "subject":"OOAD",
	               "room":"LT - 32"
	            }
	         ]
	      },
	      {
	         "day":"Saturday",
	         "schedule":[
	            {
	               "start":"09:30",
	               "end":"10:30",
	               "subject":"Java",
	               "room":"LT - 4"
	            },
	            {
	               "start":"13:30",
	               "end":"15:20",
	               "subject":"OOAD Lab",
	               "room":"Lab - 9"
	            }
	         ]
	      }
	   ],
	} // defaultData Object

} //Config Object

