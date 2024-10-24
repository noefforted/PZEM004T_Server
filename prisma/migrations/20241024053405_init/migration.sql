-- CreateTable
CREATE TABLE "pzem_data" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "voltage" REAL NOT NULL,
    "current" REAL NOT NULL,
    "power" REAL NOT NULL,
    "energy" REAL NOT NULL,
    "frequency" REAL NOT NULL,
    "power_factor" REAL NOT NULL,
    "timestamp" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
