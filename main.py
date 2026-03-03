@myaniawd:@ii1_8: import { system, world } from "@minecraft/server";
// Config
const CHECK_INTERVAL = 20;
const MAX_DISTANCE = 48;
const UPDATE_INTERVAL = 40;
let entityLastUpdate = new Map();
system.runInterval(function () {
const players = world.getPlayers();
for (let p = 0; p MAX_DISTANCE) {
try {
entity.remove();
} catch (e) {}
continue;
}
const now = system.currentTick;
// بديل آمن بدون ??
let key;
if (entity.id) {
key = entity.id;
} else {
key = entity;
}
let lastUpdate;
if (entityLastUpdate.has(key)) {
lastUpdate = entityLastUpdate.get(key);
} else {
lastUpdate = 0;
}
if (dist > MAX_DISTANCE / 2) {
if ((now - lastUpdate) < UPDATE_INTERVAL) {
continue;
}
}
entityLastUpdate.set(key, now);
try {
if (entity.hasComponent("minecraft:is_baby")) {
// optional
}
} catch (e) {}
}
}
}, CHECK_INTERVAL);
