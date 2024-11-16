"use client";
import { Joystick } from "react-joystick-component";
import { IJoystickUpdateEvent } from "react-joystick-component/build/lib/Joystick";

function post(endpoint: string, data: Record<string, string | number>) {
  return fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}

function left() {
  post("/left", { direction: "left" });
}
function right() {
  post("/right", { direction: "right" });
}
function head() {
  post("/head", { direction: "head" });
}
function jiggly() {
  post("/jiggly", { direction: "jiggly" });
}

let isLock = false;
async function leg(event: IJoystickUpdateEvent) {
  const { x, y } = event;
  if (!(x && y)) return;
  if (isLock) return;
  isLock = true;
  const angle = Math.atan2(y, x) * (180 / Math.PI);
  await post("/leg", { angle });
  isLock = false;
}

export default function Page() {
  return (
    <>
      <div className="bg-gray-200 h-screen w-screen flex items-center font-mono">
        <div className="bg-gray-300 mx-auto p-5 rounded-full shadow-2xl border text-center">
          <h1 className="inline px-3 text-2xl text-center shadow-inner shadow-gray-400  text-gray-400 rounded-full">
            PuppiWi Controller
          </h1>
          <div className="flex justify-between items-center ">
            <div className="flex ">
              <div className="border shadow-inner shadow-gray-500 rounded-full w-32 h-32 m-5 flex justify-center items-center ">
                <Joystick
                  size={100}
                  baseColor=""
                  stickColor="rgb(156 163 175)"
                  move={leg}
                />
              </div>
            </div>
            <div className="flex ">
              <div className="flex flex-col justify-center">
                <button
                  onClick={left}
                  className="m-1 bg-green-500 w-20 h-20 text-2xl rounded-full text-gray-300 shadow-lg shadow-gray-400"
                >
                  L
                </button>
              </div>
              <div className="flex flex-col justify-center">
                <button
                  onClick={head}
                  className="m-1 bg-blue-500 w-20 h-20 text-2xl rounded-full text-gray-300 shadow-lg shadow-gray-400"
                >
                  H
                </button>
                <button
                  onClick={jiggly}
                  className="m-1 bg-yellow-500 w-20 h-20 text-2xl rounded-full text-gray-300 shadow-lg shadow-gray-400"
                >
                  N
                </button>
              </div>
              <div className="flex flex-col justify-center">
                <button
                  onClick={right}
                  className="m-1 bg-red-500 w-20 h-20 text-2xl rounded-full text-gray-300 shadow-lg shadow-gray-400"
                >
                  R
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
