spawn(function()
while task.wait(1) do
    local nearest = function()
    local plrs = game:service("Players")
    for k,l in pairs(plrs:GetPlayers()) do
    local pos = v.Character:GetPrimaryPartCFrame().p
    local len = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - v.Character.HumanoidRootPart.Position).Magnitude
    plr = l
    dist = len
    end
    return plr.Character:GetPrimaryPartCFrame().p
    end
    pcall(function()
for i,v in pairs(game:GetService'Players':GetPlayers()) do
  if v.Name ~= game:GetService'Players'.LocalPlayer.Name then
      repeat
    local args = {
    [1] = "throw",
    [2] = CFrame.new(nearest())
    }
    game:GetService("ReplicatedStorage").forhackers:InvokeServer(unpack(args))
          wait(0.15)
      until v.Character.Humanoid.Health == 0
  end
end
workspace.CurrentCamera.trash.ChildAdded:connect(function(c)
c.CFrame = CFrame.new(nearest())
end)
end)
end
for i,bagss in pairs(game:GetService("Workspace").bags:GetChildren()) do
    bagss.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
end
local plrs = game:service("Players")
local ms = plrs.LocalPlayer:GetMouse()
local nearest = function()
local plr,dist = nil,math.huge
for k,l in pairs(plrs:GetPlayers()) do
local pos = l.Character:GetPrimaryPartCFrame().p
local len = (ms.Hit.p - pos).Magnitude
if len <= dist then
plr = l
dist = len
end
end
return plr.Character:GetPrimaryPartCFrame().p
end
workspace.CurrentCamera.trash.ChildAdded:connect(function(c)
c.CFrame = CFrame.new(nearest())
end)
end)