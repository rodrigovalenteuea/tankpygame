# collision bullet with tank
            i = 0
            j = 0
            while i < len(vet_tanks):
                j = 0
                while j < len(vet_tanks[i].bullets):
                    if vet_tanks[i].rect.colliderect():
                        vet_tanks[i].bullets[j].rect.x = -40
                        vet_tanks[i].bullets.pop(j)
                        i -= 1
                    elif vet_tanks[i].bullets[j].rect.x < 0:
                        vet_tanks[i].bullets[j].rect.x = -40
                        vet_tanks[i].bullets.pop(j)
                        i -= 1
                    elif vet_tanks[i].bullets[j].rect.y + vet_tanks[i].bullets[j].rect.height > altura:
                        vet_tanks[i].bullets[j].rect.y = -40
                        vet_tanks[i].bullets.pop(j)
                        i -= 1
                    elif vet_tanks[i].bullets[j].rect.y < 0:
                        vet_tanks[i].bullets[j].rect.y = -40
                        vet_tanks[i].bullets.pop(j)
                        i -= 1
                    j += 1
                i += 1