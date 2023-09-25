-- CreateTable
CREATE TABLE "calender" (
    "id" SERIAL NOT NULL,
    "task_name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "calender_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "calender_email_key" ON "calender"("email");
