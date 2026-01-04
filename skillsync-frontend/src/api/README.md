# SkillSync API Documentation

This is a **mock backend** using localStorage that simulates real API behavior. All APIs are designed to be easily swapped with real Django endpoints.

## API Structure

```
src/api/
├── index.ts          # Central exports
├── authApi.ts        # Authentication (login, register, logout, tokens)
├── dataApi.ts        # Skills & Projects CRUD
├── userApi.ts        # User profile management
├── settingsApi.ts    # User settings & notifications config
├── notificationsApi.ts # In-app notifications
└── dashboardApi.ts   # Dashboard statistics & activity
```

## Available Endpoints

### Authentication (`authApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| POST | `login()` | `/api/auth/login/` | User login |
| POST | `register()` | `/api/auth/register/` | User registration |
| POST | `logout()` | `/api/auth/logout/` | User logout |
| GET | `getCurrentUser()` | `/api/auth/me/` | Get current user |
| POST | `refreshToken()` | `/api/auth/token/refresh/` | Refresh access token |
| POST | `requestPasswordReset()` | `/api/auth/password/reset/` | Request password reset |
| POST | `resetPassword()` | `/api/auth/password/reset/confirm/` | Reset password with token |

### Skills (`skillsApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| GET | `getAll()` | `/api/skills/` | Get all skills |
| GET | `getById(id)` | `/api/skills/:id/` | Get skill by ID |
| POST | `create(data)` | `/api/skills/` | Create new skill |
| PUT | `update(id, data)` | `/api/skills/:id/` | Update skill |
| DELETE | `delete(id)` | `/api/skills/:id/` | Delete skill |

### Projects (`projectsApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| GET | `getAll()` | `/api/projects/` | Get all projects |
| GET | `getById(id)` | `/api/projects/:id/` | Get project by ID |
| POST | `create(data)` | `/api/projects/` | Create new project |
| PUT | `update(id, data)` | `/api/projects/:id/` | Update project |
| DELETE | `delete(id)` | `/api/projects/:id/` | Delete project |
| PATCH | `toggleMilestone(projectId, milestoneId)` | `/api/projects/:id/milestones/:milestoneId/` | Toggle milestone |

### User Profile (`userApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| GET | `getProfile(userId)` | `/api/users/:id/` | Get user profile |
| PUT | `updateProfile(userId, data)` | `/api/users/:id/` | Update profile |
| POST | `changePassword(userId, data)` | `/api/users/:id/change-password/` | Change password |
| POST | `uploadAvatar(userId, file)` | `/api/users/:id/avatar/` | Upload avatar |
| DELETE | `deleteAccount(userId)` | `/api/users/:id/` | Delete account |
| GET | `getStats(userId)` | `/api/users/:id/stats/` | Get user statistics |

### Settings (`settingsApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| GET | `getNotificationSettings()` | `/api/settings/notifications/` | Get notification prefs |
| PUT | `updateNotificationSettings(data)` | `/api/settings/notifications/` | Update notification prefs |
| GET | `getUserSettings()` | `/api/settings/` | Get user settings |
| PUT | `updateUserSettings(data)` | `/api/settings/` | Update user settings |
| POST | `enableTwoFactor()` | `/api/settings/2fa/enable/` | Enable 2FA |
| POST | `disableTwoFactor(code)` | `/api/settings/2fa/disable/` | Disable 2FA |
| GET | `exportUserData()` | `/api/settings/export/` | Export user data (GDPR) |

### Notifications (`notificationsApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| GET | `getAll()` | `/api/notifications/` | Get all notifications |
| GET | `getUnreadCount()` | `/api/notifications/unread-count/` | Get unread count |
| PATCH | `markAsRead(id)` | `/api/notifications/:id/read/` | Mark as read |
| POST | `markAllAsRead()` | `/api/notifications/mark-all-read/` | Mark all as read |
| DELETE | `delete(id)` | `/api/notifications/:id/` | Delete notification |
| DELETE | `clearAll()` | `/api/notifications/` | Clear all notifications |

### Dashboard (`dashboardApi`)
| Method | Mock Endpoint | Django Endpoint | Description |
|--------|--------------|-----------------|-------------|
| GET | `getStats()` | `/api/dashboard/stats/` | Get dashboard stats |
| GET | `getRecentActivity(limit)` | `/api/dashboard/activity/` | Get recent activity |
| GET | `getProgress()` | `/api/dashboard/progress/` | Get progress overview |

## Usage Example

```typescript
import { authApi, skillsApi, userApi } from '@/api';

// Login
const { data } = await authApi.login({ email: 'demo@skillsync.com', password: 'password' });

// Create a skill
const { data: skill } = await skillsApi.create({
  name: 'Vue.js',
  category: 'frontend',
  proficiency: 'intermediate',
  yearsOfExperience: 1
});

// Update profile
await userApi.updateProfile(userId, { name: 'New Name' });
```

## Switching to Real Backend

To switch to a real Django backend:

1. Update base URL in each API file
2. Replace localStorage operations with fetch/axios calls
3. Handle authentication tokens properly
4. Remove artificial delays

Each API function has a comment indicating the corresponding Django endpoint.

## Demo Credentials

- **Email:** demo@skillsync.com
- **Password:** any password (mock accepts any)
