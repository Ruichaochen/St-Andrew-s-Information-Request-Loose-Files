people = {}
function getbounties()
fireproximityprompt(game:GetService("Workspace").BountyNPC.HumanoidRootPart.ProximityPrompt)
for i,v in pairs(game:GetService("Players").LocalPlayer.PlayerGui.HUD.BountysFrame.ListingsFrame.ScrollingFrame:GetChildren()) do
    if v.Name == "BountyListing" and v.NameLabel.Text ~= game.Players.LocalPlayer.DisplayName then
        table.insert(people,v.NameLabel.Text)
    end
end
for i,v2 in pairs(game.Players:GetPlayers()) do
    if table.find(people, v2.DisplayName) then
        people[table.find(people, v2.DisplayName)] = v2.Name
    end
end
return people
end
spawn(function()
    while task.wait(20) do
        getbounties()
    end
end)
for i,v3 in pairs(people) do
    local args = {
        [1] = "AcceptBounty",
        [2] = v3
    }
    game:GetService("ReplicatedStorage").Events.WeaponEvent:FireServer(unpack(args))

    repeat task.wait() game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Players[v3].Character.HumanoidRootPart.CFrame * CFrame.new(0, 0, 2) 
    local args = {
    [1] = "Swing"
    }
    
    game:GetService("ReplicatedStorage").Events.WeaponEvent:FireServer(unpack(args))
    until game.Players[v3].Character:FindFirstChild("ForceField")
    repeat task.wait(2)
    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Players[v3].Character.HumanoidRootPart.CFrame * CFrame.new(0, 2, 0)
    wait(1)
    local args = {
        [1] = "EPress"
    }
    
    game:GetService("ReplicatedStorage").Events.WeaponEvent:FireServer(unpack(args))
    until v3 == nil
end
getgenv().toggle = false
while getgenv().toggle and task.wait(0.1) do
game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Players["Phazzy1st"].Character.HumanoidRootPart.CFrame * CFrame.new(0, 0, 3)
end