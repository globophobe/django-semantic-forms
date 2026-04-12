/*global gettext, interpolate, ngettext*/
"use strict";

const days = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const shortDays = ["S", "M", "T", "W", "T", "F", "S"];
const shortMonths = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

function hasCalendarTranslations(hasJavascriptCatalog) {
  return (
    hasJavascriptCatalog &&
    typeof gettext === "function" &&
    typeof pgettext === "function"
  );
}

function getDefaultCalendarText() {
  return {
    days: shortDays,
    months: months,
    monthsShort: shortMonths,
    today: "Today",
    now: "Now",
  };
}

function getCalendarText(hasJavascriptCatalog) {
  if (!hasCalendarTranslations(hasJavascriptCatalog)) {
    return getDefaultCalendarText();
  }

  return {
    days: shortDays.map(function (oneLetterDay, index) {
      const day = days[index];
      return pgettext(`one letter ${day}`, oneLetterDay);
    }),
    months: months.map(function (month) {
      return gettext(month);
    }),
    monthsShort: shortMonths.map(function (monthShort, index) {
      const monthLong = months[index];
      return pgettext(`abbrev. month ${monthLong}`, monthShort);
    }),
    today: gettext("Today"),
    now: gettext("Now"),
  };
}

function getCalendarOptions(type, hasJavascriptCatalog) {
  return {
    type,
    formatter: {
      date: function (date, _settings) {
        if (!date) return "";
        const year = date.getFullYear();
        const month = ("0" + (date.getMonth() + 1)).slice(-2);
        const day = ("0" + date.getDate()).slice(-2);
        return year + "-" + month + "-" + day;
      },
    },
    ampm: false,
    text: getCalendarText(hasJavascriptCatalog),
  };
}
