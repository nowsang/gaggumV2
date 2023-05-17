package com.gaggum

import androidx.room.*

@Entity
data class Client (
    @PrimaryKey(autoGenerate = true)
    val id: Int,
    val client: String,
    val turtleId: Int
)

@Dao
interface ClientDao {
    @Insert
    fun insert(client: Client)

    @Query("SELECT * FROM Client WHERE client = :client")
    fun getTurtleId(client : String): Client
}

@Database(entities = [Client::class], version = 1)
abstract class ClientDatabase : RoomDatabase() {
    abstract fun clientDao() : ClientDao
}