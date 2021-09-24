import { env } from "environment"
import { Notification } from "models/api/Notification"
import { http, HttpResponse } from "utils/http"

/**
 * Get list of notifications
 */
export function listNotifications(): HttpResponse<Notification[]> {
  return http.get(`${env.API_URL}/api/notifications/`)
}

/**
 * Get notification count
 */
export function countNotification(): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/count/`)
}

/**
 * Mark notifications as read
 */
export function markAllAsReadNotification(): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/mark_all_as_read/`)
}

/**
 * Mark notifications as unread
 */
export function markAllAsUnreadNotification(): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/mark_all_as_unread/`)
}

/**
 * Count of unread notifications
 */
export function unreadCountNotification(): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/unread_count/`)
}

/**
 *
 * @param id A UUID string identifying this notification
 */
export function retrieveNotification(id: string): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/${id}/`)
}

/**
 * Delete notification
 * @param id A UUID string identifying this notification
 */
export function destroyNotification(id: string): HttpResponse<void> {
  return http.delete(`${env.API_URL}/api/notifications/${id}/`)
}

/**
 * Mark notification as read
 * @param id A UUID string identifying this notification
 */
export function readNotification(id: string): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/${id}/read/`)
}

/**
 * Mark notification as unread
 * @param id A UUID string identifying this notification
 */
export function unreadNotification(id: string): HttpResponse<Notification> {
  return http.get(`${env.API_URL}/api/notifications/${id}/unread/`)
}
