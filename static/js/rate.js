let average_rating = document.querySelectorAll(".average_rating");
let star = document.querySelectorAll(".get_star");
// write a code get average rating and set stars
if (Math.round(average_rating[0].innerHTML) == 0) {
  for (let i = 0; i < 5; i++) {
    star[i].classList.add("fa-regular");
    star[i].classList.remove("fa");
  }
} else if (Math.round(average_rating[0].innerHTML) == 1) {
  for (let i = 0; i < 5; i++) {
    star[0].classList.add("fa-solid");
    star[1].classList.add("fa-regular");
    star[2].classList.add("fa-regular");
    star[3].classList.add("fa-regular");
    star[4].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[0].innerHTML) == 2) {
  for (let i = 0; i < 5; i++) {
    star[0].classList.add("fa-solid");
    star[1].classList.add("fa-solid");
    star[2].classList.add("fa-regular");
    star[3].classList.add("fa-regular");
    star[4].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[0].innerHTML) == 3) {
  for (let i = 0; i < 5; i++) {
    star[0].classList.add("fa-solid");
    star[1].classList.add("fa-solid");
    star[2].classList.add("fa-solid");
    star[3].classList.add("fa-regular");
    star[4].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[0].innerHTML) == 4) {
  for (let i = 0; i < 5; i++) {
    star[0].classList.add("fa-solid");
    star[1].classList.add("fa-solid");
    star[2].classList.add("fa-solid");
    star[3].classList.add("fa-solid");
    star[4].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[0].innerHTML) == 5) {
  for (let i = 0; i < 5; i++) {
    star[0].classList.add("fa-solid");
    star[1].classList.add("fa-solid");
    star[2].classList.add("fa-solid");
    star[3].classList.add("fa-solid");
    star[4].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[1].innerHTML) == 0) {
  for (let i = 0; i < 10; i++) {
    star[5].classList.add("fa-regular");
    star[6].classList.add("fa-regular");
    star[7].classList.add("fa-regular");
    star[8].classList.add("fa-regular");
    star[9].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[1].innerHTML) == 1) {
  for (let i = 0; i < 10; i++) {
    star[5].classList.add("fa-solid");
    star[6].classList.add("fa-regular");
    star[7].classList.add("fa-regular");
    star[8].classList.add("fa-regular");
    star[9].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[1].innerHTML) == 2) {
  for (let i = 0; i < 10; i++) {
    star[5].classList.add("fa-solid");
    star[6].classList.add("fa-solid");
    star[7].classList.add("fa-regular");
    star[8].classList.add("fa-regular");
    star[9].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[1].innerHTML) == 3) {
  for (let i = 0; i < 10; i++) {
    star[5].classList.add("fa-solid");
    star[6].classList.add("fa-solid");
    star[7].classList.add("fa-solid");
    star[8].classList.add("fa-regular");
    star[9].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[1].innerHTML) == 4) {
  for (let i = 0; i < 10; i++) {
    star[5].classList.add("fa-solid");
    star[6].classList.add("fa-solid");
    star[7].classList.add("fa-solid");
    star[8].classList.add("fa-solid");
    star[9].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[1].innerHTML) == 5) {
  for (let i = 0; i < 10; i++) {
    star[5].classList.add("fa-solid");
    star[6].classList.add("fa-solid");
    star[7].classList.add("fa-solid");
    star[8].classList.add("fa-solid");
    star[9].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[2].innerHTML) == 0) {
  for (let i = 0; i < 15; i++) {
    star[10].classList.add("fa-regular");
    star[11].classList.add("fa-regular");
    star[12].classList.add("fa-regular");
    star[13].classList.add("fa-regular");
    star[14].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[2].innerHTML) == 1) {
  for (let i = 0; i < 15; i++) {
    star[10].classList.add("fa-solid");
    star[11].classList.add("fa-regular");
    star[12].classList.add("fa-regular");
    star[13].classList.add("fa-regular");
    star[14].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[2].innerHTML) == 2) {
  for (let i = 0; i < 15; i++) {
    star[10].classList.add("fa-solid");
    star[11].classList.add("fa-solid");
    star[12].classList.add("fa-regular");
    star[13].classList.add("fa-regular");
    star[14].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[2].innerHTML) == 3) {
  for (let i = 0; i < 15; i++) {
    star[10].classList.add("fa-solid");
    star[11].classList.add("fa-solid");
    star[12].classList.add("fa-solid");
    star[13].classList.add("fa-regular");
    star[14].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[2].innerHTML) == 4) {
  for (let i = 0; i < 15; i++) {
    star[10].classList.add("fa-solid");
    star[11].classList.add("fa-solid");
    star[12].classList.add("fa-solid");
    star[13].classList.add("fa-solid");
    star[14].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[2].innerHTML) == 5) {
  for (let i = 0; i < 15; i++) {
    star[10].classList.add("fa-solid");
    star[11].classList.add("fa-solid");
    star[12].classList.add("fa-solid");
    star[13].classList.add("fa-solid");
    star[14].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[3].innerHTML) == 0) {
  for (let i = 0; i < 20; i++) {
    star[15].classList.add("fa-regular");
    star[16].classList.add("fa-regular");
    star[17].classList.add("fa-regular");
    star[18].classList.add("fa-regular");
    star[19].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[3].innerHTML) == 1) {
  for (let i = 0; i < 20; i++) {
    star[15].classList.add("fa-solid");
    star[16].classList.add("fa-regular");
    star[17].classList.add("fa-regular");
    star[18].classList.add("fa-regular");
    star[19].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[3].innerHTML) == 2) {
  for (let i = 0; i < 20; i++) {
    star[15].classList.add("fa-solid");
    star[16].classList.add("fa-solid");
    star[17].classList.add("fa-regular");
    star[18].classList.add("fa-regular");
    star[19].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[3].innerHTML) == 3) {
  for (let i = 0; i < 20; i++) {
    star[15].classList.add("fa-solid");
    star[16].classList.add("fa-solid");
    star[17].classList.add("fa-solid");
    star[18].classList.add("fa-regular");
    star[19].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[3].innerHTML) == 4) {
  for (let i = 0; i < 20; i++) {
    star[15].classList.add("fa-solid");
    star[16].classList.add("fa-solid");
    star[17].classList.add("fa-solid");
    star[18].classList.add("fa-solid");
    star[19].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[3].innerHTML) == 5) {
  for (let i = 0; i < 20; i++) {
    star[15].classList.add("fa-solid");
    star[16].classList.add("fa-solid");
    star[17].classList.add("fa-solid");
    star[18].classList.add("fa-solid");
    star[19].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[4].innerHTML) == 0) {
  for (let i = 0; i < 25; i++) {
    star[20].classList.add("fa-regular");
    star[21].classList.add("fa-regular");
    star[22].classList.add("fa-regular");
    star[23].classList.add("fa-regular");
    star[24].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[4].innerHTML) == 1) {
  for (let i = 0; i < 25; i++) {
    star[20].classList.add("fa-solid");
    star[21].classList.add("fa-regular");
    star[22].classList.add("fa-regular");
    star[23].classList.add("fa-regular");
    star[24].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[4].innerHTML) == 2) {
  for (let i = 0; i < 25; i++) {
    star[20].classList.add("fa-solid");
    star[21].classList.add("fa-solid");
    star[22].classList.add("fa-regular");
    star[23].classList.add("fa-regular");
    star[24].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[4].innerHTML) == 3) {
  for (let i = 0; i < 25; i++) {
    star[20].classList.add("fa-solid");
    star[21].classList.add("fa-solid");
    star[22].classList.add("fa-solid");
    star[23].classList.add("fa-regular");
    star[24].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[4].innerHTML) == 4) {
  for (let i = 0; i < 25; i++) {
    star[20].classList.add("fa-solid");
    star[21].classList.add("fa-solid");
    star[22].classList.add("fa-solid");
    star[23].classList.add("fa-solid");
    star[24].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[4].innerHTML) == 5) {
  for (let i = 0; i < 25; i++) {
    star[20].classList.add("fa-solid");
    star[21].classList.add("fa-solid");
    star[22].classList.add("fa-solid");
    star[23].classList.add("fa-solid");
    star[24].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[5].innerHTML) == 0) {
  for (let i = 0; i < 30; i++) {
    star[25].classList.add("fa-regular");
    star[26].classList.add("fa-regular");
    star[27].classList.add("fa-regular");
    star[28].classList.add("fa-regular");
    star[29].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[5].innerHTML) == 1) {
  for (let i = 0; i < 30; i++) {
    star[25].classList.add("fa-solid");
    star[26].classList.add("fa-regular");
    star[27].classList.add("fa-regular");
    star[28].classList.add("fa-regular");
    star[29].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[5].innerHTML) == 2) {
  for (let i = 0; i < 30; i++) {
    star[25].classList.add("fa-solid");
    star[26].classList.add("fa-solid");
    star[27].classList.add("fa-regular");
    star[28].classList.add("fa-regular");
    star[29].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[5].innerHTML) == 3) {
  for (let i = 0; i < 30; i++) {
    star[25].classList.add("fa-solid");
    star[26].classList.add("fa-solid");
    star[27].classList.add("fa-solid");
    star[28].classList.add("fa-regular");
    star[29].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[5].innerHTML) == 4) {
  for (let i = 0; i < 30; i++) {
    star[25].classList.add("fa-solid");
    star[26].classList.add("fa-solid");
    star[27].classList.add("fa-solid");
    star[28].classList.add("fa-solid");
    star[29].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[5].innerHTML) == 5) {
  for (let i = 0; i < 30; i++) {
    star[25].classList.add("fa-solid");
    star[26].classList.add("fa-solid");
    star[27].classList.add("fa-solid");
    star[28].classList.add("fa-solid");
    star[29].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[6].innerHTML) == 0) {
  for (let i = 0; i < 35; i++) {
    star[30].classList.add("fa-regular");
    star[31].classList.add("fa-regular");
    star[32].classList.add("fa-regular");
    star[33].classList.add("fa-regular");
    star[34].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[6].innerHTML) == 1) {
  for (let i = 0; i < 35; i++) {
    star[30].classList.add("fa-solid");
    star[31].classList.add("fa-regular");
    star[32].classList.add("fa-regular");
    star[33].classList.add("fa-regular");
    star[34].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[6].innerHTML) == 2) {
  for (let i = 0; i < 35; i++) {
    star[30].classList.add("fa-solid");
    star[31].classList.add("fa-solid");
    star[32].classList.add("fa-regular");
    star[33].classList.add("fa-regular");
    star[34].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[6].innerHTML) == 3) {
  for (let i = 0; i < 35; i++) {
    star[30].classList.add("fa-solid");
    star[31].classList.add("fa-solid");
    star[32].classList.add("fa-solid");
    star[33].classList.add("fa-regular");
    star[34].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[6].innerHTML) == 4) {
  for (let i = 0; i < 35; i++) {
    star[30].classList.add("fa-solid");
    star[31].classList.add("fa-solid");
    star[32].classList.add("fa-solid");
    star[33].classList.add("fa-solid");
    star[34].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[6].innerHTML) == 5) {
  for (let i = 0; i < 35; i++) {
    star[30].classList.add("fa-solid");
    star[31].classList.add("fa-solid");
    star[32].classList.add("fa-solid");
    star[33].classList.add("fa-solid");
    star[34].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[7].innerHTML) == 0) {
  for (let i = 0; i < 40; i++) {
    star[35].classList.add("fa-regular");
    star[36].classList.add("fa-regular");
    star[37].classList.add("fa-regular");
    star[38].classList.add("fa-regular");
    star[39].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[7].innerHTML) == 1) {
  for (let i = 0; i < 40; i++) {
    star[35].classList.add("fa-solid");
    star[36].classList.add("fa-regular");
    star[37].classList.add("fa-regular");
    star[38].classList.add("fa-regular");
    star[39].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[7].innerHTML) == 2) {
  for (let i = 0; i < 40; i++) {
    star[35].classList.add("fa-solid");
    star[36].classList.add("fa-solid");
    star[37].classList.add("fa-regular");
    star[38].classList.add("fa-regular");
    star[39].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[7].innerHTML) == 3) {
  for (let i = 0; i < 40; i++) {
    star[35].classList.add("fa-solid");
    star[36].classList.add("fa-solid");
    star[37].classList.add("fa-solid");
    star[38].classList.add("fa-regular");
    star[39].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[7].innerHTML) == 4) {
  for (let i = 0; i < 40; i++) {
    star[35].classList.add("fa-solid");
    star[36].classList.add("fa-solid");
    star[37].classList.add("fa-solid");
    star[38].classList.add("fa-solid");
    star[39].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[7].innerHTML) == 5) {
  for (let i = 0; i < 40; i++) {
    star[35].classList.add("fa-solid");
    star[36].classList.add("fa-solid");
    star[37].classList.add("fa-solid");
    star[38].classList.add("fa-solid");
    star[39].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[8].innerHTML) == 0) {
  for (let i = 0; i < 45; i++) {
    star[40].classList.add("fa-regular");
    star[41].classList.add("fa-regular");
    star[42].classList.add("fa-regular");
    star[43].classList.add("fa-regular");
    star[44].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[8].innerHTML) == 1) {
  for (let i = 0; i < 45; i++) {
    star[40].classList.add("fa-solid");
    star[41].classList.add("fa-regular");
    star[42].classList.add("fa-regular");
    star[43].classList.add("fa-regular");
    star[44].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[8].innerHTML) == 2) {
  for (let i = 0; i < 45; i++) {
    star[40].classList.add("fa-solid");
    star[41].classList.add("fa-solid");
    star[42].classList.add("fa-regular");
    star[43].classList.add("fa-regular");
    star[44].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[8].innerHTML) == 3) {
  for (let i = 0; i < 45; i++) {
    star[40].classList.add("fa-solid");
    star[41].classList.add("fa-solid");
    star[42].classList.add("fa-solid");
    star[43].classList.add("fa-regular");
    star[44].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[8].innerHTML) == 4) {
  for (let i = 0; i < 45; i++) {
    star[40].classList.add("fa-solid");
    star[41].classList.add("fa-solid");
    star[42].classList.add("fa-solid");
    star[43].classList.add("fa-solid");
    star[44].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[8].innerHTML) == 5) {
  for (let i = 0; i < 45; i++) {
    star[40].classList.add("fa-solid");
    star[41].classList.add("fa-solid");
    star[42].classList.add("fa-solid");
    star[43].classList.add("fa-solid");
    star[44].classList.add("fa-solid");
  }
}
if (Math.round(average_rating[9].innerHTML) == 0) {
  for (let i = 0; i < 50; i++) {
    star[45].classList.add("fa-regular");
    star[46].classList.add("fa-regular");
    star[47].classList.add("fa-regular");
    star[48].classList.add("fa-regular");
    star[49].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[9].innerHTML) == 1) {
  for (let i = 0; i < 50; i++) {
    star[45].classList.add("fa-solid");
    star[46].classList.add("fa-regular");
    star[47].classList.add("fa-regular");
    star[48].classList.add("fa-regular");
    star[49].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[9].innerHTML) == 2) {
  for (let i = 0; i < 50; i++) {
    star[45].classList.add("fa-solid");
    star[46].classList.add("fa-solid");
    star[47].classList.add("fa-regular");
    star[48].classList.add("fa-regular");
    star[49].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[9].innerHTML) == 3) {
  for (let i = 0; i < 50; i++) {
    star[45].classList.add("fa-solid");
    star[46].classList.add("fa-solid");
    star[47].classList.add("fa-solid");
    star[48].classList.add("fa-regular");
    star[49].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[9].innerHTML) == 4) {
  for (let i = 0; i < 50; i++) {
    star[45].classList.add("fa-solid");
    star[46].classList.add("fa-solid");
    star[47].classList.add("fa-solid");
    star[48].classList.add("fa-solid");
    star[49].classList.add("fa-regular");
  }
} else if (Math.round(average_rating[9].innerHTML) == 5) {
  for (let i = 0; i < 50; i++) {
    star[45].classList.add("fa-solid");
    star[46].classList.add("fa-solid");
    star[47].classList.add("fa-solid");
    star[48].classList.add("fa-solid");
    star[49].classList.add("fa-solid");
  }
}
