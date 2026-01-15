spawn(function()
while task.wait() do
    if game.Players.LocalPlayer.Character ~= nil then
        pathtofind = game.Players.LocalPlayer.Character.Parent
    end
end
end)
local UIS = game:GetService("UserInputService")
local camera = game.Workspace.CurrentCamera
function getClosest()
local closestPlayer = nil
local closesDist = math.huge
for i,v in pairs(pathtofind:GetChildren()) do
    if v ~= game:GetService("Players").LocalPlayer.Character and v.Name == "R15Rig" then
local Dist = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - v.HumanoidRootPart.Position).magnitude
if Dist < closesDist then
closesDist = Dist
closestPlayer = v
end
end
end
print(closestPlayer)
return closestPlayer
end
_G.aim = false
UIS.InputBegan:Connect(function(inp)
    if inp.UserInputType == Enum.UserInputType.MouseButton2 then
    _G.aim = true
    while task.wait() do
        camera.CFrame = CFrame.new(camera.CFrame.Position,getClosest().Head.Position)
        if _G.aim == false then return end
    end
    end
end)
--> ending the aimbot
UIS.InputEnded:Connect(function(inp)
    if inp.UserInputType == Enum.UserInputType.MouseButton2 then
    _G.aim = false
    end
end)